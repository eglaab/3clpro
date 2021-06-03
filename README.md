# SARS-CoV-2 3CLpro screening and pharmacophore generation

<br>
Accompanying files for the manuscript "A pharmacophore model for SARS-CoV-2 3CLpro small molecule inhibitors and experimental validation of computationally screened inhibitors"
<br>

## Overview of files

<br>
Settings and pharmacophore files:

- Configuration settings used for MD simulations of ligand-binding interactions in NAMD:

  [ligand_binding_simulation.namd](ligand_binding_simulation.namd)

- Merged pharmacophore model in the “Compressed Pharmaceutical Markup Language” (PMZ) format:

  [3clpro_pharmacophore_ligandscout.pmz](3clpro_pharmacophore_ligandscout.pmz)

<br>
Molecular docking scripts:

- Script for molecular docking using LeadIT/FlexX (iterating over all compound files in working directory):

  [docking_leadit_script.sh](docking_leadit_script.sh)
  
- Script for docking and binding affinity estimation using FlexX/HYDE for individual compounds:

  [dock_and_score.sh](dock_and_score.sh)
  
- Script to extract binding affinity stimation scores from HYDE output files:

  [extractHydeScores.py](extractHydeScores.py)

- Script to generate ensembles of conformers for the compound libraries using the software OpenEye OEOmega:

  [openeye_omega.sh](openeye_omega.sh) 

- Script for molecular docking using the software OpenEye HYBRID:

  [openeye_hybrid_docking.sh](openeye_hybrid_docking.sh) 

<br>  
Molecular dynamics simulations:  
  
- SARS-CoV-2 3CLpro protein in complex with small molecule compound <b>M-8524</b>:

  [Video animation](https://youtu.be/_Pzde7GRawM)
  
- SARS-CoV-2 3CLpro protein in complex with small molecule compound <b>M-1805</b>:

  [Video animation](https://youtu.be/Jj5nmU-U6IU)

- SARS-CoV-2 3CLpro protein in complex with natural compound <b>baicalein</b>:

  [Video animation](https://youtu.be/SiPqjSoYu6k)

- SARS-CoV-2 3CLpro protein in complex with natural compound <b>luteolin</b>:

  [Video animation](https://youtu.be/RrpM8l70euc)
- SARS-CoV-2 3CLpro protein in complex with natural compound <b>rottlerin</b>:

  [Video animation](https://youtu.be/aoVfy5d7388)
  
- SARS-CoV-2 3CLpro protein in complex with natural compound <b>amentoflavone</b>:

  [Video animation](https://youtu.be/5iWZRTRgG0Y)  







