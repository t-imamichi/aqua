import numpy as np

from qiskit.aqua import AquaError
from qiskit.aqua.algorithms.minimum_eigen_solvers import (MinimumEigensolver,
                                                          NumPyMinimumEigensolver, VQE, QAOA)
from qiskit.circuit.library import EfficientSU2
from . import MinimumEigenOptimizer
from ..converters import QuadraticProgramToQubo
from ..problems import QuadraticProgram


class MinimumEigenOptimizerFactory:
    def __init__(self, mes: str = 'numpy'):
        self._mes = mes

    def get_solver(self, prob: QuadraticProgram) -> MinimumEigenOptimizer:
        mes = self._get_mes(prob)
        return MinimumEigenOptimizer(min_eigen_solver=mes)

    def _get_mes(self, prob: QuadraticProgram) -> MinimumEigensolver:
        if self._mes == 'numpy':
            mes = self._get_numpy_mes(prob)
        elif self._mes == 'vqe':
            mes = self._get_vqe(prob)
        elif self._mes == 'qaoa':
            mes = self._get_qaoa(prob)
        else:
            raise AquaError('Invalid mes name: {}. Should be "numpy", "vqe", or "qaoa".'
                            ''.format(self._mes))
        return mes

    def _get_numpy_mes(self, prob: QuadraticProgram) -> NumPyMinimumEigensolver:
        return NumPyMinimumEigensolver()

    def _get_vqe(self, prob: QuadraticProgram) -> VQE:
        return VQE()

    def _get_qaoa(self, prob: QuadraticProgram) -> QAOA:
        return QAOA()


class SampleMEOFactory(MinimumEigenOptimizerFactory):
    def __init__(self, penalty: float, initial_point: np.ndarray, mes: str = 'numpy'):
        super().__init__(mes)
        self._penalty = penalty
        self._initial_point = initial_point

    def get_solver(self, prob: QuadraticProgram) -> MinimumEigenOptimizer:
        mes = self._get_mes(prob)
        # generate a custom list of converters
        converters = [QuadraticProgramToQubo(penalty=self._penalty)]
        return MinimumEigenOptimizer(min_eigen_solver=mes, converters=converters)

    def _get_vqe(self, prob: QuadraticProgram) -> VQE:
        # generate a custom varform
        var_form = EfficientSU2(reps=1)
        return VQE(initial_point=self._initial_point, var_form=var_form)

    def _get_qaoa(self, prob: QuadraticProgram) -> QAOA:
        # customize the p-value
        p = 2
        return QAOA(p=p, initial_point=self._initial_point)
