#!/bin/bash -l
module load bio/GROMACS/2019.2-intelcuda-2019a
./namd2 ligand_binding_simulation.namd > ligand_binding_simulation_simul.log