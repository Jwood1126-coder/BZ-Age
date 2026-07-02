# How to Push This Repo to GitHub

This local repo is built and ready. To push it to your empty GitHub repo at https://github.com/Jwood1126-coder/BZ-Age.git, do the following from a terminal on your machine.

## Option A — Easiest (recommended)

```bash
# 1. Download and extract the BZ-Age.zip file to wherever you keep projects.
#    This creates a folder called BZ-Age/

# 2. Open a terminal in that folder
cd BZ-Age

# 3. Initialize git (if you haven't already)
git init
git branch -M main

# 4. Stage and commit everything
git add .
git commit -m "Initial commit: Bronze Age podcast project structure"

# 5. Connect to your GitHub repo
git remote add origin https://github.com/Jwood1126-coder/BZ-Age.git

# 6. Push
git push -u origin main
```

If GitHub asks for credentials, use a Personal Access Token (not your password). You can generate one at GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic), with the `repo` scope.

## Option B — If your local repo on GitHub already has files (README, .gitignore, etc.)

```bash
# 1. Clone your existing repo
git clone https://github.com/Jwood1126-coder/BZ-Age.git
cd BZ-Age

# 2. Copy all files from the extracted zip INTO this folder (overwriting any conflicts)
#    On macOS/Linux:
cp -r /path/to/extracted/BZ-Age/* .
cp -r /path/to/extracted/BZ-Age/.gitignore .   # gitignore needs explicit copy
cp /path/to/extracted/BZ-Age/.* . 2>/dev/null  # any other dotfiles

# 3. Stage, commit, push
git add .
git commit -m "Add Bronze Age podcast project structure"
git push
```

## Opening this as an Obsidian vault

Once the files are on your machine, open Obsidian and choose "Open folder as vault" — point it at the BZ-Age folder. Everything will render immediately.

For the Claude plugin integration (the writing-equivalent-of-Copilot setup you asked about), install one of:
- **claudian** — embeds Claude Code in your vault (most capable, requires API setup)
- **Spencer Marx's obsidian-ai** — similar approach
- **AI Assistant by qgrail** — simpler, lower commitment

Then in any session, the first move is to load `CLAUDE.md` into the AI's context. That's what makes the editorial DNA active for that session.

## After the first push

From this point forward, the workflow is normal:

```bash
# Make changes locally
git add .
git commit -m "Description of what changed"
git push
```

Every substantive change should also get an entry in `04-Working-Notes/Revision-Log.md` so future-you (and future Claude sessions) can reconstruct the reasoning.
