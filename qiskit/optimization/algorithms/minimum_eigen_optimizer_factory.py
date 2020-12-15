import numpy as np

from qiskit.aqua import AquaError
from qiskit.aqua.algorithms.minimum_eigen_solvers import (MinimumEigensolver,
                                                          NumPyMinimumEigensolver, VQE, QAOA)
from . import MinimumEigenOptimizer
from ..converters import QuadraticProgramToQubo
from ..problems import QuadraticProgram


class MinimumEigenOptimizerFactory:
    def __init__(self, mes: str = 'numpy'):
        self._mes = mes

    def get_solver(self, prob: QuadraticProgram) -> MinimumEigenOptimizer:
        mes = self._get_mes()
        return MinimumEigenOptimizer(min_eigen_solver=mes)

    def _get_mes(self) -> MinimumEigensolver:
        if self._mes == 'numpy':
            mes = self._get_numpy_mes()
        elif self._mes == 'vqe':
            mes = self._get_vqe()
        elif self._mes == 'qaoa':
            mes = self._get_qaoa()
        else:
            raise AquaError('Invalid mes name: {}. Should be "numpy", "vqe", or "qaoa".'
                            ''.format(self._mes))
        return mes

    def _get_numpy_mes(self) -> NumPyMinimumEigensolver:
        return NumPyMinimumEigensolver()

    def _get_vqe(self) -> VQE:
        return VQE()

    def _get_qaoa(self) -> QAOA:
        return QAOA()


class SpecialMinimumEigenOptimizerFactory(MinimumEigenOptimizerFactory):
    def __init__(self, penalty: float, initial_point: np.ndarray, mes: str = 'numpy'):
        super().__init__(mes)
        self._penalty = penalty
        self._initial_point = initial_point

    def get_solver(self, prob: QuadraticProgram) -> MinimumEigenOptimizer:
        mes = self._get_mes()
        converters = [QuadraticProgramToQubo(penalty=self._penalty)]
        return MinimumEigenOptimizer(min_eigen_solver=mes, converters=converters)

    def _get_vqe(self) -> VQE:
        return VQE(initial_point=self._initial_point)

    def _get_qaoa(self) -> QAOA:
        return QAOA(initial_point=self._initial_point)
