#
# Ligand similarity screening for 3CLpro inhibitors using the FTrees software
#

# retrieve smi files with compounds to screen in the current directory
smifiles = dir()[grep("\\.smi$",dir())]

# specify file containing the SMILES for the 3CLpro inhibitor query compounds
query_smi = "query_3clpro_binders.smi"

# iterate over smi files and apply Ftrees screening
for(i in 1:length(smifiles)){
        
        # ignore smi files which have already been processed
        if(file.exists(paste(basename(smifiles[i]),"_1.csv",sep=""))){
         next
        }

        # show current progress
        print(paste(i,". file out of ",length(smifilt)," - ",100*i/length(smifilt),"% complete - current file:",smifilt[i],sep=""))

        # apply FTrees screening to current smi file
        system(paste("/ftrees-6.2-Linux-x64/ftrees -i ",query_smi," -s ",smifilt[i]," -o ", basename(smifilt[i]),'.csv',sep=""))
        
}

