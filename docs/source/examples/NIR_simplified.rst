
DiaDEM Tutorial: Discovery of Near-Infrared Materials
=======================================================

The discovery of near-infrared materials can be achieved with the DiaDEM platform. Candidates can be purchased directly and tested for near-infrared activity by the researcher.

General theory
--------------

Near-infrared materials are a class of compounds that can absorb and emit light in the near-infrared range (750-2500 nm). Their applications span a wide variety of domains including communications, medical imaging, photovoltaics, sensing and night-vision. The synthesis of photostable, high-mobility and device-compatible near-infrared compounds is extremely challenging, making them a rare and coveted class of materials. Near-infrared absorption and emission in organic compounds is normally seen in extended π-conjugated systems, donor-acceptors, ionic dyes and metal complexes. 

Requirements for near-infrared absorption-emission
--------------------------------------------------

The requirement for near-infrared absorption-emission is simply the existence of near-infrared absorption and/or emission band(s) in the respective absorption and fluorescence spectra. In computational terms, the energy of the :math:`S_{0}` :math:`\rightarrow` :math:`S_{1}` transition E(:math:`S_{1}`) should be lower than 1.65 eV (750 nm). Due to molecular design, these low-energy states are usually weak in intensity, e.g. small transition dipole moment for donor-acceptors due to non-spatially-overlapping HOMO and LUMO; therefore, a bright :math:`S_{1}` can be imposed by setting a lower limit for the oscillator strength f(:math:`S_{1}`). 

Searching for candidates
------------------------

Finding near-infrared candidates based on the requirements detailed above can be done using the **Search** functionality found on the navigation bar. First click **+Group**, then **+Rule** twice.  Choose the **Property Name** for the first singlet excited state transition energy E(:math:`S_{1}`) and set the **Value** to be **less than** 1.65 eV, then **Submit Query**. 

This will search the DiaDEM database for all molecules which have an experimentally calibrated, vertical :math:`S_{0}` :math:`\rightarrow` :math:`S_{1}` energy lower than the boundary of red to near-infrared light. 
For additional constraints, return to the **Search** function and add another condition block within the same query using **+Group**. Continue by choosing the oscillator strength for the first singlet transition f(:math:`S_{1}`) and set this **Value** to be **greater than** 0.05. This value can be modified; the greater the value, the brighter the :math:`S_{1}` state is predicted to be, removing those entries with forbidden or low-intensity transitions.

Purchasing materials
--------------------

All of the molecules on the DiaDEM database are commercially available and can be purchased directly for laboratory testing; however, availability for a material at any given time can vary. 

In the **Search** results, clicking on a molecular entry will open a new page with greater detail, including more properties, availability and price. You can add a material to cart by clicking **Add to cart**. The cart can be accessed at the top right of the banner. From here, the quantity of material can be modified. An **Indicative price** will be shown and a purchase request can be made by pressing **Submit request**. After processing, final pricing, delivery time and additional information will be provided, and a **Notification** will appear which can be opened from the navigation bar. If email notifications are enabled, an automated email will be sent.
