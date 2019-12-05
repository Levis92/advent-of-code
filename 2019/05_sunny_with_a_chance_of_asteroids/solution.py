# Format data
with open("data.txt") as f:
    instructions = [int(i) for i in f.readline().split(",")]


"""
--- Part one ---
"""
numbers = [*instructions]


def get_val(pos, mode):
    return numbers[numbers[pos]] if mode == 0 else numbers[pos]


def set_val(pos, val, mode):
    if mode == 0:
        numbers[numbers[pos]] = val
    else:
        numbers[pos] = val


def translate_instruction(instruction):
    opcode = int(str(instruction)[-2:])
    param_modes = [int(m) for m in str(instruction)[:-2]]
    param_modes = [0] * (3 - len(param_modes)) + param_modes
    return opcode, param_modes


def compute(instruction, pos):
    opcode, param_modes = translate_instruction(instruction)
    m3, m2, m1 = param_modes
    if opcode == 1:
        set_val(pos + 3, get_val(pos + 1, m1) + get_val(pos + 2, m2), m3)
        return pos + 4
    elif opcode == 2:
        set_val(pos + 3, get_val(pos + 1, m1) * get_val(pos + 2, m2), m3)
        return pos + 4
    elif opcode == 3:
        param = input("Provide value to save\n")
        set_val(pos + 1, int(param), m1)
        return pos + 2
    elif opcode == 4:
        print(get_val(pos + 1, m1))
        return pos + 2
    elif opcode == 99:
        print("Program has quit successfully")
        return -1
    else:
        raise ValueError(f"Expected 1, 2, 3, 4, 50 or 99 but got: {opcode}")


position = 0
while len(numbers) > position:
    position = compute(numbers[position], position)
    if position == -1:
        break


"""
--- Part two ---
"""
numbers = [*instructions]


def compute_2(instruction, pos):
    opcode, param_modes = translate_instruction(instruction)
    m3, m2, m1 = param_modes
    if opcode == 1:
        set_val(pos + 3, get_val(pos + 1, m1) + get_val(pos + 2, m2), m3)
        return pos + 4
    elif opcode == 2:
        set_val(pos + 3, get_val(pos + 1, m1) * get_val(pos + 2, m2), m3)
        return pos + 4
    elif opcode == 3:
        param = input("Provide value to save\n")
        set_val(pos + 1, int(param), m1)
        return pos + 2
    elif opcode == 4:
        print(get_val(pos + 1, m1))
        return pos + 2
    elif opcode == 5:
        if get_val(pos + 1, m1) > 0:
            return get_val(pos + 2, m2)
        return pos + 3
    elif opcode == 6:
        if get_val(pos + 1, m1) == 0:
            return get_val(pos + 2, m2)
        return pos + 3
    elif opcode == 7:
        if get_val(pos + 1, m1) < get_val(pos + 2, m2):
            set_val(pos + 3, 1, m3)
        else:
            set_val(pos + 3, 0, m3)
        return pos + 4
    elif opcode == 8:
        if get_val(pos + 1, m1) == get_val(pos + 2, m2):
            set_val(pos + 3, 1, m3)
        else:
            set_val(pos + 3, 0, m3)
        return pos + 4
    elif opcode == 99:
        print("Program has quit successfully")
        return -1
    else:
        raise ValueError(f"Expected 1, 2, 3, 4, 50 or 99 but got: {opcode}")


position = 0
while len(numbers) > position:
    position = compute_2(numbers[position], position)
    if position == -1:
        break
