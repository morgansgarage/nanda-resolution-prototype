import base64
import json
from pathlib import Path

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519


PRIVATE_KEY_PATH = Path("keys/private_key.pem")

AGENT_FILES = [
    Path("agents/claims_agent.json"),
    Path("agents/policy_agent.json"),
]


def load_private_key():
    private_key_bytes = PRIVATE_KEY_PATH.read_bytes()
    return serialization.load_pem_private_key(
        private_key_bytes,
        password=None,
    )


def canonical_agent_bytes(agent_data):
    unsigned_data = dict(agent_data)
    unsigned_data["signature"] = ""

    canonical_json = json.dumps(
        unsigned_data,
        sort_keys=True,
        separators=(",", ":"),
    )

    return canonical_json.encode("utf-8")


def sign_agent_file(agent_file, private_key):
    agent_data = json.loads(agent_file.read_text())

    message = canonical_agent_bytes(agent_data)
    signature = private_key.sign(message)

    agent_data["signature"] = base64.b64encode(signature).decode("utf-8")

    agent_file.write_text(json.dumps(agent_data, indent=2))

    print(f"Signed {agent_file}")


def main():
    private_key = load_private_key()

    for agent_file in AGENT_FILES:
        sign_agent_file(agent_file, private_key)


if __name__ == "__main__":
    main()