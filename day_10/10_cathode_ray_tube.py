cycle = 0
draw_cycle = 0
register = 1
result = 0

cycle_list = [20, 60, 100, 140, 180, 220]
crt_screen = []


def checkCycle():
    global result

    if cycle in cycle_list:
        result += cycle * register
        cycle_list.remove(cycle)


def draw():
    global draw_cycle

    if abs(register - draw_cycle) <= 1:
        crt_screen.append("#")
    else:
        crt_screen.append(".")

    if draw_cycle >= 39:
        draw_cycle = 0
    else:
        draw_cycle += 1


file = open("input.txt").read().split("\n")
for line in file:
    checkCycle()
    if line.startswith("noop"):
        draw()
        cycle += 1
    else:
        draw()
        cycle += 1
        checkCycle()
        draw()
        cycle += 1
        checkCycle()
        register += int(line.split(" ")[-1])


print(f"Part 1 Solution: {result}")

print(f"Part 2 Solution:")
for i in range(0, len(crt_screen), 40):
    print(" ".join(crt_screen[i:i + 40]))
