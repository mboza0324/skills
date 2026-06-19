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

## 🔍 Skill Discovery (Before Building)

1. **Read `SKILL_INDEX.json`** – this lists all available internal skills.
2. **Match keywords** – compare the user's request against each skill's `keywords`.
3. **If a match is found** – read that skill's `SKILL.md` and recommend it with install instructions.
4. **If no match is found** – fall back to `AGENT_RULES.md` and build from scratch.
