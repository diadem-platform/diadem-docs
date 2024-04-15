ESOL values
=============

For the DiaDEM project we have selected the ESOL [1]_ values for predicting aqueous solubility, as we intended to utilise freely available models.
ESOL is a simple empirical method that can provide aqueous solubility information based on structural properties.
Originally, various properties were considered to have effect on the solubility, including:
    - octanol-water partition coefficient (cLogP)
    - molecular weight (MW)
    - number of rotatable bonds (RB)
    - aromatic portion (AP) - proportion of aromatic atoms among heavy atoms
    - non-carbon portion (NCP) - the proportion of heavy atoms in the molecule that are not carbon
    - hydrogen-bond donors (HBD)
    - hydrogen-bond acceptors (HBA)
    - polar surface area (PSA)
Such data of 2874 natural compounds were utilized for training, and four parameters were found to have significant contributions to the final solubility model.
Generally, the partitioning coefficient, the molecular weight, the number of rotatable bonds and the aromatic portion of the molecule was found to be related to aqueous solubility. The final equation for providing the ESOL values is:
:math:`Log(S) = 0.16 - 0.63 clogP - 0.0062 MW + 0.066 RB - 0.74 AP``

.. [#] John S. Delaney J. Chem. Inf. Comput. Sci. 2004, 44, 3, 1000–1005 https://pubs.acs.org/doi/10.1021/ci034243x
