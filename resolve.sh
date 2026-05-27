#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: ./resolve.sh <agent-name>"
  echo "Example: ./resolve.sh claims-review.agent"
  exit 1
fi

AGENT_NAME=$1

echo ""
echo "=============================================="
echo "         NANDA Resolution Prototype"
echo "=============================================="
echo ""

echo "Resolution Flow"
echo "----------------"
echo ""
echo "  $AGENT_NAME"
echo "          │"
echo "          ▼"
echo "   registry.json"
echo "          │"
echo "          ▼"
echo "   AgentAddr"
echo "          │"
echo "          ▼"
echo "   AgentFacts"
echo "          │"
echo "          ▼"
echo "   Signature Verification"
echo "          │"
echo "          ▼"
echo "   VERIFIED AGENT"
echo ""

echo "Executing Resolution..."
echo ""

.venv/bin/python src/resolve_agent.py "$AGENT_NAME"