# -*- coding: utf-8 -*-

# Copyright 2018 IBM.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

import unittest
import operator

from parameterized import parameterized
from qiskit_aqua import get_aer_backend

from test.common import QiskitAquaTestCase
from qiskit_aqua.components.oracles import SAT
from qiskit_aqua.algorithms import Grover
from qiskit_aqua import QuantumInstance


class TestGrover(QiskitAquaTestCase):

    @parameterized.expand([
        ['test_grover_tiny.cnf', False, 1, 'basic'],
        ['test_grover_tiny.cnf', False, 1, 'advanced'],
        ['test_grover.cnf', False, 2, 'basic'],
        ['test_grover.cnf', False, 2, 'advanced'],
        ['test_grover_no_solution.cnf', True, 1, 'basic'],
        ['test_grover_no_solution.cnf', True, 1, 'advanced'],
    ])
    def test_grover(self, input_file, incremental=True, num_iterations=1, cnx_mode='basic'):
        input_file = self._get_resource_path(input_file)
        # get ground-truth
        with open(input_file) as f:
            buf = f.read()
        if incremental:
            self.log.debug('Testing incremental Grover search on SAT problem instance: \n{}'.format(
                buf,
            ))
        else:
            self.log.debug('Testing Grover search with {} iteration(s) on SAT problem instance: \n{}'.format(
                num_iterations, buf,
            ))
        header = buf.split('\n')[0]
        self.assertGreaterEqual(header.find('solution'), 0, 'Ground-truth info missing.')
        self.groundtruth = [
            ''.join([
                '1' if i > 0 else '0'
                for i in sorted([int(v) for v in s.strip().split() if v != '0'], key=abs)
            ])[::-1]
            for s in header.split('solutions:' if header.find('solutions:') >= 0 else 'solution:')[-1].split(',')
        ]
        backend = get_aer_backend('qasm_simulator')
        sat_oracle = SAT(buf)
        grover = Grover(sat_oracle, num_iterations=num_iterations, incremental=incremental, cnx_mode=cnx_mode)
        quantum_instance = QuantumInstance(backend, shots=100)

        ret = grover.run(quantum_instance)

        self.log.debug('Ground-truth Solutions: {}.'.format(self.groundtruth))
        self.log.debug('Measurement result:     {}.'.format(ret['measurements']))
        top_measurement = max(ret['measurements'].items(), key=operator.itemgetter(1))[0]
        self.log.debug('Top measurement:        {}.'.format(top_measurement))
        if ret['oracle_evaluation']:
            self.assertIn(top_measurement, self.groundtruth)
            self.log.debug('Search Result:          {}.'.format(ret['result']))
        else:
            self.assertEqual(self.groundtruth, [''])
            self.log.debug('Nothing found.')


if __name__ == '__main__':
    unittest.main()
