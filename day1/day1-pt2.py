file = open("input.txt", "r")

counter = 0
location = 50

for line in file.readlines():
    distance = int(line[1:])
    direction = 1 if line[0] == "R" else -1
    
    if distance >= 100:
        full_loops = distance // 100
        counter += full_loops
        distance = distance - (full_loops * 100)
    
    linear_position = location + (distance * direction)
    
    if location != 0 and not (100 > linear_position > 0):
        counter += 1
    
    location = linear_position % 100
    
print(counter)