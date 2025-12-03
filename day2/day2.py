file = open("input.txt", "r")

line = file.readline().strip()

def is_invalid(s):
    if len(s) % 2 != 0:
        return False
    
    if s[0:(len(s)//2)] == s[(len(s)//2):len(s)]:
        return True
    return False

ranges = line.split(",")
total = 0
for r in ranges:
    bounds = r.split("-")
    start = int(bounds[0])
    end = int(bounds[1])
    count = 0
    for i in range(start, end + 1):
        if is_invalid(str(i)):
            total += i
print(total)

