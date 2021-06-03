#! /bin/bash
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/leadit-2.1.5-Linux-x64
export BIOSOLVE_LICENSE_FILE=ADD-PATH-TO-LICENSE-FILE-HERE
cd /leadit-2.1.5-Linux-x64

files=(*.mol2)
for ((i = 0; i < ${#files[@]}; ++i)); do
    b=`basename ${files[$i]} .mol2`
    f=${files[$i]}
    echo Processing ligand $b
    /leadit-2.1.5-Linux-x64/leadit --commandline --library $f --rundock --poses ../parsed/${b}_poses.mol2 --nof_poses 30 --soltab ../parsed/${b}_scoretable.csv --exit -o csv /home/users/eglaab/bin/leadit-2.1.5-Linux-x64/corona/5r8t_maestro_filtered.fxx
    mv $f ../parsed/$f
done

