#!/bin/bash
set -e # exit with nonzero exit code if anything fails

cd "pages"
git init
git config user.name "Travis CI"
git config user.email "none@none.no"
git add .
git commit -m "Deploy to GitHub Pages"
git push --force --quiet "https://radium226:${GITHUB_TOKEN}@github.com/radium226/resume.git" master:gh-pages
