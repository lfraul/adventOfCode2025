file = open("input.txt", "r")


def bank_voltage(batteries: str):
    length = len(batteries)
    tens, ones = int(batteries[0]), -1
    x = 1

    if length <= 2:
        return batteries

    while x < length:
        voltage = int(batteries[x])
        if voltage > tens and x + 1 < length:
            tens = voltage
            ones = int(batteries[x + 1])
        elif voltage > ones:
            ones = voltage
        x += 1

    return f"{tens}{ones}"


total_voltage = 0
while battery_bank := file.readline():
    volts = int(bank_voltage(battery_bank.strip("\n")))
    print(volts, end=" ")
    total_voltage += volts

file.close()

print(total_voltage)
