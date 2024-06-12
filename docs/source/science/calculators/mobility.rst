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
   - *Density Functional Theory (DFT)* is used to optimize the geometry and compute partial charges via an electrostatic potential (ESP) fit for single molecules in a vacuum.

2. **Morphology Generation**:
   - The *DEPOSIT protocol* simulates physical vapor deposition to generate thin-film morphologies with atomistic resolution. This involves Monte Carlo (MC) based basin hopping with simulated annealing (SA) to model intermolecular interactions during deposition.

3. **Electronic Structure Calculation**:
   - Using the *QuantumPatch method*, energy disorder, electronic couplings, and reorganization energies are calculated by self-consistently equilibrating the charge densities of a subset of molecules in their unique environments.

4. **Structure Expansion**:
   - To bridge the scales from atomistic resolution to device level, a *stochastic extension scheme* is used to expand the thin-film morphologies, drawing electronic couplings and site energies from distributions analyzed in the QuantumPatch method.

5. **Charge Transport Simulation**:
   - *Kinetic Monte Carlo (kMC) simulations* model charge transport in organic semiconductor thin films. The workflow uses the lightforge (LF) package to simulate field-dependent and zero-field mobility, taking into account percolation and many-body effects.


Reference
---------

