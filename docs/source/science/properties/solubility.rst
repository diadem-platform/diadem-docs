Solubility
=============

For the DiaDEM project we have selected the ESOL [1]_ values for predicting aqueous solubility, as we intended to utilise freely available models.
ESOL is a simple empirical method that can provide aqueous solubility information based on structural properties.

Such data of 2874 natural compounds were utilized for training, and four parameters were found to have significant contributions to the final solubility model.

- octanol-water partition coefficient (cLogP)
- molecular weight (MW)
- number of rotatable bonds (RB)
- aromatic portion (AP) - proportion of aromatic atoms among heavy atoms

The final equation for providing the ESOL values is:
:math:`Log(S) = 0.16 - 0.63 clogP - 0.0062 MW + 0.066 RB - 0.74 AP`

.. [1] John S. Delaney J. Chem. Inf. Comput. Sci. 2004, 44, 3, 1000–1005 https://pubs.acs.org/doi/10.1021/ci034243x
