#!/bin/bash

echo "Generating keys..."
.venv/bin/python src/generate_keys.py

echo ""
echo "Signing agents..."
.venv/bin/python src/sign_agents.py

echo ""
echo "Resolving claims-review.agent"
.venv/bin/python src/resolve_agent.py claims-review.agent

echo ""
echo "Resolving policy-summary.agent"
.venv/bin/python src/resolve_agent.py policy-summary.agent

echo ""
echo "Running tamper detection demo"
.venv/bin/python src/tamper_demo.py