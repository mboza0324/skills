# Instructions for AI Agents

**Applies to:** ChatGPT, Claude, Codex, or any other LLM-based agent.

## Read in This Order

1. **`AGENT_RULES.md`** – Mandatory rules for all operations.
2. **`AGENT_USAGE_RULES.md`** – How to apply skills in this repository.
3. **`SKILLS_GUIDE.md`** – Describes available skills and when to use them.

## Key Points

- **GAAI is pre-installed** in `.gaai/`. Do NOT run `install-gaai.sh` unless you are updating GAAI.
- **Skills are in `agentspace/`** – use them when they match the user's request.
- When creating a new repository, **copy all files** from this repo to the target.
- **Do NOT overwrite** existing `.gitignore`, `.env.example`, or `README.md` – merge them carefully.
- If in doubt, **ask the user** for clarification before making changes.