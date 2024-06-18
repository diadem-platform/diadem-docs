.. _science_calculators_morphology:

Morphology
==========


The **morphology** calculator represents is the first part of the **mobility** calculator workflow (:ref:`science_calculators_mobility`), which terminates after the morphology is generated and analyzed.

.. list-table:: Morphology Workflow Overview
   :widths: 30 30 30
   :header-rows: 1

   * - **Nanomatch Software**
     - **Scientific Role**
     - **Illustration**
   * - `Parametrizer <http://docs.nanomatch.de/nanomatch-modules/Parametrizer/Parametrizer.html>`_
     - | Geometry optimization
     - .. image:: mobility/parametrizer.png
          :width: 300px
          :align: center
   * - `DihedralParametrizer <http://docs.nanomatch.de/nanomatch-modules/DihedralParametrizer/DihedralParametrizer.html>`_
     - | Computation of intramolecular
       | forcefields
     - .. image:: mobility/dhp.png
          :width: 300px
          :align: center
   * - `Deposit <http://docs.nanomatch.de/nanomatch-modules/Deposit/Deposit.html>`_
     - | Simulation of the physical
       | vapor deposition (PVD)
       | to obtain atomistic morphology
     - .. image:: mobility/deposit.png
          :width: 300px
          :align: center

Implemented Scientific Methods
------------------------------

The following scientific methods are implemented in the Calculator "**morphology**":

Molecular Structure Optimization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*obabel*, *xtb*, and *Density Functional Theory (DFT)* are used to generate initial 3D conformers, pre-optimize and optimize the geometry, and compute partial charges via an electrostatic potential (ESP) fit for single molecules in a vacuum. DFT optimization is performed with def2-TZVP/B3LYP level of theory.

Morphology Generation
~~~~~~~~~~~~~~~~~~~~~

The *DEPOSIT protocol* [1]_ simulates physical vapor deposition to generate thin-film morphologies with atomistic resolution. This involves Monte Carlo (MC) based basin hopping with simulated annealing (SA) to model intermolecular interactions during deposition. In total, 1000 molecules are deposited into a box with a base size of 100x100 Å.


Output
------

This Calculator provides the following properties:

- HOMO and LUMO (see :ref:`science_properties_HOMOLUMO`)
- Dipole (property not yet described / available)
- Morphology and its related properties (see section Files).


Parsed Output
~~~~~~~~~~~~~
The data below will be displayed as the workflow ends (backend name: `result.yml`):

.. code-block:: yaml

    ZUOUZKKEUPVFJK-UHFFFAOYSA-N:
      HOMO:
        value: -6.304540838835274
      LUMO:
        value: -0.9858224534777202
      dipole:
        results:
          dipole_vector:
          - -1.3524802844422331e-05
          - 3.1223022592016277e-06
          - 1.662349335263646e-05
        value: 2.1656629345848317e-05
      morphology:
        results:
          average_neighbors:
            unit: Angstrom
            value: 17.6
          mass_density:
            std: 0.01
            unit: g/cm3
            value: 1.14
          molecular_volume:
            unit: nm3
            value: 0.23
          number_density:
            std: 9.9e+19
            unit: 1/cm3
            value: 4.36e+21
          rdf_first_peak:
            unit: Angstrom
            value: 4.921630094043887
        value: 'file: structure.cml'

The table below explains each parameter, its meaning, units, and other relevant information (field "value" is occasionally omitted).

.. list-table::
   :header-rows: 1

   * - Parameter
     - Description
     - Units
     - Value
     - Additional Information
   * - HOMO
     - Highest Occupied Molecular Orbital
     - eV
     - -6.304540838835274
     - HOMO
   * - LUMO
     - Lowest Unoccupied Molecular Orbital
     - eV
     - -0.9858224534777202
     - LUMO
   * - dipole_vector
     - Components of the dipole moment vector
     - Debye (D)
     - (-1.3524802844422331e-05, 3.1223022592016277e-06, 1.662349335263646e-05)
     - Vector representation of the dipole moment
   * - dipole
     - Magnitude of the dipole moment
     - Debye (D)
     - 2.1656629345848317e-05
     - Magnitude of the dipole moment
   * - average_neighbors
     - Average number of neighboring molecules
     - Å
     - 17.6
     - Average distance to neighboring molecules
   * - mass_density
     - Mass per unit volume
     - g/cm³
     - 1.14
     - Standard deviation (`std`): 0.01 (example value)
   * - molecular_volume
     - Volume occupied by a single molecule
     - nm³
     - 0.23
     -
   * - number_density
     - Number of molecules per unit volume
     - 1/cm³
     - 4.36e+21
     - Standard deviation (`std`): 9.9e+19 (example value)
   * - rdf_first_peak
     - Position of the first peak in the radial distribution function
     - Å
     - 4.921630094043887
     - Indicates the most probable intermolecular distance


Files
~~~~~

In addition to parsed output, the following files are available upon the workflow completion:

.. list-table::
   :header-rows: 1
   :widths: 5 15 15 50

   * - No.
     - File
     - Description
     - Example
   * - 1
     - output_molecule.mol2
     - | Molecule output file in MOL2
       | format.
     - `output_molecule.mol2 <../../../../../docs/build/html/_static/science/calculators/mobility/output_molecule.mol2>`_
   * - 2
     - summary_RDF.png
     - | Radial distribution function
       | (RDF).
     - .. image:: mobility/summary_RDF.png
          :width: 300px
          :align: center
   * - 3
     - structure.cml
     - | Molecular structure in
       | CML format.
     - `structure.cml <../../../../../docs/build/html/_static/science/calculators/mobility/structure.cml>`_
   * - 4
     - | visualization_2D
       | _and_3D.png
     - | 2D and 3D visualizations
       | of the molecules
       | (center of geometries)
     - .. image:: mobility/visualization_2D_and_3D.png
          :width: 300px
          :align: center


Reference
---------

.. _ref1:

.. [1] Neumann, T., Friederich, P., Symalla, F., Meded, V., Wenzel, W., "Simulating Charge Transport in Organic Semiconductors: From Quantum Chemistry to Device Simulation," Journal of Computational Chemistry, 34 (31), 2013, 2716-2725. URL: https://onlinelibrary.wiley.com/doi/abs/10.1002/jcc.23445.
