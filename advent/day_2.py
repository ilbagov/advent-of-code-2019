from typing import Tuple
import numpy as np
from numpy.typing import NDArray


def load_intcode(path: str) -> NDArray[np.int_]:
    """
    Loads the Intocode entries from day 2 into a list
    """
    with open(path) as f:
        data = [int(x) for x in f.readline().split(',')]

    return np.array(data, dtype=np.int_)


def run_intcode(code: NDArray[np.int_]) -> NDArray[np.int_]:
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
