# --- Format data ---
with open("01_data.txt") as f:
    lines = f.readlines()

frequency_modifiers = [int(line.strip()) for line in lines]

# --- Part one ---
print(sum(frequency_modifiers))

# --- Part two ---
reached_freqs = set()
current_freq = 0
found = False
while not found:
    for freq in frequency_modifiers:
        if current_freq in reached_freqs:
            print(current_freq)
            found = True
            break
        else:
             reached_freqs.add(current_freq)
             current_freq += freq

