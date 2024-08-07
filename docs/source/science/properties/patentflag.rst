Patent flag
=============
Unit: [True/False] (True: found in patent database | False: not found in patent database)

Patent and article derived chemical databases are widely utilized for the evaluation of novelty.
In the case of the DiaDEM platform, our initial expectation is that literature data could have a lower relevance than patent-based data,
as many of the research articles show molecules that are not patented or a different application is demonstrated,
which does not limit the use as an organic electronic material.
The SureChEMBL [1]_ database currently contains ~17M structures, covering European, American, Japanese and world patents.

Although chirality and tautomer forms could be important factors in the working mechanisms of an active agent or a drug-like molecule,
patentability is mainly covered for the core chemical structure, and usually all stereoisomers and tautomers are covered with the same application.
Therefore, for the comparison we selected Sp2- level matching, based on generated InChIs and in case of matched we have **flagged** the relevant compounds.

.. [#] George Papadatos et al, Nucleic Acids Res. 2016 Jan 4; 44(Database issue): D1220–D1228. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4702887/
