import json
from pathlib import Path

from resolve_agent import resolve_agent


AGENT_FILE = Path("agents/claims_agent.json")
AGENT_NAME = "claims-review.agent"


def main():
    original_text = AGENT_FILE.read_text()
    agent_data = json.loads(original_text)

    print("\nBefore tampering")
    print("----------------")
    result = resolve_agent(AGENT_NAME)
    print(f"Verified: {result['verified']}")

    print("\nTampering with AgentFacts...")
    agent_data["capabilities"].append("unauthorized_payment_approval")
    AGENT_FILE.write_text(json.dumps(agent_data, indent=2))

    print("\nAfter tampering")
    print("---------------")
    result = resolve_agent(AGENT_NAME)
    print(f"Verified: {result['verified']}")

    AGENT_FILE.write_text(original_text)

    print("\nAgentFacts restored.")


if __name__ == "__main__":
    main()