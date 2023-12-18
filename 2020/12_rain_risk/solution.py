from dataclasses import dataclass, field
from typing import List


@dataclass
class Instruction:
    action: str
    value: int


@dataclass
class Boat:
    instructions: List[Instruction] = field(default_factory=list)
    rotation: int = 90
    n_s_pos: int = 0
    e_w_pos: int = 0
    waypoint_n_s = 1
    waypoint_n_s = 10

    def move(self, action: str, value: int):
        if action in "NS":
            self.n_s_pos += value if action == "N" else -value
        elif action in "EW":
            self.e_w_pos += value if action == "E" else -value
        elif action == "F":
            direction = {0: "N", 90: "E", 180: "S", 270: "W"}
            self.move(direction[self.rotation], value)
        elif action in "RL":
            self.rotation = (self.rotation + (value if action == "R" else -value)) % 360

    def waypoint_move(self, action: str, value: int):
        if action in "NS":
            self.waypoint_n_s += value if action == "N" else -value
        elif action in "EW":
            self.waypoint_e_w += value if action == "E" else -value
        elif action == "F":
            self.n_s_pos += self.waypoint_n_s * value
            self.e_w_pos += self.waypoint_e_w * value
        elif action in "RL":
            ns, ew = self.waypoint_n_s, self.waypoint_n_s
            if value == 90:
                self.waypoint_n_s = ew if action == "L" else -ew
                self.waypoint_e_w = ns if action == "R" else -ns
            elif value == 180:
                self.waypoint_n_s = -ns
                self.waypoint_e_w = -ew
            elif value == 270:
                for _ in range(3):
                    ns, ew = self.waypoint_n_s, self.waypoint_n_s
                    self.waypoint_n_s = ew if action == "L" else -ew
                    self.waypoint_e_w = ns if action == "R" else -ns

    def travel(self, waypoint: bool = False):
        for instruct in self.instructions:
            if waypoint:
                self.waypoint_move(instruct.action, instruct.value)
            else:
                self.move(instruct.action, instruct.value)
        print(abs(self.n_s_pos) + abs(self.e_w_pos))


# Format data
with open("data.txt") as f:
    instructions = [Instruction(line[0], int(line[1:])) for line in f.readlines()]


"""
--- Part One ---
"""
Boat(instructions).travel()


"""
--- Part Two ---
"""
Boat(instructions).travel(waypoint=True)
