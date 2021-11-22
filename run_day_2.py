from numpy import intc
from numpy.lib.npyio import load
from advent.day_2 import load_intcode, run_intcode

intcode = load_intcode("data/day_2/data.txt")
intcode[1] = 12
intcode[2] = 2
print(run_intcode(intcode)[0])

intcode = load_intcode("data/day_2/data.txt")
for noun in range(0,100):
    for verb in range(0,100):
        intcode_copy = intcode.copy()
        intcode_copy[1] = noun
        intcode_copy[2] = verb
        output = run_intcode(intcode_copy)[0]
        if output == 19690720:
            print(100*noun + verb)
            break
