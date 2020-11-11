import numpy as np

######################################################### DAY 1
def load_mass(file):
    """
    Loads a list of masses of all modules
    """

    with open(file) as f:
        data = [int(x) for x in f.readlines() if x not in ['\n', '\rn']]

    return data


def fuel_eq(mass):
    """
    Implements the fuel equation from day 1 of the challenge.
    """

    return np.floor(np.array(mass)/3) - 2


def fuel_eq_iterative(mass):
    """
    Adds iterations to the original fuel equation so that the mass of the fuel itself is taken into account.
    """

    fuel = np.zeros(np.array(mass).shape)
    new_fuel = np.array(mass).copy()

    while True:
        new_fuel = fuel_eq(new_fuel)
        new_fuel[new_fuel <= 0] = 0
        fuel += new_fuel

        if (new_fuel == np.zeros(new_fuel.shape)).all():
            break

    return fuel


######################################################### DAY 2
def load_intcode(path):
    """
    Loads the Intocode entries from day 2 into a list
    """
    with open(path) as f:
        data = [int(x) for x in f.readline().split(',')]

    return data


def run_intcode(code):
    """
    Reads an Intcode sequence according to the specifications of day 2
    """

    # split the code into 4-numbers-long  chunks for easier manipulation
    chunks = [code[i:i+4] for i in range(0, len(code), 4)]

    for c in chunks:
        # check if opcode is valid
        if c[0] not in [1, 2]:
            break

        # extracting the opcode, the positions of the operands, and the storage position
        opcode = c[0]
        pos_op_1, pos_op_2, pos_store = c[1:]

        # running the needed operation
        if opcode == 1:
            code[pos_store] = code[pos_op_1] + code[pos_op_2]
        elif opcode == 2:
            code[pos_store] = code[pos_op_1] * code[pos_op_2]

    return code

