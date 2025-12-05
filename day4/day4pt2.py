    
file = open("input.txt", "r")

rolls_map: list[list[int]] = [[]]
index = 0
while line := file.readline().strip():
    rolls_map.append([])
    for i, char in enumerate(line):
        rolls_map[index].append(1 if char == "@" else 0)
    index += 1

file.close()

rolls = sum(sum(row) for row in rolls_map)

y_max = index - 1
x_max = len(rolls_map[0]) - 1
seen: set = set()
      
def remove_roll(y, x):
    rolls_adj = set()
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
                if rolls_map[yi][xj] == 1: 
                    rolls_adj.add((yi, xj))
             
    if len(rolls_adj) < 4:
        rolls_map[y][x] = 0
        if (y, x) in seen:
            seen.remove((y, x))
        for (yi, xj) in rolls_adj.intersection(seen):
            remove_roll(yi, xj)
    else: 
        seen.add((y, x))

    
for y_index in range(x_max + 1):
    for x_index in range(y_max + 1): 
        if rolls_map[y_index][x_index] == 1:
            remove_roll(y_index, x_index)
            
final_rolls = sum(sum(row) for row in rolls_map)
print(rolls - final_rolls)