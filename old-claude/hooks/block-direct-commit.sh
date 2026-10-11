#!/bin/bash
# PreToolUse hook: blocks any Bash command containing "git commit"
# unless it goes through the commit.sh wrapper script.

INPUT=$(cat)
TOOL=$(echo "$INPUT" | jq -r '.tool_name')

if [ "$TOOL" != "Bash" ]; then
  exit 0
fi

COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command')

if echo "$COMMAND" | grep -q 'git commit' && ! echo "$COMMAND" | grep -q 'commit\.sh'; then
  echo '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"Direct git commit is not allowed. Use the committer subagent which calls .ai/scripts/commit.sh."}}'
  exit 0
fi

exit 0
