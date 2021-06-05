# SARS-CoV-2 3CLpro screening and pharmacophore generation

<br>
Accompanying scripts and parameter setting files for the molecular docking, MD simulations, machine learning analyses, and the pharmacophore model for the manuscript "A Pharmacophore Model for SARS-CoV-2 3CLpro Small Molecule Inhibitors and in Vitro Experimental Validation of Computationally Screened Inhibitors"
<br>

## Overview of files

<br>
Software tools:

- List of used software tools and versions for molecular docking, machine learning based compound screening, MD simulations and molecular visualizations:

  [used_software_tools_and_versions.txt](used_software_tools_and_versions.txt)

<br>
Scripts for molecular docking, binding affinity estimation, and ligand-based similarity screening:

- Script for molecular docking and binding affinity estimation using the software LeadIT FlexX/HYDE for individual compounds:

  [dock_and_score.sh](dock_and_score.sh)

- Script to extract binding affinity estimation scores from HYDE output files:

  [extractHydeScores.py](extractHydeScores.py)

- Script for the automation of molecular docking runs using the LeadIT software (iterating over all compound files in the working directory):

  [docking_leadit_script.sh](docking_leadit_script.sh)
  
- Script to generate ensembles of conformers for the compound libraries using the software OpenEye OMEGA:

  [openeye_omega.sh](openeye_omega.sh) 

- Script for molecular docking using the software OpenEye HYBRID:

  [openeye_hybrid_docking.sh](openeye_hybrid_docking.sh)
  
- Script for ligand preparation and molecular docking using the software AutoDock-GPU:

  [autodock_screening.R](autodock_screening.R)
  
- Script for ligand-based similarity screening using the FTrees software:

  [ftrees_screening.R](ftrees_screening.R)


<br>
Machine learning based compound scoring analysis:

- Script for machine learning based compound screening using quantitative descriptors extracted from compound SMILES:

  [ml_screening.R](ml_screening.R)

<br>  
Molecular dynamics simulations and molecular visualizations:

- Configuration settings used for MD simulations of ligand binding interactions in NAMD:

  [ligand_binding_simulation.namd](ligand_binding_simulation.namd)
  
- Script to run ligand binding MD simulations in NAMD:

  [run_namd_simulation.sh](run_namd_simulation.sh)
  
- Configuration settings used for PoseView 2D visualizations (= default settings):

  [poseview_settings.pxx](poseview_settings.pxx)
  
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

<br>
Pharmacophore model:

- Merged pharmacophore model in the “Compressed Pharmaceutical Markup Language” (PMZ) format:

  [3clpro_pharmacophore_ligandscout.pmz](3clpro_pharmacophore_ligandscout.pmz)







