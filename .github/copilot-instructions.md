# GitHub Copilot Instructions

## Repository Role

- Repository: `vllm-general-plugin-template`
- Purpose: reusable standalone template for out-of-tree vLLM plugins

## Critical Boundary

- Do **not** modify `/home/shuhao/reference-repos/vllm` when using this template.
- If a future plugin built from this template truly requires upstream-local changes, clone or vendor vLLM inside the derived repository and patch there.
- The template should teach clean plugin boundaries, not direct edits to the reference checkout.

## Working Rules

- Keep the template minimal and reusable.
- Keep example plugin logic under `src/`.
- Record template changes in this repository's `CHANGELOG.md` only.
- Do not write template-repo changes into `/home/shuhao/sagellm/CHANGELOG.md`.
- Update `README.md` if the recommended plugin boundary changes.
- Do not create `.venv` or `venv`.

## Testing

```bash
PYTHONPATH=src pytest -q
```