# vllm-general-plugin-template-copilot-agent

Use this agent when working in `vllm-general-plugin-template` on:

- reusable out-of-tree plugin scaffolding
- documentation of the official `vllm.general_plugins` boundary
- template-safe examples that avoid upstream checkout pollution

## Hard Boundary

- Never use this template as justification for directly editing `/home/shuhao/reference-repos/vllm`.
- If a derived project needs deeper integration, vendor or clone vLLM inside that derived repository.