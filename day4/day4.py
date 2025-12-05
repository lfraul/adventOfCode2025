file = open("input.txt", "r")

rolls_map: list[list[int]] = [[]]
index = 0
while line := file.readline().strip():
    rolls_map.append([])
    for i, char in enumerate(line):
        rolls_map[index].append(1 if char == "@" else 0)
    index += 1

file.close()

y_max = index - 1
x_max = len(rolls_map[0]) - 1
    
def can_reach(y, x): 
    count = 0
    y_indices, x_indices = [y], [x]
    if y < y_max: 
        y_indices.append(y+1)
    if y > 0: 
        y_indices.append(y-1)
    if x < x_max: 
        x_indices.append(x+1)
    if x > 0: 
        x_indices.append(x-1)
    
    for yi in sorted(y_indices): 
        for xj in sorted(x_indices): 
            if (yi, xj) != (y, x):
                count += rolls_map[yi][xj]

    return count < 4


total = 0
for y_index in range(y_max + 1):
    for x_index in range(x_max + 1): 
        if rolls_map[y_index][x_index] == 1 and can_reach(y_index, x_index):
            total += 1

            
print(total)
