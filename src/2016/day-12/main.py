"""
--- Day 12: Leonardo's Monorail
"""

from aocd import get_data

data = get_data(day=12, year=2016).splitlines()


def run(regs):
    inst = 0
    while inst < len(data):
        cmd = data[inst].split(" ")

        if cmd[0] == "cpy":
            if cmd[1] in regs.keys():
                regs[cmd[2]] = regs[cmd[1]]
            else:
                regs[cmd[2]] = int(cmd[1])
            inst += 1

        elif cmd[0] == "inc":
            regs[cmd[1]] += 1
            inst += 1

        elif cmd[0] == "dec":
            regs[cmd[1]] -= 1
            inst += 1

        else:
            if cmd[1] in regs.keys():
                if regs[cmd[1]] != 0:
                    inst += int(cmd[2])
                else:
                    inst += 1
            else:
                if int(cmd[1]) != 0:
                    inst += int(cmd[2])
                else:
                    inst += 1
    return regs["a"]


regs = {x: 0 for x in "abcd"}
print("ONE:", run(regs))

regs = {x: 0 for x in "abcd"}
regs["c"] = 1
print("TWO:", run(regs))
