from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class Operation:
    code: str
    value: int


@dataclass
class GameConsole:
    ops: List[Operation] = field(default_factory=list)
    index: int = 0
    acc: int = 0
    visited: List[int] = field(default_factory=list)

    def get_op(self) -> Operation:
        return self.ops[self.index]

    def exec_acc(self, val: int):
        self.acc += val

    def exec_jmp(self, offset: int):
        self.index += offset

    def next_index(self):
        self.index += 1

    def graceful_exit(self):
        if self.index in self.visited:
            return True
        self.visited.append(self.index)
        return False

    def run_program(self) -> Tuple[bool, int]:
        while self.index < len(self.ops):
            if self.graceful_exit():
                return False, self.acc
            op = self.get_op()
            if op.code == "acc":
                self.exec_acc(op.value)
            elif op.code == "jmp":
                self.exec_jmp(op.value)
                continue
            elif op.code == "nop":
                pass
            self.next_index()

        return True, self.acc


# Format data
with open("data.txt") as f:
    operations = [
        Operation(code, int(val))
        for code, val in (line.split() for line in f.readlines())
    ]


"""
--- Part One ---
"""
successful, val = GameConsole(operations).run_program()
print(val)


"""
--- Part Two ---
"""


def create_op(op: Operation, curr_i: int, target_i: int) -> Operation:
    if curr_i == target_i:
        return Operation("nop" if op.code == "jmp" else "nop", op.value)
    else:
        return Operation(op.code, op.value)


indexes_to_try = [i for i, op in enumerate(operations) if op.code in ("jmp", "nop")]

for index in indexes_to_try:
    new_operations = [create_op(op, i, index) for i, op in enumerate(operations)]
    successful, val = GameConsole(new_operations).run_program()
    if successful:
        print(val)
        break
