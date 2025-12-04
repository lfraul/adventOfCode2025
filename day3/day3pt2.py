from collections import deque
file = open("input.txt", "r")
    
def bank_voltage(batteries: str):
    voltage = [-1] * 12
    length = len(batteries)
    q = deque(batteries)
    filled = 0
    for i in range(length):
        value = int(q.popleft())
        j = max(filled, 12 - (length - i))
        while j < 12:
            if value > voltage[j]:
                voltage[j] = value
                voltage = voltage[:j+1] + [-1] * (12 - (j+1))
                if value == 9:
                    filled += 1
                break
            j += 1
        
    return "".join(str(v) for v in voltage)

total_voltage = 0
while battery_bank := file.readline():
    volts = int(bank_voltage(battery_bank.strip("\n")))
    total_voltage += volts

file.close()

print(total_voltage)
