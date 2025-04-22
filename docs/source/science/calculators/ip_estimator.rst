.. _science_calculators_ip_estimator:

IP/EA Calculator
================

.. list-table::
   :header-rows: 1
   :align: center

   * - Properties
     - Notes
   * - :ref:`science_properties_ipea_estimator`
     - recommended


Workflow
--------




.. list-table:: IP/EA es Workflow Overview
   :widths: 30 30 30
   :header-rows: 1

   * - **Nanomatch Software**
     - **Scientific Role**
     - **Illustration**
   * - `Parametrizer <http://docs.nanomatch.de/nanomatch-modules/Parametrizer/Parametrizer.html>`_
     - | Ground State
       | Geometry optimization
     - .. image:: mobility/parametrizer.png
          :width: 150px
          :align: center
   * - `Parametrizer <http://docs.nanomatch.de/nanomatch-modules/Parametrizer/Parametrizer.html>`_
     - | IP in vacuum (DFT)
     - .. image:: stokes_shift/Parametrizer3.png
          :width: 100px
          :align: center
   * - `Parametrizer <http://docs.nanomatch.de/nanomatch-modules/Parametrizer/Parametrizer.html>`_
     - | EA in vacuum (DFT)
     - .. image:: stokes_shift/Parametrizer3.png
          :width: 100px
          :align: center
   * - `Parametrizer <http://docs.nanomatch.de/nanomatch-modules/Parametrizer/Parametrizer.html>`_
     - | IP in medium (COSMO)
     - .. image:: stokes_shift/Parametrizer3.png
          :width: 100px
          :align: center
   * - `Parametrizer <http://docs.nanomatch.de/nanomatch-modules/Parametrizer/Parametrizer.html>`_
     - | EA in medium (COSMO)
     - .. image:: stokes_shift/Parametrizer3.png
          :width: 100px
          :align: center
   * - IP/EA Analysis
     - | Compute *IP* and *EA* as:
       | :math:`\mathrm{IP} = -\mathrm{HOMO}_\mathrm{GW} - P^+_\mathrm{DFT}`
       | :math:`\mathrm{EA} = -\mathrm{LUMO}_\mathrm{GW} + P^-_\mathrm{DFT}`
     - .. image:: stokes_shift/StokesShiftAnalysis.png
           :width: 100px
           :align: center


Implemented Scientific Methods
------------------------------

+---------------------------------------------------------------+-----------------------------------------------------------+
| **Step**                                                      | **Method**                                                |
+===============================================================+===========================================================+
| Ground-State Geometry Optimization                            | DFT, B3LYP/def2-SVP                                       |
+---------------------------------------------------------------+-----------------------------------------------------------+
| DFT Single Point Calculations (vacuum / COSMO)                | DFT, BP86/def2-SVPD                                     |
+---------------------------------------------------------------+-----------------------------------------------------------+
| GW Calculations in complete basis set limit                   | G₀W₀@PBE0/(aug-cc-pVDZ, aug-cc-pVTZ)                      |
+---------------------------------------------------------------+-----------------------------------------------------------+

Software:

- Quantum Chemistry: `PySCF <https://pyscf.org/>`_
- Geometry Optimization: `geomeTRIC <https://github.com/leeping/geomeTRIC>`_


Output
------

Displayed Results
~~~~~~~~~~~~~~~~~

The data below will be displayed as the workflow ends (backend name: `result.yml`):

.. code-block:: yaml

    QLQHAHDIYGVQJO-UHFFFAOYSA-N:
      EA:
        results:
          EA in eV: 2.5607947915471554
          LUMO_vacuum in eV: -1.6542377032731708
          P_minus in eV: 0.9065570882739848
        value: 2.5607947915471554
      IP:
        results:
          HOMO_vacuum in eV: -6.784890425832648
          IP in eV: 5.928143563226561
          P_plus in eV: 0.8567468626060872
        value: 5.928143563226561

Here, not only computed estimated solid-state EA/IP estimators are saved (``EA``/``IP``), but also the quantities used to calculate the estimation of them:

- ``EA``/``IP`` are the solid-state values of the IP and EA.
- ``P_plus`` and ``P_minus`` are cation and anion polarization energies, respectively.
- ``HOMO_vacuum`` and ``LUMO_vacuum`` are computed in vacuum with GW method.


Files
~~~~~
In addition to parsed output, the following file are available upon the workflow completion:

.. list-table::
   :header-rows: 1
   :widths: 5 15 50

   * - No.
     - File
     - Description
   * - 1
     - `Molecule_opt.mol2`
     - Ground State geometry in MOL2 format