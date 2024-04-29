.. _science_calculators:

Calculators
============

We refer to implementations of specific scientific methods as *calculators*. E.g., DFT-Single-Point as implemented in PySCF version X with a def2-SVP basis set and B3LYP functional would be one calculator, whereas the same computation with the BP functional would be considered a different calculator. Each calculator may have different versions, e.g. to track changes in the underlying implementation.
A specific molecular property may therefore be provided by multiple calculators of the DiaDEM platform. On the other hand, a single calculator may provide multiple properties, such as HOMO, LUMO, and excitation energy, as all properties are computed when the calculator is executed on a specific compound.

As the accuracy of computed properties is strongly method dependent, the choice of the calculator is crucial both when searching for compounds with a specific property in the database and when computing additional properties on-demand.
To identify the calculator most suitable for your purpose, this section provides details of each calculator. The :ref:`properties section <science_properties>` gives additional recommendations and benchmarks.




.. toctree::
   :maxdepth: 2

   calib_TDDFT

