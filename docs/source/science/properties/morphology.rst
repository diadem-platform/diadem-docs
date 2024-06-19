.. _science_properties_morphology:

Morphology
==========


.. list-table::
   :header-rows: 1
   :align: center

   * - Calculators
     - Notes
   * - :ref:`science_calculators_morphology`
     - recommended
   * - :ref:`science_calculators_mobility`
     - byproduct



What is Material Morphology?
----------------------------

Morphology, in a general sense, refers to the form, structure, and arrangement of the constituent parts of a substance. For organic materials, morphology encompasses the size, shape, and distribution of the molecules that make up the material, as well as their arrangement and organization. The morphology of organic semiconductors (OS) is molecule-dependent, and for industry-relevant amorphous materials, the molecular structure may directly determine the characteristics of the morphology.

In the context of organic semiconductors, particularly small molecule organic semiconductors, morphology specifically refers to the arrangement and structure of the organic molecules within the material. This includes the presence of crystalline and amorphous regions, the molecular packing, and the overall molecular order. The detailed study of morphology is essential for understanding and optimizing the electronic and optical properties of these materials. In terms of the multiscale simulation of material properties, for instance, OLED characteristics, morphology is a prerequisite to determining mobility, ionization potential (IP), and electron affinity (EA) of the molecules constituting a material.


Importance of Morphology
------------------------

In organic electronic devices, the properties of a single molecule are significant, but the collective arrangement of these molecules determines the overall material characteristics. The morphology of organic semiconductors is critically important because it directly affects the material's electronic properties and, consequently, the performance of devices made from these materials. Specifically:

- **Charge Transport**: The arrangement of molecules influences how easily charge carriers (electrons and holes) can move through the material. Well-ordered, crystalline regions generally allow for more efficient charge transport compared to disordered, amorphous regions. Additionally, the gigantic surface potential in small molecule organic semiconductors plays a role in charge transport.
- **Optical Properties**: The molecular packing and order can affect how the material interacts with light, influencing properties such as absorption and emission. For example, in OLEDs, effective light outcoupling is influenced by the morphology of the material.
- **Device Stability**: The stability of the material under operational conditions can be affected by its morphology. Materials with well-defined, stable morphologies are less likely to degrade over time.

Generating Atomistic Morphologies Starting from First Principles
----------------------------------------------------------------

Generating atomistic morphologies [1]_, [2]_, [3]_, [4]_ is a critical starting point for understanding and predicting the properties of organic semiconductors. By generating atomistic morphologies, one can obtain secondary properties such as charge carrier mobility, conductivity, optical absorption spectra, ionization potentials, and electron affinities of the embedded molecules. These properties are crucial for the comprehensive understanding and optimization of materials for specific applications.


Nanomatch Multiscale Workflow for Morphology
--------------------------------------------

In the DiaDEM Platform, the Nanomatch Multiscale Workflow for morphology is employed (:ref:`science_calculators_morphology`), which includes:

- Molecule parametrization,
- Morphology deposition using a Monte-Carlo protocol mimicking physical deposition (*DEPOSIT protocol* [1]_),
- Analysis of the generated morphology using various computational tools,
- Calculation of key morphological properties such as radial distribution function, mass and number density, mean distance to the nearest neighbours.

The morphology can be downloaded under the name `structure.cml` along with other files (:ref:`science_calculators_morphology_files`).

The morphological properties, which are computed within the calculator  :ref:`science_calculators_morphology` are explained in the Table below.

.. list-table::
   :header-rows: 1

   * - Parameter
     - Description
     - Units
     - Value (example)
     - Additional Information
   * - average_neighbors
     - Average distance to neighboring molecules
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


Using existing or generated morphology, the determination of secondary properties that depend on the morphology, such as charge carrier mobility, ionization potentials (IP), and electron affinities (EA) as possible as well.
For example, see :ref:`science_properties_mobility`.

Although this workflow integrates extensive experience and advanced simulation methods, including quantum chemistry (QM), molecular mechanics (MM), and Monte Carlo simulations, the user only needs to know the structure of the molecule. This makes the workflow accessible to all users, regardless of their background.
The DiaDEM project allows you to compute detailed morphological characteristics and secondary properties for any single-component organic semiconductor by simply specifying the molecule in the form of an InChI key.




References
----------

.. [1] Neumann, T., Friederich, P., Symalla, F., Meded, V., Wenzel, W., "Simulating Charge Transport in Organic Semiconductors: From Quantum Chemistry to Device Simulation," Journal of Computational Chemistry, 34 (31), 2013, 2716-2725. URL: https://onlinelibrary.wiley.com/doi/abs/10.1002/jcc.23445.
.. [2] Friederich, P., et al., "The influence of impurities on the charge carrier mobility of small molecule organic semiconductors," arXiv, 2019. DOI: 10.48550/arXiv.1908.11854. URL: https://arxiv.org/abs/1908.11854.
.. [3] Reiser, P., Friederich, P., et al., "Analyzing dynamical disorder for charge transport in organic semiconductors via machine learning," arXiv, 2021. DOI: 10.48550/arXiv.2102.01479. URL: https://arxiv.org/abs/2102.01479.
.. [4] Friederich, P., "Built-In Potentials Induced by Molecular Order in Amorphous Organic Semiconductors," Karlsruhe Institute of Technology, 2021. URL: https://publikationen.bibliothek.kit.edu/1000141627/138747603.
