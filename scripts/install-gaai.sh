#!/usr/bin/env bash
set -euo pipefail

: "${GAAI_REPO:?Set GAAI_REPO to the approved GAAI framework Git URL}"

GAAI_REF="${GAAI_REF:-e8242f3ceee2d42dd9ab09474ec495899fe83098}"
TARGET="${1:-.}"
TOOL="${GAAI_TOOL:-other}"

tmp_dir="$(mktemp -d)"
trap 'rm -rf "$tmp_dir"' EXIT

git clone --quiet "$GAAI_REPO" "$tmp_dir/gaai"
git -C "$tmp_dir/gaai" checkout --quiet "$GAAI_REF"

bash "$tmp_dir/gaai/.gaai/core/scripts/install.sh"   --target "$TARGET"   --tool "$TOOL"   --yes

echo "Installed GAAI from the configured repository at $GAAI_REF"
echo "Review changes with: git status && git diff --stat"
