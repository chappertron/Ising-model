from typing import Tuple
import numpy as np


class IsingLattice:
    E = 0.0
    E2 = 0.0
    M = 0.0
    M2 = 0.0

    n_cycles = 0

    def __init__(self, n_rows, n_cols):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.lattice = np.random.choice([-1, 1], size=(n_rows, n_cols))

    def energy(self) -> float:
        "Return the total energy of the current lattice configuration."
        energy = 0.0
        return energy

    def magnetisation(self) -> float:
        "Return the total magnetisation of the current lattice configuration."
        magnetisation = 0.0
        return magnetisation

    def montecarlostep(self, temp: float) -> Tuple[float, float]:
        # complete this function so that it performs a single Monte Carlo step
        energy = self.energy()
        # the following two lines will select the coordinates of the random spin for you
        random_i = np.random.choice(range(0, self.n_rows))
        random_j = np.random.choice(range(0, self.n_cols))
        # the following line will choose a random number in the rang e[0,1) for you
        random_number = np.random.random()
        ...

    def statistics(self) -> Tuple[int, float, float, float, float]:
        # complete this function so that it calculates the correct values for the averages of E, E*E (E2), M, M*M (M2), and returns them with Nsteps
        ...
