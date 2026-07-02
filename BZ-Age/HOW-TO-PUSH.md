# Backing This Repo Up to GitHub

**The repo is live at https://github.com/Jwood1126-coder/BZ-Age and the first full push happened
July 2, 2026.** The rule from here on is simple:

> **Push at the end of every work session.** Codespaces expire; GitHub doesn't. Anything not
> pushed exists only on a machine with a countdown timer.

## The routine (from the codespace terminal, or ask Claude to do it)

```bash
git add -A
git commit -m "Short description of what changed"
git push
```

That's the whole workflow. If Claude did the work, ask it to commit and push — it will write a
descriptive commit message.

## Checking you're safe

```bash
git status        # "nothing to commit, working tree clean" = everything is saved locally
git log origin/main -1 --oneline   # what GitHub has
```

If `git status` shows modified or untracked files, they are NOT on GitHub yet.

## Opening this as an Obsidian vault (unchanged)

Open Obsidian → "Open folder as vault" → point it at the BZ-Age folder. For Claude integration
inside Obsidian, options include claudian, obsidian-ai, or AI Assistant; in any session, load
`CLAUDE.md` first so the editorial DNA is active.

## Change hygiene

Every substantive change should get an entry in `04-Working-Notes/Revision-Log.md`, and any
dossier-affecting change should keep `08-Fable-Dossier/00-INDEX.md` statuses current.
