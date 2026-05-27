# NANDA Resolution Prototype

This prototype demonstrates a minimal NANDA-style agent resolution flow:

Agent Name → Index Lookup → AgentAddr → AgentFacts → Signature Verification

## Goal

A client can resolve an agent name, retrieve its metadata, verify that the metadata has not been tampered with, and act on the verified AgentFacts.

## Demo Agents

- claims-review.agent
- policy-summary.agent

## Planned Flow

1. Generate signing keys
2. Create AgentFacts files
3. Sign AgentFacts
4. Resolve an agent name through the registry
5. Verify the AgentFacts signature
6. Demonstrate tamper detection
