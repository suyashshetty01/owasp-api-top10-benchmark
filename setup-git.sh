#!/usr/bin/env bash
# One-time setup: initialise this as a git repo and make the first commit.
# Run this from inside the repo folder after you've worked through
# PUBLISHING_CHECKLIST.md.

set -euo pipefail

if [ -d .git ]; then
  echo "Already a git repo — skipping git init."
else
  git init
fi

echo ""
echo "Before committing, double-check for secrets one more time:"
echo "  git grep -i 'eyJ' -- . ':!*.md'   (catches most JWTs)"
echo ""
read -p "Have you completed PUBLISHING_CHECKLIST.md and checked for secrets? [y/N] " confirm
if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
  echo "Stopping — work through the checklist first."
  exit 1
fi

git add .
git status
echo ""
echo "Review the file list above. If it looks right:"
echo "  git commit -m 'Initial artefact repo for MSc dissertation benchmark'"
echo ""
echo "Then create a repo on GitHub (via the website or 'gh repo create'),"
echo "and push:"
echo "  git remote add origin https://github.com/<your-username>/<repo-name>.git"
echo "  git branch -M main"
echo "  git push -u origin main"
