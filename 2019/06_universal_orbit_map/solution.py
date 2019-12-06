from dataclasses import dataclass, field
from typing import List

# Format data
with open("data.txt") as f:
    orbits = [[s.strip() for s in o.split(")")] for o in f.readlines()]


@dataclass
class Node:
    name: str
    children: List = field(default_factory=list)

    def add_child(self, obj):
        self.children.append(obj)
