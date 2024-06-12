text = open('wordle-solver/solver/en_50k.txt', 'r')
lines = text.readlines()
for i, line in enumerate(lines):
    lines[i] = line[:-1]
new_lines = []
with open('wordle-solver/solver/output.txt', 'w') as f:
    for line in lines:
        word = line.split()
        if len(word[0]) == 5:
            f.write(line)
            f.write(', ')
