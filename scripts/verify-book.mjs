import fs from 'node:fs';
import path from 'node:path';
import process from 'node:process';
import YAML from 'yaml';
import { createHash } from 'node:crypto';

const root = process.cwd();
const required = ['myst.yml', 'index.md', '.github/workflows/ci.yml', '.github/workflows/deploy.yml', 'pwa/service-worker.js'];
const missing = required.filter((file) => !fs.existsSync(path.join(root, file)));
if (missing.length) throw new Error(`Missing required files: ${missing.join(', ')}`);

const config = YAML.parse(fs.readFileSync(path.join(root, 'myst.yml'), 'utf8'));
const errors = [];
if (!config.project?.title) errors.push('project.title is required');
if (!config.project?.short_title) errors.push('project.short_title is required');
if (config.project?.open_access !== true) errors.push('project.open_access must be true');
if (!config.project?.github) errors.push('project.github is required');
if (!Array.isArray(config.project?.toc) || !config.project.toc.length) errors.push('project.toc must contain at least one page');

const pages = [];
function collectToc(entries) {
  for (const entry of entries || []) {
    if (entry.file) pages.push(entry.file);
    collectToc(entry.children);
  }
}
collectToc(config.project?.toc);

const labels = new Set();
const refs = [];
const solutionTargets = [];
for (const file of pages) {
  const absolute = path.join(root, file);
  if (!fs.existsSync(absolute)) {
    errors.push(`Missing TOC page: ${file}`);
    continue;
  }
  const text = fs.readFileSync(absolute, 'utf8');
  for (const match of text.matchAll(/\(([A-Za-z][\w:-]*)\)=/g)) labels.add(match[1]);
  for (const match of text.matchAll(/:label:\s*(\S+)/g)) labels.add(match[1]);
  for (const match of text.matchAll(/\{figure\}\s+(\S+)/g)) {
    const image = path.resolve(path.dirname(absolute), match[1]);
    if (!fs.existsSync(image)) errors.push(`Missing figure ${match[1]} in ${file}`);
  }
  for (const match of text.matchAll(/!\[[^\]]*]\(([^)\s]+)\)/g)) {
    if (/^(https?:|mailto:)/.test(match[1])) continue;
    const image = path.resolve(path.dirname(absolute), match[1].split('#')[0]);
    if (!fs.existsSync(image)) errors.push(`Missing image ${match[1]} in ${file}`);
  }
  for (const match of text.matchAll(/\{ref\}`(?:[^`<]*<)?([A-Za-z][\w:-]*)>?`/g)) refs.push([file, match[1]]);
  for (const match of text.matchAll(/\{solution\}\s+(\S+)/g)) solutionTargets.push([file, match[1]]);
}
for (const [file, label] of refs) {
  if (!labels.has(label)) errors.push(`Unresolved reference ${label} in ${file}`);
}
for (const [file, label] of solutionTargets) {
  if (!labels.has(label)) errors.push(`Solution without exercise ${label} in ${file}`);
}

// Source omissions had plain-text citations, so the local-image checks alone
// could not detect them. Keep every restored figure and its license auditable.
const restored = JSON.parse(fs.readFileSync(path.join(root, 'images/restored/manifest.json'), 'utf8'));
const openLicenses = /^(CC BY(?:-SA)? [234]\.0|CC BY-SA 2\.5|CC0|Public domain)$/;
for (const figure of restored) {
  const page = fs.readFileSync(path.join(root, figure.page), 'utf8');
  if (!page.includes(`:label: ${figure.label}\n`)) errors.push(`Missing restored Figure ${figure.number} in ${figure.page}`);
  for (const asset of figure.assets) {
    const filename = path.join(root, 'images/restored', asset.file);
    if (!fs.existsSync(filename)) {
      errors.push(`Missing restored asset: ${asset.file}`);
      continue;
    }
    if (!openLicenses.test(asset.license) || !asset.credit || !asset.source || !asset.license_url || !asset.alt) {
      errors.push(`Incomplete open-license attribution or alt text: ${asset.file}`);
    }
    const digest = createHash('sha256').update(fs.readFileSync(filename)).digest('hex');
    if (digest !== asset.sha256) errors.push(`Restored asset differs from its provenance record: ${asset.file}`);
    if (!page.includes(`../images/restored/${asset.file}`)) errors.push(`Restored asset is not displayed: ${asset.file}`);
  }
}
if (errors.length) throw new Error(errors.join('\n'));

console.log(`Book structure is valid (${pages.length} pages, ${labels.size} labels).`);
