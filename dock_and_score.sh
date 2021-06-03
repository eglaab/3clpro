#!/bin/bash
#
#__________________________________________________
# Script to perform FlexX-ing, then Hyde-ing, 
#                           then best-of-n Picking
#
#__________________________________________________
# USAGE:
#
# dock_and_score.sh   [FXX_FILE]   [LIGANDS_MOL2_FILE]
#
# e.g. 
# dock_and_score.sh 3eml_defaults_dockTop30.fxx test.mol2
#
#__________________________________________________
# WHAT IS THIS SCRIPT?
#__________________________________________________
# 
# Run a leadit docking (flexx + flexsis) with a 
# protein prepared as a leadit2.1 fxx file and 
# a set of ligands prepared as mol2 file.
# 
# NEEDED: 
#
# - LeadIT executable + license
# - hydescorer executable (usually in LeadIT2 package)
# - extract_hydescores.py script (in this folder)
# - a bash and python (cygwin+windows works, too)
# - BIOSOLVE_LICENSE_FILE variable point to lic.server or lic.file
#
#__________________________________________________
#
# INPUT:
#
# - fxx protein input WITH DOCKING defined; 
#       optional: - definition of number of poses to keep
#                 - pharmacophore definition in the docking
# - mol2 ligands input
#
# OUTPUT:
# - csv file with ligand names and Hyde/TS1 scores
#   to be read in with excel for plotting
#
# CAVEATs:
# (1) the hydescorer csv output file must not have an 
#     empty line at the end.
#
# (2) the ligand identifier is the ligand name. 
#     -> if a ligand name occurs more than once, 
#        the respective inputs will be merged, and 
#        the lowest energy from all ligands with the
#        same name will be taken.
#__________________________________________________



#########################################
# USER, PLEASE SPECIFY THE FOLLOWING: 
#########################################
# 
# LOCATIONS OF SCRIPTS, EXEs etc.
#    Please just modify between the quotation marks!

# export license
export BIOSOLVE_LICENSE_FILE=ADD-PATH-TO-LICENSE-FILE-HERE

#
#
# 1. Where is your installation of leadit2.1 ?
leaditdir="/leadit-2.1.5-Linux-x64"
#
# 2. Where is the script extractHydeScores.py ?
extractHydeScores="./extractHydeScores.py"
#
# 3. How many docking poses shall we file into Hyde? 
nofposes="30"

#########################################
# END OF USER SPECIFICATION.
#########################################



#_________________________
# Step 0: Preparation, form generic output file names etc.:
#_________________________
leadit="$leaditdir/leadit"
#mac:
#leadit="$leaditdir/LeadIT"
hydescorer="$leaditdir/hydescorer"
#
# take fxx and input mol2 from commandline arguments:
#
project=$1
ligands=$2
#
poses=${ligands%.*}_poses.mol2
allscores=${ligands%.*}_allscores.csv 
bestscores=${ligands%.*}_bestscores.csv



#_________________________
# Step 1: Docking
#_________________________
#echo "STEP 1: Docking... (writing poses to: "$poses")"
#echo COMMAND:
#echo "$leadit" --commandline --rundock "$project"  --library="$ligands" --poses="$poses" --nof_poses=$nofposes --exit
#     "$leadit" --commandline --rundock "$project"  --library="$ligands" --poses="$poses" --nof_poses=$nofposes --exit
#echo "  docking done"




#_________________________
# Step 2: Rescoring with Hyde
#_________________________
echo "STEP 2: Hyde-ing... (writing to: "$allscores")"
echo COMMAND:
echo "$hydescorer" --target "$project" --input "$poses" --output csv --output-file "$allscores"
     "$hydescorer" --target "$project" --input "$poses" --output csv --output-file "$allscores"
echo "  Hyde-ing done."




#_________________________
# Step 3: Taking the best-scored from all ligand poses
#_________________________
echo "STEP 3: Extracting best scores... (writing to: "$bestscores")"
echo COMMAND:
echo python "$extractHydeScores" --oneline --nofposes=$nofposes "$allscores" \> "$bestscores"
     python "$extractHydeScores" --oneline --nofposes=$nofposes "$allscores" > "$bestscores"
echo "...Extracting done."


echo $bestscores " should have been written."
echo "All done. Call Excel to read the CSV file, please."
