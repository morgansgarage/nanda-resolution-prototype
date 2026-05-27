import base64
import json
import sys
from pathlib import Path

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import serialization


REGISTRY_PATH = Path("registry.json")
PUBLIC_KEY_PATH = Path("keys/public_key.pem")


def load_public_key():
    public_key_bytes = PUBLIC_KEY_PATH.read_bytes()
    return serialization.load_pem_public_key(public_key_bytes)


def canonical_agent_bytes(agent_data):
    unsigned_data = dict(agent_data)
    unsigned_data["signature"] = ""

    canonical_json = json.dumps(
        unsigned_data,
        sort_keys=True,
        separators=(",", ":"),
    )

    return canonical_json.encode("utf-8")


def verify_agentfacts(agent_data, public_key):
    signature = base64.b64decode(agent_data["signature"])
    message = canonical_agent_bytes(agent_data)

    try:
        public_key.verify(signature, message)
        return True
    except InvalidSignature:
        return False


def resolve_agent(agent_name):
    registry = json.loads(REGISTRY_PATH.read_text())

    if agent_name not in registry:
        raise ValueError(f"Agent not found in registry: {agent_name}")

    agent_addr = registry[agent_name]["agent_addr"]
    agent_path = Path(agent_addr)

    agent_data = json.loads(agent_path.read_text())
    public_key = load_public_key()
    is_verified = verify_agentfacts(agent_data, public_key)

    return {
        "agent_name": agent_name,
        "agent_addr": agent_addr,
        "agentfacts": agent_data,
        "verified": is_verified,
    }


def main():
    if len(sys.argv) != 2:
        print("Usage: python src/resolve_agent.py <agent-name>")
        print("Example: python src/resolve_agent.py claims-review.agent")
        sys.exit(1)

    agent_name = sys.argv[1]
    result = resolve_agent(agent_name)

    print("\nNANDA Resolution Result")
    print("-----------------------")
    print(f"Agent Name: {result['agent_name']}")
    print(f"AgentAddr:  {result['agent_addr']}")
    print(f"Verified:   {result['verified']}")

    print("\nAgentFacts")
    print("----------")
    print(f"Display Name: {result['agentfacts']['display_name']}")
    print(f"Description:  {result['agentfacts']['description']}")
    print(f"Endpoint:     {result['agentfacts']['endpoint']}")
    print(f"Capabilities: {', '.join(result['agentfacts']['capabilities'])}")


if __name__ == "__main__":
    main()