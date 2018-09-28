.. _aqua-installation:

===========================
インストールとセットアップ
===========================

Aqua は `量子アルゴリズム <#quantum-algorithms.html>`_ を実行するツールとして使われます。適切な入力で、入力された問題をモデリングする量子回路を生成、コンパイルし、量子アルゴリズムの基盤となる `Terra <https://qiskit.org/terra>`_ プラットフォーム上で実行します。 Aquaは、:ref:`aqua-chemistry`、:ref:`aqua-ai` 、:ref:`aqua-optimization` などの特定の領域固有のアプリケーションの基礎としても使用できます。 このセクションでは、ユーザーの目標にもとづいて、Aquaをインストールし設定する方法について説明します。

------------
依存関係
------------


Aquaの導入には、少なくとも、`Python の バージョン3.5 以降 <https://www.python.org/downloads/>`__ のインストールが必要です。チュートリアルを使うためには `Jupyter Notebook <https://jupyter.readthedocs.io/en/latest/install.html>`__ のインストールも推奨します。これらの理由により、すべての依存する不ライブラリーが事前にインストールされた `Anaconda 3 <https://www.continuum.io/downloads>`__　のPythonディストリビューションをインストールすることを推奨します。

.. 参考::
    Aquaは `Terra <https://qiskit.org/terra>`_ の上に構築されているので、 
    `Terra インストールとセットアップ <https://qiskit.org/documentation/install.html>`_ も参考にしてください。
    

------------
インストール
------------

Aqua をツールとして使う、または量子アルゴリズムのライブラリーとして使うのが目的の場合の、Aqua をインストールするベストな方法は、`pip <https://pip.pypa.io/en/stable/>`__ パッケージマネージメントシステムを使って、以下のようにします。


.. code:: sh

    pip install qiskit_aqua


pipはすべての依存関係を自動的に取り扱うので、常に最新の（よくテストされた）リリースバージョンがインストールされます。

別のユーザー、例えば、量子の研究者や開発者は、Aquaのソースコードの開発や新規コンポーネントが共有された:ref:`aqua-extending` （:ref:`quantum-algorithms`, :ref:`optimizers`, :ref:`variational-forms`,
:ref:`iqfts`, :ref:`oracles` and :ref:`initial-states` など）により興味があるでしょう。Aquaの可能性を拡張することが目的の場合に最適な方法は、 `Aqua repository <https://github.com/Qiskit/aqua>`__ をクローンすることです。


.. メモ::

    Qiskitと他のアプリケーションを区別し、あなたの経験を向上させるために
    `Python virtual environments <https://docs.python.org/3/tutorial/venv.html>`__ を使うことを推奨します。
    
