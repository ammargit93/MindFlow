import json
import logging
from typing import *
# ------------------ Helper Functions ------------------ #
def parse_request_body(body_bytes: bytes) -> Dict[str, Any]:
    """Parse JSON request body safely."""
    if not body_bytes:
        return {}
    try:
        return json.loads(body_bytes.decode())
    except json.JSONDecodeError:
        return {}

def log_domain_counts(domain_count):
    """Log the request count per domain."""
    for domain, count in domain_count.items():
        logging.info(f"Domain {domain}: {count} requests")
