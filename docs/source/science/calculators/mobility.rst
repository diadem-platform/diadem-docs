.. _science_calculators_mobility:

Charge Carrier Mobility. Calculator **mobility**.
========


The Nanomatch Mobility Workflow (Calculator "**mobility**") is a multiscale simulations workflow designed to calculate the hole mobility of organic semiconductors starting from the first-principles.
Users only need to provide the molecular structure as an InChI key. The workflow then takes over, progressing from the atomic properties to the macroscopic hole mobility, ensuring an efficient and comprehensive computational protocol.

The brief overview is given in the table below.


.. list-table:: Mobility Workflow Overview
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

Molecular Structure Optimization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*obabel*, *xtb*, and *Density Functional Theory (DFT)* are used to generate initial 3D conformers, pre-optimize and optimize the geometry, and compute partial charges via an electrostatic potential (ESP) fit for single molecules in a vacuum. DFT optimization is performed with def2-TZVP/B3LYP level of theory.

Morphology Generation
~~~~~~~~~~~~~~~~~~~~~

The *DEPOSIT protocol* simulates physical vapor deposition to generate thin-film morphologies with atomistic resolution. This involves Monte Carlo (MC) based basin hopping with simulated annealing (SA) to model intermolecular interactions during deposition. In total, 1000 molecules are deposited into a box with a base size of 100x100 Å. After this, the top and bottom 7 Å are cut out, and periodic copies are added in the x and y axes to increase its base size to 300x300 Å.

Electronic Structure Calculation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using the *QuantumPatch method*, energy disorder, electronic couplings, and reorganization energies are calculated by self-consistently equilibrating the charge densities of a subset of molecules in their unique environments.
The shell structure is similar to those described in *Keiser et al* [1]_.

In total, 200 molecules core molecules are considered, embedded in the generated morphology.
For these 200 molecules the following is computed:

- **HOMO/LUMO** levels of the embedded molecules,
- **Electronic couplings** for every pair of 200 molecules if their distance is below a reasonable threshold.

From HOMO/LUMO distributions, the energy disorder is deduced.

are self-consistently computed to yield the energy disorder, and their interactions are used to compute the overlap integral distribution across relevant distances.

The parameters of the *QuantumPatch* embedding scheme is as follows:

- **Core molecule**: Self-consistent DFT def2-SVP/B3LYP
- **First shell**: Self-consistent DFT shell def2-SVP/BP86, radius 15 Å
- **Second shell**: Self-consistent DFTB, radius 25 Å
- **Third shell**: Static DFTB, radius 60 Å


Structure Expansion
~~~~~~~~~~~~~~~~~~~

To bridge the scales from atomistic resolution to the device level, a stochastic expansion scheme *EDCM* is used to expand the thin-film morphologies,
drawing electronic couplings and site energies from distributions analyzed in the QuantumPatch method.

Charge Transport Simulation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Kinetic Monte Carlo (kMC) simulations* model charge transport in organic semiconductor thin films.
The workflow uses the LightForge package to simulate field-dependent mobility, taking into account percolation and many-body effects [3]_.
Zero-field mobility is extrapolated to the zero-field limit assuming Poole-Frenkel field dependence.

Parameters of the kMC simulations:

- **Fields**: three fields are applied: 0.02 0.03 0.04 eV/nm.
- **Morphology** and **replicas**: for every field value, 10 independent morphologies are generated using the stochastic extension scheme, including HOMO/LUMO/Js distributions derived from the *QuantumPatch* simulations.
- **Temperature** is 300 K.
- **Convergence criterion**: either the fluctuation parameter "iv_fluctuation" below 0.05, or "max_iterations" exceeds 5E6.
- **Number of Charge Carrier**:
- **Neighbours**: 120, meaning a charge carrier can jump to the nearest 120 neighboring molecules.

Output
------

Parsed Output
~~~~~~~~~~~~~
The data below will be displayed as the workflow ends:

.. code-block:: yaml

    ZUOUZKKEUPVFJK-UHFFFAOYSA-N:
      HOMO:
        value: -6.3045408287491576
      LUMO:
        value: -0.9858224512636844
      dipole:
        value:
        - -1.3528304359760581e-05
        - 3.1219102412616073e-06
        - 1.6623358493787502e-05
      mobility:
        results:
          fields:
            units: V/nm
            values:
            - 0.2
            - 0.3
            - 0.4
          mobilities:
            units: cm2/V*s
            values:
            - 0.0007483182783762549
            - 0.0025391270604621014
            - 0.007458906308908711
          stderr:
            units: cm2/V*s
            values:
            - 7.776944379601362e-05
            - 0.00021154214466139146
            - 0.000801520575814753
        value: 2.893350117363308e-06
      morphology:
        results:
          average_neighbors:
            unit: Angstrom
            value: 13.4
          mass_density:
            std: 0.01
            unit: g/cm3
            value: 1.12
          molecular_volume:
            unit: nm3
            value: 0.23
          number_density:
            std: 1.63e+20
            unit: 1/cm3
            value: 4.42e+21
          rdf_first_peak:
            unit: Angstrom
            value: 3.9184952978056424
        value: 'file: structure.cml'

The zero-field mobility measured in [cm2/V*s] is: `result['ZUOUZKKEUPVFJK-UHFFFAOYSA-N']['mobility']['value']`

The value is derived from field-dependent mobilities, which are also provided in the output. Extrapolation is performed using linear regression in the log(mobility) vs. sqrt(field) plot. The extrapolation is shown in one of the output files, example: `mobility_vs_sqrt_field.png <../../../../../docs/build/html/_static/mobility_files/mobility_vs_sqrt_field.png>`_.

Files
~~~~~~~~~

In addition to parsed output, the following files are available upon the workflow completion:

.. list-table::
   :header-rows: 1
   :widths: 5 15 15 50

   * - No.
     - File
     - Description
     - Example
   * - 1
     - DeltaE_*.png
     - | Distribution of the HOMO/LUMO
       | levels, local and global,
       | values of computed disorder.
     - .. image:: mobility_files/DeltaE_8_80d05a518bbbefc060f8c4ec4026517b.80d05a518bbbefc060f8c4ec4026517b.png
          :width: 300px
          :align: center
   * - 2
     - output_molecule.mol2
     - | Molecule output file in MOL2
       | format.
     - `output_molecule.mol2 <../../../../../docs/build/html/_static/mobility_files/output_molecule.mol2>`_
   * - 3
     - summary_RDF.png
     - | Radial distribution function
       | (RDF).
     - .. image:: mobility_files/summary_RDF.png
          :width: 300px
          :align: center
   * - 4
     - mobility_vs_sqrt_field.png
     - | Poole-Frenkel plot of the
       | mobility versus the square
       | root of the electric field.
     - .. image:: mobility_files/mobility_vs_sqrt_field.png
          :width: 300px
          :align: center
   * - 5
     - structure.cml
     - | Molecular structure in
       | CML format.
     - `structure.cml <../../../../../docs/build/html/_static/mobility_files/structure.cml>`_
   * - 6
     - visualization_2D_and_3D.png
     - | 2D and 3D visualizations
       | of the molecular structure.
     - .. image:: mobility_files/visualization_2D_and_3D.png
          :width: 300px
          :align: center


Reference
---------

.. _ref1:

.. [1] Keiser, S., et al., "De Novo Calculation of the Charge Carrier Mobility in Amorphous Small Molecule Organic Semiconductors," Frontiers in Chemistry, 9, 2021. URL: https://www.frontiersin.org/articles/10.3389/fchem.2021.801589.

.. _ref2:

.. [2] Friederich, P., Symalla, F., Meded, V., Neumann, T., Wenzel, W., "Ab Initio Treatment of Disorder Effects in Amorphous Organic Materials: Toward Parameter Free Materials Simulation," Journal of Chemical Theory and Computation, 10 (9), 2014, 3720-3725. URL: https://doi.org/10.1021/ct500418f.

.. _ref3:

.. [3] Symalla, F., Friederich, P., Massé, A., Meded, V., Coehoorn, R., Bobbert, P., Wenzel, W., "Charge Transport by Superexchange in Molecular Host-Guest Systems," Physical Review Letters, 2016, 117, 276803. URL: https://doi.org/10.1103/PhysRevLett.117.276803.
