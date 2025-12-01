file = open("input.txt", "r")

counter = 0
location = 50
for line in file.readlines():
    location = (location + (int(line[1:]) if line[0] == "R" else -int(line[1:]))) % 100
        
    if location == 0:
        counter += 1

print(counter)
