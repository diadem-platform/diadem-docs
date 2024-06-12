.. _science_calculators_mobility:

Charge Carrier Mobility. Calculator **mobility**.
========


The Nanomatch Mobility Workflow (Calculator "**mobility**") is a multiscale simulations workflow designed to calculate the hole mobility of organic semiconductors starting from the first-principles.
Users only need to provide the molecular structure as an InChI key. The workflow then takes over, progressing from the atomic properties to the macroscopic hole mobility, ensuring an efficient and comprehensive computational protocol.

The brief overview is given in the table below.


.. list-table:: Mobiliy Worflow Overview
   :widths: 30 30 30
   :header-rows: 1

   * - **Nanomatch Software**
     - **Scientific Role**
     - **Illustration**
   * - `Parametrizer <http://docs.nanomatch.de/nanomatch-modules/Parametrizer/Parametrizer.html>`_
     - | Geometry optimization
     - .. image:: parametrizer.png
          :width: 300px
          :align: center
   * - `DihedralParametrizer <http://docs.nanomatch.de/nanomatch-modules/DihedralParametrizer/DihedralParametrizer.html>`_
     - | Parametrization of the total energy
       | depending on dihedral angles
     - .. image:: dhp.png
          :width: 300px
          :align: center
   * - `Deposit <http://docs.nanomatch.de/nanomatch-modules/Deposit/Deposit.html>`_
     - | Simulation of the physical deposition
       | to obtain atomistic morphology
     - .. image:: deposit.png
          :width: 300px
          :align: center
   * - `QuantumPatch <http://docs.nanomatch.de/nanomatch-modules/QuantumPatch/QuantumPatch.html>`_
     - | Calculation of electronic properties
       | including charge transfer parameters
     - .. image:: quantumpatch.png
          :width: 300px
          :align: center
   * - `LightForge <http://docs.nanomatch.de/nanomatch-modules/LightForge/LightForge.html>`_
     - | Simulation of charge-carrier transport
       | using kMC protocol
     - .. image:: lightforge.png
          :width: 300px
          :align: center


Implemented Scientific Methods
------------------------------

The following scientific methods are implemented in the Calculator "**mobility**":

1. **Molecular Structure Optimization**:
   *obabel*, *xtb*, and *Density Functional Theory (DFT)* are used to generate initial 3D conformers, pre-optimize and optimize the geometry, and compute partial charges via an electrostatic potential (ESP) fit for single molecules in a vacuum. DFT optimization is performed with def2-TZVP/B3LYP level of theory.

2. **Morphology Generation**:
   The *DEPOSIT protocol* simulates physical vapor deposition to generate thin-film morphologies with atomistic resolution. This involves Monte Carlo (MC) based basin hopping with simulated annealing (SA) to model intermolecular interactions during deposition. In total, 1000 molecules are deposited into a box with a base size of 100x100 Å. After this, the top and bottom 7 Å are cut out, and periodic copies are added in the x and y axes to increase its base size to 300x300 Å.

3. **Electronic Structure Calculation**:
   Using the *QuantumPatch method*, energy disorder, electronic couplings, and reorganization energies are calculated by self-consistently equilibrating the charge densities of a subset of molecules in their unique environments. The shell structure is the same as described in [Simon's paper]. In total, 100 molecules embedded in the morphology are considered, for which the HOMO/LUMO are self-consistently computed to yield the energy disorder, and their interactions are used to compute the overlap integral distribution across relevant distances.

4. **Structure Expansion**:
   To bridge the scales from atomistic resolution to the device level, a *stochastic extension scheme* is used to expand the thin-film morphologies, drawing electronic couplings and site energies from distributions analyzed in the QuantumPatch method.

5. **Charge Transport Simulation**:
   *Kinetic Monte Carlo (kMC) simulations* model charge transport in organic semiconductor thin films. The workflow uses the LightForge package to simulate field-dependent mobility, taking into account percolation and many-body effects. Zero-field mobility is extrapolated to the zero-field limit assuming Poole-Frenkel field dependence.


Reference
---------

