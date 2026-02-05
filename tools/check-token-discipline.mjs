import fs from "node:fs";
import path from "node:path";

const ROOT = process.cwd();
const TARGET_DIRS = ["src/components", "src/layouts", "src/pages"];
const EXTENSIONS = new Set([".astro", ".css"]);
const HEX_COLOR = /#[0-9a-fA-F]{3,8}\b/g;

function walk(dir, files = []) {
  if (!fs.existsSync(dir)) return files;
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      walk(fullPath, files);
      continue;
    }
    if (EXTENSIONS.has(path.extname(entry.name))) {
      files.push(fullPath);
    }
  }
  return files;
}

const violations = [];

for (const relDir of TARGET_DIRS) {
  const absDir = path.join(ROOT, relDir);
  for (const file of walk(absDir)) {
    const content = fs.readFileSync(file, "utf8");
    const matches = content.match(HEX_COLOR);
    if (!matches) continue;
    violations.push({
      file: path.relative(ROOT, file),
      matches: [...new Set(matches)],
    });
  }
}

if (violations.length > 0) {
  console.error("Token discipline check failed. Raw hex values found:");
  for (const item of violations) {
    console.error(`- ${item.file}: ${item.matches.join(", ")}`);
  }
  process.exit(1);
}

console.log("Token discipline check passed.");
