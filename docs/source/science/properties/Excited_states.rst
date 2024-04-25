S, T, f: Excited state properties
=================================

Closed-shell molecules exists in stable, singlet ground states (:math:`S_{0}`) where all of their electrons are paired in the occupied orbitals. Excitation refers to the promotion of an electron into higher-energy orbitals, typically with the absorption of a photon, transitioning the molecule from its ground state to an excited state: singlets (:math:`S_{n}`) for electrons remaining in anti-parallel spin alignment after excitation and triplets (:math:`T_{n}`) for parallel-spin electrons.

Radiative decay from singlet states is known as fluorescence. Most fluorescent molecules decay from their :math:`S_{1}` state due to rapid internal conversion from higher singlet states - this is known as Kasha's rule. Direct radiative decay from :math:`T_{n}` is phosphorescence, although this is less efficient due to being a spin-forbidden process. 

In general, absorption corresponds to the vertical :math:`S_{0}` > :math:`S_{n}` transition where the molecule's geometry has not yet relaxed to the minimum of the excited state's potential energy surface. Emission corresponds to the vertical :math:`S_{n}` > :math:`S_{0}` transition.

Oscillator strengths correspond to the propensity for the transition to occur and are related to the intensity of a transition. Excitations from :math:`S_{0}` > :math:`T_{n}` are formally forbidden and have zero oscillator strengths.  

In the DiaDEM database, single-molecule, vacuum vertical excitation energies related to absorption are provided, in units of eV, as precomputed properties and are estimated using the **Calibrated (TD)DFT** protocol. These are calibrated to experimental values. Oscillator strength values are also provided. 

1. :math:`E(S_{1})`: :math:`S_{0}` > :math:`S_{1}` vertical transition energy
2. :math:`f(S_{1})`: oscillator strength for the :math:`S_{0}` > :math:`S_{1}` transition
3. :math:`E(S_{2})`: :math:`S_{0}` > :math:`S_{2}` vertical transition energy
4. :math:`f(S_{2})`: oscillator strength for the :math:`S_{0}` > :math:`S_{2}` transition
5. :math:`E(S_{3})`: :math:`S_{0}` > :math:`S_{3}` vertical transition energy
6. :math:`f(S_{3})`: oscillator strength for the :math:`S_{0}` > :math:`S_{3}` transition
7. :math:`E(S_{4})`: :math:`S_{0}` > :math:`S_{4}` vertical transition energy
8. :math:`f(S_{4})`: oscillator strength for the :math:`S_{0}` > :math:`S_{4}` transition
9. :math:`E(T_{1})`: :math:`S_{0}` > :math:`T_{1}` vertical transition energy
10. :math:`E(T_{2})`: :math:`S_{0}` > :math:`T_{2}` vertical transition energy
