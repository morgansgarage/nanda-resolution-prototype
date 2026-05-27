# NANDA Resolution Prototype

A minimal working prototype demonstrating the core NANDA-style resolution flow:

```text
Agent Name → Registry Lookup → AgentAddr → AgentFacts → Signature Verification
```

This project was built as part of the Foundation for Agentic Networks VP of Engineering technical challenge.

---

# Overview

The prototype demonstrates how a client can:

1. Resolve an agent name through an index/registry
2. Retrieve AgentFacts metadata
3. Verify metadata authenticity using cryptographic signatures
4. Detect tampering of signed metadata

The implementation intentionally focuses on the smallest complete end-to-end flow rather than broader platform architecture.

---

# Architecture

## Components

### Registry

`registry.json`

Maps an agent name to an AgentAddr location.

Example:

```json
{
  "claims-review.agent": {
    "agent_addr": "agents/claims_agent.json"
  }
}
```

---

### AgentFacts

Located in:

```text
agents/
```

Each agent contains:

- metadata
- capabilities
- endpoint information
- cryptographic signature

Two demo agents are included:

- `claims-review.agent`
- `policy-summary.agent`

---

### Cryptographic Verification

The prototype uses:

- Ed25519 public/private key signing
- Canonicalized JSON serialization
- Signature verification during resolution

If AgentFacts are modified after signing, verification fails.

---

# Project Structure

```text
nanda-prototype/
│
├── agents/
│   ├── claims_agent.json
│   └── policy_agent.json
│
├── keys/
│   ├── private_key.pem
│   └── public_key.pem
│
├── src/
│   ├── generate_keys.py
│   ├── sign_agents.py
│   ├── resolve_agent.py
│   └── tamper_demo.py
│
├── registry.json
├── resolve.sh
├── run_demo.sh
├── requirements.txt
└── README.md
```

---

# Setup

## Create Virtual Environment

```bash
python3 -m venv .venv
```

## Activate Environment

Mac/Linux:

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Prototype

## Generate Keys

```bash
.venv/bin/python src/generate_keys.py
```

## Sign AgentFacts

```bash
.venv/bin/python src/sign_agents.py
```

## Resolve an Agent

```bash
./resolve.sh claims-review.agent
```

or

```bash
./resolve.sh policy-summary.agent
```

---

# Tamper Detection Demo

```bash
.venv/bin/python src/tamper_demo.py
```

Expected result:

```text
Before tampering
Verified: True

After tampering
Verified: False
```

---

# Design Decisions

This prototype intentionally prioritizes:

- clear end-to-end execution
- cryptographic verification
- minimal operational complexity
- developer readability
- runnable local workflows

The implementation does not attempt to solve:

- distributed discovery
- decentralized identity infrastructure
- production networking
- multi-party trust management
- enterprise routing
- scalability concerns

Those concerns were intentionally deferred in favor of a minimal verifiable resolution flow.

---

# AI Tooling

AI-assisted development tools were used during implementation for:

- scaffolding
- troubleshooting
- iterative refinement
- documentation generation

All architectural decisions, scoping, and final implementation choices were reviewed and validated manually.

---

# Future Improvements

Potential next steps include:

- HTTP-based registry service
- DID-based identity support
- W3C Verifiable Credentials
- Docker packaging
- multi-node resolution
- visualization dashboard
- automated tests
- agent registration workflows

# Tradeoffs

This implementation intentionally prioritizes:

- simplicity over distributed architecture
- cryptographic verification over networking complexity
- local execution over hosted infrastructure
- readability over abstraction layers

The goal was to demonstrate the narrowest complete verifiable resolution flow.

---

# Author

Scott Morgan
