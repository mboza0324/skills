#!/usr/bin/env bash
# install-skills.sh — Installs skills globally (find.sh, etc.) for any devcontainer

set -euo pipefail

SKILLS_REPO="https://github.com/mboza0324/skills.git"
SKILLS_DIR="$HOME/.skills"

# Clone or update the skills repo
if [ -d "$SKILLS_DIR" ]; then
  echo "🔄 Updating skills repo..."
  git -C "$SKILLS_DIR" pull --quiet
else
  echo "📦 Cloning skills repo..."
  git clone --quiet "$SKILLS_REPO" "$SKILLS_DIR"
fi

# Make find.sh executable and link it globally
chmod +x "$SKILLS_DIR/scripts/find.sh"
sudo ln -sf "$SKILLS_DIR/scripts/find.sh" /usr/local/bin/find-skills

# Install jq if missing (required for find.sh)
if ! command -v jq &> /dev/null; then
  echo "📥 Installing jq..."
  sudo apt-get update -qq && sudo apt-get install -y -qq jq
fi

# Also link other scripts if needed (optional)
# sudo ln -sf "$SKILLS_DIR/scripts/discover-skill.sh" /usr/local/bin/discover-skill

echo "✅ find-skills installed globally. Run: find-skills '<query>'"
