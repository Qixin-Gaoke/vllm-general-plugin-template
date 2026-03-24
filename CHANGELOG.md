# Changelog

## [Unreleased]

### Added

- Added a shared top-level `Makefile` with consistent `install-dev`, `smoke`, `test`, `lint`, `format`, `build`, `bench`, and `paper` targets.
- Added a top-level `CHANGELOG.md` so the template matches the standalone plugin repository structure used across the related vLLM and SGLang artifact repos.

### Changed

- Clarified changelog ownership: template changes must be recorded in this repository's own `CHANGELOG.md`, not in `/home/shuhao/sagellm/CHANGELOG.md`.
- Standardized local developer metadata by aligning `.[dev]` dependencies, pytest testpaths, and CONTRIBUTING workflow wording with the other standalone plugin repos.