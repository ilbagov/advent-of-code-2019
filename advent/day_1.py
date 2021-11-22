import numpy as np
from numpy.typing import NDArray


def load_mass(file: str) -> NDArray[np.float64]:
    """
    Loads a list of masses of all modules
    """

    with open(file) as f:
        data = [int(x) for x in f.readlines() if x not in ['\n', '\rn']]

    return np.array(data, dtype=np.float64)


def fuel_eq(mass: NDArray[np.float64]) -> NDArray[np.float64]:
    """
    Implements the fuel equation from day 1 of the challenge.
    """
    fuel = np.array((np.floor(np.array(mass)/3) - 2), dtype=np.float64)

    return fuel


def fuel_eq_iterative(mass: NDArray[np.float64]) -> NDArray[np.float64]:
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