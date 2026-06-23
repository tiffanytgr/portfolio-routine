#!/bin/bash
set -euo pipefail

# Only run the dependency install in Claude Code on the web (remote) sessions.
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# The portfolio routine uses `requests` to deliver the rundown via Telegram.
pip install --quiet requests
