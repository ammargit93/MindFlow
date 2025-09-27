from typing import List
import random

def random_balancer(urls: List[str]) -> str:
    idx = random.randint(0,len(urls)-1)
    return urls[idx]