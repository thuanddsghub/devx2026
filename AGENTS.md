# Repository instructions

## Environment

- Use the Python virtual environment located at `.ao`.
- Run Python commands with `python`.
- Install packages using `python -m pip`.
- Do not modify the Ubuntu system Python environment.

## Project structure

- Application code belongs in `src/`.
- Tests belong in `tests/`.
- Documentation belongs in `docs/`.
- Generated files belong in `outputs/`.

## Code quality

- Follow PEP 8.
- Use type hints for public functions.
- Keep functions small and testable.
- Prefer pathlib for filesystem operations.
- Add tests for new behavior.

## Safety

- Never commit passwords, tokens, API keys, or `.env`.
- Do not modify files outside this repository.
- Do not delete files unless explicitly requested.
- Do not commit, push, merge, or create pull requests unless requested.

## Workflow

1. Inspect the repository before editing.
2. Present a short plan.
3. Make focused changes.
4. Run applicable tests.
5. Report modified files and validation results.
