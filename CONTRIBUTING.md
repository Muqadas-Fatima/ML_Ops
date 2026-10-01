# Contributing Guidelines

## Branch Naming Rules
- Production: `main`
- Release Candidate: `staging`
- Integration: `dev`
- Features: `feat/<name>`
- Data & DVC: `data/<name>`
- Experiments: `exp/<member>-<idea>`
- Urgent Hotfixes: `fix/<name>`

## Commits & PRs
- Use Conventional Commits (`feat:`, `data:`, `exp:`, `fix:`, `chore:`).
- PRs into `dev` will be **Squash-merged**.
- Always run `dvc push` before `git push`.
