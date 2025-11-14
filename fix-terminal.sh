#!/bin/bash
# Fix terminal flickering by setting proper TERM value
# Usage: source fix-terminal.sh  (or . fix-terminal.sh)

if [ "$TERM" = "dumb" ] || [ -z "$TERM" ]; then
    export TERM=xterm-256color
    echo "✓ TERM set to xterm-256color (was: ${TERM:-unset})"
else
    echo "✓ TERM already set to: $TERM"
fi

