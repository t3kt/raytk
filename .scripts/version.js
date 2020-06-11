#!/usr/bin/env node

const { resolve } = require("path");
const { readdir, rename, unlink, readFile, writeFile } = require("fs").promises;

// TODO
const vPrev = require("../.jekyll-theme-hydejack-pro/assets/version.json").version;
const vNext = require("../.jekyll-theme-hydejack-pro/package.json").version;

const ENC = "utf-8";

const FILES = [
  "./_data/authors.yml",
  "./CHANGELOG.md",
  "./download.md",
  "./README.md",
  "./thank-you.md",
].map(f => resolve(f));

// <https://stackoverflow.com/a/45130990/870615>
async function getFiles(dir) {
  const dirents = await readdir(dir, { withFileTypes: true });
  const files = await Promise.all(dirents.map((dirent) => {
    const res = resolve(dir, dirent.name);
    return dirent.isDirectory() ? getFiles(res) : res;
  }));
  return Array.prototype.concat(...files);
}

(async function main() {
  try {
    const prev = vPrev.replace(/\./g, "\\.");
    const prevRegExp = new RegExp(prev, "g");

    const args = await Promise.all([
      getFiles("./hyde/_posts"),
      getFiles("./hydejack/_posts"),
      getFiles("./_projects"),
      getFiles("./docs"),
    ]);
      
    const files = Array.prototype.concat.call(FILES, ...args);

    const pFiles = Promise.all(
      files
        .filter(([f]) => !f.startsWith("."))
        .map(f => [f, readFile(f, ENC)])
        .map(async ([f, p]) => {
          const content = await p;

          if (f.includes("CHANGELOG")) {
            const pattern = new RegExp(`([^v])${prev}`, "g");
            return [f, content.replace(pattern, `$1${vNext}`)];
          }

          return [f, content.replace(prevRegExp, vNext)];
        })
        .map(async p => {
          const [f, content] = await p;
          return writeFile(f, content, ENC);
        })
    );

    await pFiles;

    // const pUnlink = Promise.all(
    //   (await getFiles('./assets/js'))
    //     .filter(f => f.includes(vPrev))
    //     .map(unlink)
    // );

    // const pJSCSS = rename(
    //   resolve(`./assets/css/hydejack-${vPrev}.css`),
    //   resolve(`./assets/css/hydejack-${vNext}.css`)
    // );

    // await Promise.all([pUnlink, pFiles, pJSCSS]);

    process.exit(0);
  } catch (e) {
    console.error(e); // eslint-disable-line
    process.exit(1);
  }
})();
