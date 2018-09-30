========
Overview
========

----------------------------
モジュール性と拡張性
----------------------------

Aquaは、様々なレベルでモジュラーや拡張可能になるように特別に設計された量子アルゴリズムのライブラリーです。 これにより、さまざまなレベルの経験と科学的関心を持った異なるユーザーが、異なるレベルでAquaのソフトウェアスタックに貢献し、拡張することができます。

^^^^^^^^^^^^^^^^
Input Generation
^^^^^^^^^^^^^^^^

アプリケーションレベルでは、Aquaは古典的な計算ソフトウェアを量子アプリケーションのフロントエンドとして使用することができます。 このモジュールは拡張可能です；新しいソフトウェアを簡単にプラグインすることができます。Aquaでは、そのソフトウェアで古典的な初期計算を実行できます。 これらの計算の結果は問題の構成と組み合わされ、1つ以上の量子アルゴリズムの入力に変換され、`Qiskit Terra <https://Qiskit.org/terra>`__ code APIがビルド、コンパイルされ、量子回路が実行されます 。
At the application level, Aqua allows for classical computational
software to be used as the quantum application front end.  This module is extensible;
new computational software can be easily plugged in.  Behind the scenes, Aqua lets that
software perform some initial computations classically.  The  results of those computations
are then combined with the problem
configuration and translated into input for one or more quantum algorithms, which invoke
the `Qiskit Terra <https://Qiskit.org/terra>`__ code APIs to build, compile and execute quantum circuits.

^^^^^^^^^^^^^^^^^
入力の翻訳
^^^^^^^^^^^^^^^^^
問題の構成と計算ソフトウェアの古典的実行から得られる追加の中間データ（が存在する場合は）とを組み合わせて、量子システムへ入力します。 *翻訳*と呼ばれるフェーズも拡張可能です。 より効率的な翻訳オペレータを提供することに関心を持つ実験者は、Aquaソフトウェアスタックのこの層を独自の翻訳オペレータ実装で拡張することによって、そうすることができます。

The problem configuration and (if present) the additional intermediate data
obtained from the classical execution of the computational software are
combined to form the input to the quantum system.  This phase, known as *translation*,
is also extensible.  Practitioners interested in providing more efficient
translation operators may do so by extending this layer of the Aqua software
stack with their own translation operator implementation.

^^^^^^^^^^^^^^^^^^
量子アルゴリズム
^^^^^^^^^^^^^^^^^^
量子アルゴリズムの研究者や開発者は、すでにAquaに含まれているアルゴリズムを試したり、Aquaに公開されているプラグイン可能なインターフェイスを通じて独自のアルゴリズムを提供したりすることができます。 プレーンな量子アルゴリズムに加えて、Aquaは、膨大なコンポーネントをサポートし提供しています。例えば、変分形式、ローカルオプティマイザ、グローバルオプティマイザ、初期状態、量子フーリエ変換（QFT）、グロヴァー・オラクルなど、 これらのコンポーネントは、プラガブルインターフェイスを介して拡張することもできます。

Quantum algorithm researchers and developers can experiment with the algorithms already included
in Aqua, or contribute their own algorithms via the pluggable interface exposed
by Aqua.  In addition to plain quantum algorithms, Aqua offers a vast set
of supporting components, such as variational forms, local and global optimizers, initial states,
Quantum Fourier Transforms (QFTs) and Grover oracles.  These components are also extensible via pluggable
interfaces.

--------------
新機能
--------------
そのモジュール性と拡張性、複数の領域にわたる能力、古典的な計算ソフトウェアから量子ハードウェアまでの完全な完全性に加え、他の量子ソフトウェアスタックと比較して、Aquaは使いやすさ、機能性、および 構成の正しさを強化する点を実装しています。

In addition to its modularity and extensibility, ability to span across multiple
domains, and top-to-bottom completeness from classical computational software to
quantum hardware, compared to other quantum software stacks, Aqua presents numerous unique advantages
in terms of usability, functionality, and configuration-correctness enforcement.  

^^^^^^^^^^^^^^^
ユーザー・エクスペリエンス
^^^^^^^^^^^^^^^
フロントエンドで古典的な計算ソフトウェアを使用することには、それ自身の重要な利点があります。実際、Aquaソフトウェアスタックの最上位には、業界ドメイン専門家がいます。これらの専門家は、自分のドメインに固有の既存の計算ソフトウェアをよく知っています。これらの実務家は、おそらく、パフォーマンス、正確性、計算複雑性の低減という点で量子コンピューティングの利点を試すことに興味がありますが、同時に基礎となる量子インフラストラクチャーについて学ぶことを好まない可能性もあります。理想的には、そのような実務家は、新しい量子プログラミング言語や新しいAPIを習得することなく、彼らが精通している計算ソフトウェアを量子コンピューティングシステムのフロントエンドとして使用したいと考えています。また、そのような実践者が、様々な実験に対応して、時間の経過とともに、多数の問題構成を収集する可能性があります。 Aquaは、変更なしで、特定のドメインで経験を積んだ開業医が量子プログラミング言語を習得する必要なく、これらの設定ファイルを受け入れるように設計されています。このアプローチは、ユーザビリティの点で明らかな利点があります。

Allowing classical computational software at the frontend has its own important advantages.
In fact, at the top of the Aqua software stack are industry-domain experts, who are most likely
very familiar with existing computational software specific to their own domains.  These practitioners are probably interested in experimenting with the benefits of quantum computing in terms of performance, accuracy
and reduction of computational complexity, but at the same time they might be
unwilling to learn about the underlying quantum infrastructure. Ideally,
such practitioners would like to use the computational software they are
familiar with as a front end to the quantum computing system,
without having to learn a new quantum programming
language or new APIs.  It is also
likely that such practitioners may have collected, over time, numerous
problem configurations, corresponding to various experiments. Aqua has been designed to accept those
configuration files  with no modifications, and
without requiring a practitioner experienced in a particular domain to
have to learn a quantum programming language. This approach has a clear advantage in terms
of usability.

^^^^^^^^^^^^^
機能性　
^^^^^^^^^^^^^
Aquaが量子プログラミング言語や新しいAPIをユーザーと古典的計算ソフトウェアの間に挿入するように設計されていた場合、それらの機能が上位レベルに公開されていない限り、基礎となる古典計算ソフトウェアのすべての機能を完全に活用することはできません。プログラミング言語またはAPIレベル言い換えれば、量子入力を形成するために必要な中間データの最も正確な計算にインタフェースされた計算ソフトウェアの古典的実行を駆動するために、そのソフトウェアの高度な機能はAquaを通じて構成可能でなければなりませんでした。 Aquaが古典的な計算ソフトウェアを受け入れることができる拡張可能なインターフェースを持つことを考えれば、量子特有のプログラミング言語やAPIのインプットは、ユーザビリティの障害であるだけでなく、機能制限要因でもありました。 Aquaが古典的計算ソフトウェアと直接的にインタフェースする能力により、そのソフトウェアは量子入力を最高精度で形成するのに必要な中間データを計算することができます。

If Aqua had been designed to interpose a quantum programming language
or new APIs between the user and the classical computational software, it would not have been able to
fully exploit all the features of the underlying classical computational software unless those features
had been exposed at the higher programming-language or API level.  In other words, in order to drive
the classical execution of any interfaced computational software to the most
precise computation of the intermediate data needed to form
the quantum input, the advanced features of that software would have had to be configurable
through Aqua.
Given the intention for Aqua to have an extensible interface capable of accepting
any classical computational
software, the insertion of a quantum-specific programming language or API would have
been not only a usability
obstacle, but also a functionality-limiting factor.
The ability of Aqua to directly interface classical computational software allows that software
to compute the intermediate data needed to form the quantum input at its highest level of precision.

^^^^^^^^^^^^^^^^^^^^^^^^^
構成の正しさ
^^^^^^^^^^^^^^^^^^^^^^^^^
Aquaにはもう一つのユニークな機能があります。 Aquaが従来のソフトウェアを量子システム上で実行できるようにすると、特定の業界ドメインで実験を構成するには、値を互いに分離して割り当てることができないドメイン特有の構成パラメータと量子固有の構成パラメータの両方を含むハイブリッド構成が必要になることがあります。 特定のドメインに精通しているものの、量子コンピューティングの領域では初めての人にとっては、構成エラーを導入したり、誤植を付けたり、互換性のない構成パラメータを選択する可能性は非常に高いです。 このような問題に対処するために、Aquaでは、問題特有および量子固有の構成データの正しさを動的に検証し、古典入力と量子入力の組み合わせが構成エラーに耐えられるようにします。 非常に重要なのは、構成の正確さは、動的に検出されてロードされるコンポーネントであっても動的に適用されることです。

Aqua offers another unique feature. Given that Aqua
allows traditional software to be executed on a quantum system,
configuring an experiment in a particular domain may require a hybrid
configuration that involves both domain- and quantum-specific
configuration parameters whose values cannot be assigned in isolation from each other.
The chances of introducing configuration
errors, making typos, or selecting incompatible configuration parameters
are very high, especially for people who are expert in a given domain
but new to the realm of quantum computing. To address such issues, in
Aqua the problem-specific and
quantum-specific configuration data is dynamically verified for
correctness so that the combination of classical and quantum inputs is
resilient to configuration errors. Very importantly, configuration
correctness is dynamically enforced even for components that are
dynamically discovered and loaded.


.. include:: ../CONTRIBUTORS.RST

-------
ライセンス
-------

This project uses the `Apache License Version 2.0 software
license <https://www.apache.org/licenses/LICENSE-2.0>`__.
