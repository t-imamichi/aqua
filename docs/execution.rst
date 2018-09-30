.. _aqua-execution:

=====================================
設定と実験の実行
=====================================

Aquaは2つのタイプのユーザーをサポートします： 

1. *実践者*：単にアクアを実行するツールとして、ref： `quantum-algorithms`を実行することに興味があります。 これらのユーザーは、追加の機能でAquaを拡張することに関心がないかもしれません。 実際、彼らは、回路、ゲート、量子ビットといった概念のような量子コンピューティングの詳細を学ぶことにも興味がないかもしれません。 これらのユーザが量子コンピューティングに期待するのは、古典的なアルゴリズムの使用と比較して、性能と精度の向上、計算の複雑さの低減です。 Aquaはまた、参照値を生成し、実験中の結果を比較して対比するための：ref： `古典的参照アルゴリズム 'のライブラリを提供しています。
2. *量子アルゴリズムの研究者および開発者*：より効率的かつ正確な計算のために、新しい量子アルゴリズムまたはアルゴリズムコンポーネントでAquaを拡張することに関心のある。

1. *Practitioners*, who are merely interested in executing Aqua
   as a tool to execute :ref:`quantum-algorithms`.
   These users may not be interested in extending Aqua
   with additional capabilities.  In fact, they may not even be interested
   in learning the details of quantum computing, such as the notions of
   circuits, gates and qubits.  What these users expect
   from quantum computing is the gains in performance and accuracy, and
   the reduction in computational complexity, compared to the use of
   a classical algorithm.  Aqua also provides a library of :ref:`classical-reference-algorithms`
   for generating reference values and comparing and contrasting results during
   experimentation.
2. *Quantum algorithm researchers and developers*, who are interested in extending
   Aqua with new quantum algorithms or algorithm components for more efficient
   and accurate computations.

このセクションでは、アルゴリズムの実践者である第1クラスのユーザーについて説明します。 具体的には、このセクションでは、量子アルゴリズムの実行を実験するためのツールとしてAquaにアクセスする方法について説明します。

新しいコンポーネントでAquaを拡張する方法を知るには、 `section：ref：` aqua-extending`を参照してください。

In this section, we cover the first class of users --- the algorithm practitioners.
Specifically, this section describes how Aqua can be accessed as a
tool for experimenting with the execution of quantum algorithms.

To see how you can extend Aqua with new components,
please refer to `Section ":ref:`aqua-extending`".

---------------
実行モード
---------------
Aquaには、 `グラフィカルユーザーインターフェイス（GUI）<＃aqua-gui>`_ と `コマンドラインツール<＃aqua-command-line>`_ があります。 これらは、量子アルゴリズムを試すときに使用できます。 両方とも、実験の問題の種類と計算に使用される量子アルゴリズムとアルゴリズムの構成やその他のさまざまなオプションを指定した `input file <＃aqua-input-file>`_ をロードして実行できます。実験をカスタマイズする Aquaを初めてお使いの方は、GUIを使い始めることを強くお勧めします。 Aquaは、コマンドラインとGUIが提供できるものを越えて実験をカスタマイズすることに関心を持つユーザーによって、 `プログラム可能<＃aqua-programmable-interface>`_ にアクセスすることもできます。 最後に、Aqua実験を構成するユーザと新しいコンポーネントでAquaを拡張する研究者は、：ref： `aqua-doc-ui`にアクセスして、様々なコンポーネントとその設定パラメータを素早く調べることができます。

Aqua has both a `Graphical User Interface (GUI) <#aqua-gui>`__ and a `command
line tool <#aqua-command-line>`__.  These can be used when experimenting with quantum algorithms.
Both can load and run an `input
file <#aqua-input-file>`__ specifying the the type of problem the experiment is about,
and the quantum
algorithm to be used for the computation, along with the algorithm configuration
and various other options to
customize the experiment.  If you are new to
Aqua, we highly recommend getting started with the GUI.
Aqua can also be accessed
`programmatically <#aqua-programmable-interface>`__ by users interested
in customizing the experiments beyond what the command line and GUI can offer.
Finally, users configuring an Aqua experiment and researchers
intersted in extending Aqua with new components can access
the :ref:`aqua-doc-ui` for quickly inspecting the various components
and their configuration parameters.

.. _aqua-gui:

^^^
GUI
^^^
GUIは、ゼロから作成するか、既存の `入力ファイル<＃aqua-input-file> `_ を読み込み、その入力ファイルを実行して量子アルゴリズムを試す簡単な手段を提供します。 Aquaの入力ファイルはJSON形式であるとみなされます。 このファイルは、パラメータ値のスキーマベースで検証し作成、編集、保存されます。

インストール時
`` pip install``コマンドでAquaを起動すると、次のようにコマンドラインからGUIを起動できるスクリプトが作成されます：

.. code:: sh

   qiskit_aqua_ui

`` pip install``を使わずに `GitHubリポジトリ<https://github.com/Qiskit/aqua>`_ からAquaを直接クローンした場合、上記のスクリプトは存在せず、起動コマンドが代わりになるはずです ：

.. code:: sh

   python qiskit_aqua/ui/run

このコマンドは、 `` qiskit-aqua``リポジトリクローンのルートフォルダから起動する必要があります。

.. seealso::

   詳細は：ref： `aqua-installation`のドキュメントを参照してください。

.. _aqua-command-line:

^^^^^^^^^^^^
コマンドライン
^^^^^^^^^^^^

If installed via ``pip install``,
Aqua comes with the following command-line tool:

.. code:: sh

   qiskit_aqua_cmd

If you cloned Aqua from its remote
`GitHub repository <https://github.com/QISKit/aqua>`__
instead of using ``pip install``, then the command-line interface can be executed as follows:

.. code:: sh

   python qiskit_aqua

from the root folder of the ``qiskit-aqua`` repository clone.

.. seealso::

    Consult the documentation on the :ref:`aqua-installation` for more details.

When invoking Aqua from the command line, an `input file <#aqua-input-file>`__ in
`JavaScript Object Notation (JSON) <https://www.json.org/>`__ format
is expected as a command-line parameter.

.. _aqua-programmable-interface:

^^^^^^^^^^^^^^^^^^^^^^
プログラマブルインターフェイス
^^^^^^^^^^^^^^^^^^^^^^

Experiments can be run programmatically too. Numerous examples on how to program an experiment in Aqua
can be found in the ``aqua`` folder of the `Aqua Tutorials GitHub repository <https://github.com/QISKit/aqua-tutorials>`__.

It should be noted at this point that Aqua is designed to be as much declarative as possible.  This is done in order
to simplify the programmatic access to Aqua, minimize the chances for configuration errors, and help users who might not interested in writing a lot of code or learning new Application Programming Interfaces (APIs).

There is nothing preventing a user from accessing the Aqua APIs and programming an experiment step by step, but a  more direct way to access Aqua programmatically is by obtaining a JSON algorithm input file, such as one of those
available in the ``aqua/input_files`` subfolder of the `Aqua Tutorials GitHub repository <https://github.com/QISKit/aqua-tutorials>`__. Such files can be constructed manually, but a much more intuitive way to automatically
construct one of these input files is via Aqua domain-specific applications.  For example, the :ref:`aqua-chemistry-command-line` and :ref:`aqua-chemistry-gui` have options to serialize the input to the quantum algorithm for future reuse. The JSON file can then be pasted into a Python program and modified according to the needs of the developer, before invoking the ``run_algorithm`` API in ``qiskit_aqua``. This technique can be used, for example, to compare the results of two different algorithms.

.. _aqua-doc-ui:

^^^^^^^^^^^^^^^^
ドキュメントUI
^^^^^^^^^^^^^^^^
Aquaはモジュール化された拡張可能なソフトウェアフレームワークで、実験を実行するためのツールとしてAquaを使いたい人や、新しいコンポーネントでAquaを拡張することに関心を持つ人など、2種類のエンドユーザをサポートしています。 これらのカテゴリのいずれかのユーザーは、プラグイン可能なすべてのコンポーネントとそのパラメータのスキーマを示すAquaドキュメントUIにアクセスすると便利です。

`` pip install``を介してインストールされた場合、
Aquaには、AquaドキュメントUIを起動するための次のコマンドラインツールが付属しています。

.. code:: sh

   qiskit_aqua_browser

`` pip install``を使う代わりに、リモート `GitHubリポジトリ<https://github.com/QISKit/aqua>` __からAquaをクローンした場合、
AquaのドキュメントUIは、次のように起動できます。...

.. code:: sh

   python qiskit_aqua/ui/browser

`` qiskit-aqua``リポジトリクローンのルートフォルダから

.. _aqua-input-file:

----------
入力ファイル
----------
入力ファイルは、Aqua問題を定義するために使用され、量子アルゴリズムへの入力と、基礎となる量子システムの構成情報を含みます。 与えられていない場合には、デフォルト値を使用するのではなく、計算に使用される処理および量子アルゴリズムを明示的に制御するために、特定の構成パラメータ値が供給されます。

入力ファイルのフォーマットは `JavaScript Object Notation（JSON）<https://www.json.org/>`__ です。 これにより、スキーマベースの構成入力の正確性の検証が可能になります。 Aquaでは、手動でJSON入力ファイルを生成することは可能ですが、ドメイン固有のアプリケーションの実行からこのようなJSON入力ファイルを自動的に生成することができます。

例えば、Aqua Chemistryのコマンドラインツール：ref： `aqua-chemistry-command-line`と：ref：` aqua-chemistry-gui`は、両方ともJSONファイル：ref ： `input-file-for-direct-algorithm-invocation` として、量子アルゴリズムへの入力を自動的にシリアル化します。 量子アルゴリズムへの入力をシリアライズすることは、そのようなJSONファイルの内容がドメインと問題に依存しないため、多くのシナリオで役に立ちます。

- Users can share JSON files among each other in order to compare and contrast their experimental results at the algorithm level, for example to compare results obtained by passing the same input to different algorithms, or to different implementations of the same algorithm, regardless of the domain in which those inputs were generated (chemistry, artificial intelligence, optimization, etc. or the problem that the user was trying to solve.
- People performing research on quantum algorithms may be interested in having
  access to a number of such JSON files in order to test and refine the design and
  implementation of an algorithm, irrespective of the domain in which those JSON files were generated
  or the problem that the user was trying to solve.
- Repeating a domain-specific experiment in which the values of the input parameters remain the same,
  and the only difference is in the configuration of the quantum algorithm and its
  supporting components becomes much more efficient because the user can choose to
  restart any new experiment directly at the algorithm level, thereby bypassing the
  data extraction from the driver, and the translation of that data into input to a
  quantum algorithm.

A number of sample JSON input files for Aqua are available in the
``aqua/input_files``
subfolder of the `Aqua Tutorials GitHub repository <https://github.com/QISKit/aqua-tutorials>`__.

An input file comprises the following main sections, although not all
mandatory:

^^^^^^^^^^^^^
``"問題"``
^^^^^^^^^^^^^
Aquaでは、* problem *は実行されている実験のタイプを指定します。 問題の構成は、特定の実験に適したアルゴリズムを決定するため不可欠です。 Aquaには、あらかじめ定義された問題があります。 このセットは拡張可能です。既存の問題を別の方法で解決するために新しいアルゴリズムをプラグインできるように、新しい問題を追加することも、新しい問題を解決することもできます。

現在、 `` name ""パラメータに `` str``の値を代入することで問題を設定できます：

.. code:: python

    "name" = "energy" | "excited_states" | "ising" | "dynamics" | "search" | "svm_classification"

上で示したように、 "エネルギー" "、" "興奮状態 "、 "イジング "、 ""力学 ""、"探索"および""svm_分類""が現在のところ、"name"で受け入れられている値です。 *エネルギー*、*励起状態*、*イジングモデル*、*進化のダイナミクス*、*検索*、*サポートベクターマシン（SVM）分類*の計算に対応しています。新しい問題は、"name"パラメーターに明確化され、``AlgorithmInput`` Application Programming Interface (API)　を介してAquaにプログラマティカリーに追加され、それぞれの量子または古典的なAquaアルゴリズムは、``QuantumAlgorithm`` インターフェースでインプリされたクラスとしてJSONスキームで、問題をリストアップする必要があります。

計算の際には、乱数の使用を含むことができます。 例えば、VQEで、変分法が初期状態に基づいて優先事項を供給しない場合、およびユーザが明示的に初期ポイントを供給しない場合、ランダム初期ポイントを使用するようにコード化されます。 この場合、VQEの各実行は、それ以外の場合には一定の問題となる可能性があるため、異なる結果を生み出す可能性があり、非決定論を引き起こし、同一の構成で異なる実行間で同じ結果を複製することができません。 VQEを複数回実行した後に得られる最終的な値は数値的に区別できない場合がありますが、評価の数は実行ごとに異なる場合があります。 反復可能な実験を可能にするために、全く同じ結果でランダムなシードを設定することで、実験が実行されるたびに同じ疑似乱数が強制的に生成されます。


.. code:: python

    "random_seed" : int

このパラメータのデフォルト値は `` None``です。

^^^^^^^^^^^
``"入力"``
^^^^^^^^^^^
このセクションでは、ユーザーがAquaアルゴリズムへの入力を指定できます。そのような入力は、タイプエネルギー、励起状態、イジングモデルおよび進化のダイナミクスの問題に対する「qubit_op」パラメータの値として表されるキュビット演算子であると予想されます。 SVM分類の問題については、入力はトレーニングデータセット（各ラベルをデータポイントのリストにリンクするマップ）、テストデータセット（各ラベルをデータポイントのリストにリンクするマップ）、および分類を適用するデータポイント。これらは、それぞれ、「training_datasets」、「test_datasets」、および「datapoints」のパラメータの値として指定されます。 "input"セクションはタイプ検索の問題では無効です。そのような問題の場合、入力仕様は、Quantum Grover Searchアルゴリズムで選択された特定のオラクルに依存します。現在、Aquaは、「cnf」パラメータの値として表されるDIMACS CNF形式のSAT問題を入力として受け取り、対応する量子回路を構築する充足可能性（SAT）オラクルの実装を提供しています。

^^^^^^^^^^^^^^^
``"アルゴリズム"``
^^^^^^^^^^^^^^^
これはオプションのセクションで、ユーザーはどの量子アルゴリズムを実験に使用するかを指定できます。参照値を計算するために、Aquaは古典参照アルゴリズムのライブラリも提供しています。 「アルゴリズム」セクションでは、各アルゴリズムがAqua QuantumAlgorithm APIに従って提供する必要があるJSONスキーマに基づいて、Aquaが認識する宣言的な名前を使用してアルゴリズムの曖昧さを解消します。宣言的な名前は、「アルゴリズム」セクションの「名前」パラメータとして指定されます。 "name"パラメータのデフォルト値は "VQE"で、Variant Quantum Eigensolver（VQE）アルゴリズムに対応しています。

通常、アルゴリズムには一連の構成パラメータが付属しています。それぞれについて、Aqua QuantumAlgorithm APIに従ってデフォルト値が提供されます。

さらに、各アルゴリズムに従って、追加のセクションは、そのアルゴリズムの構成要素を任意に構成するのに関連し得る。たとえば、VQEなどの変分アルゴリズムを使用すると、オプティマイザとバリアントフォームのライブラリからオプティマイザとバリアントフォームを選択して構成することができます。量子位相推定（QPE）は、逆量子化フーリエ変換Quantum Grover Searchには、Oraclesライブラリからオラクルを指定するオプションが付属しています。量子アルゴリズムに関するAquaのドキュメントでは、各アルゴリズムとそれが使用する可能性のあるプラガブルエンティティの設定方法について説明しています。

制限付きメモリBroyden-Fletcher-Goldfarb-Shanno Bound（L-BFGS-B）オプティマイザおよびRyRz変種フォームとともにアルゴリズムVQEが選択される例を以下に示します。

Here is an example in which the algorithm VQE is selected along with the
:ref:`L-BFGS-B`
optimizer and the :ref:`ryrz` variational form:

.. code:: json

    "algorithm": {
        "initial_point": null,
        "name": "VQE",
        "operator_mode": "matrix"
    },

    "optimizer": {
        "factr": 10,
        "iprint": -1,
        "maxfun": 1000,
        "name": "L_BFGS_B"
    },

    "variational_form": {
        "depth": 3,
        "entanglement": "full",
        "entangler_map": null,
        "name": "RYRZ"
    }

^^^^^^^^^^^^^
``"バックエンド"``
^^^^^^^^^^^^^
Aquaでは、量子実験が実行される量子コンピュータであるバックエンドを構成することができます。 この構成では、計算に使用するQiskit Terra量子計算バックエンドを指定する必要があります。これは、str値を「バックエンド」セクションの「name」パラメーターに割り当てることによって行われます。

.. code:: python

    "name" : string

「名前」パラメータの値は、実際のハードウェアの量子コンピュータまたは量子シミュレータのいずれかを示します。 Terraには、ローカル・ステート・ベクタ・シミュレータとローカルQASMシミュレータの2つの定義済み量子デバイス・シミュレータが付属しています。「name」パラメータの「local_statevector_simulator」（「name」パラメータのデフォルト値）と "local_qasm_simulator"と呼ばれます。 しかし、実際の量子ハードウェアデバイスを含めて、任意の適切な量子バックエンドを選択することができる。 QISKitがリモートデバイスにアクセスするためにQConfig.pyファイルを設定する必要があります。 このためには、Terraのインストール手順に従うだけで十分です。 Aqua GUI <＃aqua-gui>は、Preferences ...メニュー項目からアクセスできる使いやすいインターフェイスを使用して、QConfig.pyの設定を大幅に簡素化します。

The value of the ``"name"`` parameter indicates either a real-hardware
quantum computer or a quantum simulator.
Terra comes
with two predefined quantum device simulators: the *local state vector simulator* and
the *local QASM simulator*, corresponding to the following two
values for the ``"name"`` parameter: ``"local_statevector_simulator"`` (which
is the default value for the ``"name"`` parameter) and ``"local_qasm_simulator"``, respectively.
However, any suitable quantum backend can be selected, including
a real quantum hardware device. The ``QConfig.py`` file
needs to be setup for QISKit to access remote devices.  For this, it is sufficient to follow the
`Terra installation instructions <https://qiskit.org/documentation/install.html#installation>`__.
The Aqua `GUI <#aqua-gui>` greatly simplifies the
configuration of ``QConfig.py`` via a user friendly interface,
accessible through the **Preferences...** menu item.

.. topic:: Backend Configuration: Quantum vs. Classical Algorithms

    Although Aqua is mostly a library of
    :ref:`quantum-algorithms`,
    it also includes a number of
    :ref:`classical-reference-algorithms`
    which can be selected to generate reference values
    and compare and contrast results in quantum research experimentation.
    Since a classical algorithm runs on a classical computer,
    no backend should be configured when a classical algorithm
    is selected in the ``"algorithm"`` section.
    Accordingly, the Aqua `GUI <#aqua-gui>`__ will automatically
    disable the ``"backend"`` configuration section
    whenever a non-quantum algorithm is selected. 

Configuring the backend to use by a quantum algorithm
requires setting the following parameters too:

-  The number of repetitions of each circuit to be used for sampling:

   .. code:: python

        "shots" : int

   This parameter applies, in particular to the local QASM simulator and any real quantum device.
   The default value is ``1024``. 
   
-  A ``bool`` value indicating whether or not the circuit should undergo optimization:

   .. code:: python
       
        "skip_transpiler" : bool

   The default value is ``False``.  If ``"skip_transpiler"`` is set to ``True``, then
   QISKit will not perform circuit translation. If Aqua has been configured
   to run an experiment with a quantum algorithm that uses only basis gates,
   then no translation of the circuit into basis gates is required.
   Only in such cases is it safe to skip circuit translation.
   Skipping the translation phase when only basis gates are used may improve overall performance,
   especially when many circuits are used repeatedly, as it is the case with the VQE algorithm.

   .. warning::

       Use caution when setting ``"skip_transpiler"`` to ``True``
       as if the quantum algorithm does not restrict itself to the set of basis
       gates supported by the backend, then the circuit will fail to run.

-  An optional dictionary can be supplied to control the backend's noise model:

   .. code:: python

       "noise_params" : dictionary

   This is a Python dictionary consisting of key/value pairs.  Configuring it is optional; the default
   value is ``None``.  The following is an example of such a dictionary that can be used:

   .. code:: python

      "noise_params": {"U": {"p_depol": 0.001,
                             "p_pauli": [0, 0, 0.01],
                             "gate_time": 1,
                             "U_error": [ [[1, 0], [0, 0]]
                                        ]
                            }
                      }

   .. seealso::
       The `Terra documentation on noise parameters
       <https://github.com/Qiskit/qiskit-terra/tree/master/src/qasm-simulator-cpp#noise-parameters>`__
       provides more details on the configuration of the noise model for the backend.
