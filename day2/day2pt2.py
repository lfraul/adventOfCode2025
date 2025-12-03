file = open("input.txt", "r")

def is_invalid(s):
    if (length := len(s)) < 2: 
        return False
    
    a, b = 0, 1
    while b < length:
        a = 0
        while b < length and s[a] != s[b]:
            b += 1
            if b > length // 2:
                return False
        
        while b < length and s[a] == s[b]:
            a += 1
            b += 1

    return not ((b - a) == 0 or length % (b - a) != 0)
            
total = 0
for r in file.readline().split(","):
    bounds = r.split("-")
    for i in range(int(bounds[0]), int(bounds[1]) + 1):
        if is_invalid(str(i)):
            total += i
print(total)

