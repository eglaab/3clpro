#
# Apply ligand preparation and molecular docking using the AutoDock-GPU software for all compounds in the current directory
#

# Define input and output directories
output_folder = '/compound_folder'
setwd(output_folder)
input_folder = "/protein_folder"

# Directory containing autodock software
autodock_folder = "/AutoDock-GPU"

# Read list of compounds in mol2 format
curlst = dir()
mol2files = curlst[grep("\\.mol2$",curlst)]

# Iterate over files and prepare compounds
for(i in 1:length(mol2files)){

	# Ignore already processed compounds
        if(file.exists(paste(sub("\\.mol2","",mol2files[i]),".pdbqt",sep=""))){
         next
        }

        # Prepare current ligand
        system(paste('/work/projects/bds_early_pd/AutoDock-GPU/mgltools_x86_64Linux2_1.5.6/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_ligand4.py -l', mol2files[i]), timeout=30)
        
        # Show current progress every 100 iterations
        if(i %% 100 == 0)
            print(i)
}

# Read list of compounds in pdbqt format
pdbqtfiles = dir()[grep("\\.pdbqt",dir())]

# Iterate over compounds, prepare input grid files and run docking simulations
for(i in 1:length(pdbqtfiles)){
	
	# Ignore already processed compounds
	if(file.exists(paste(sub(".pdbqt","",pdbqtfiles[i]),"_docking.dlg",sep=""))){
		next
	}

	# Prepare grid parameter file in input folder
	setwd(input_folder)
	system(paste(autodock_folder,'/mgltools_x86_64Linux2_1.5.6/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_gpf4.py -l ',output_folder,'/',pdbqtfiles[i]," -r ",input_folder,"/receptor.pdbqt",sep=""))

	# Pre-calculate grid maps of interaction energies
    	system(paste(autodock_folder,'/x86_64Linux3/autogrid4 -p ', input_folder, '/receptor.gpf -l ', input_folder, '/receptor.glg',sep=""))
	
	# Create output in dedicated folder			
	setwd(output_folder)
		
	# Run docking with AutoDock-GPU (increasing the thoroughness of search by setting -nrun to 100)
	system(paste(autodock_folder,'/bin/autodock_gpu_256wi -ffile ', input_folder, '/receptor.maps.fld -lfile ', pdbqtfiles[i], ' -nrun 100',sep=""))
	
	# Rename docking output by the name of the corresponding compound
	system(paste('mv docking.dlg', paste(sub(".pdbqt","",pdbqtfiles[i]),"_docking.dlg",sep="")))
	
	# Show current progress every 100 iterations
	if(i %% 100 == 0)
		print(i)
}


