#!/bin/bash 

# activate the conda environment where all the python packages are installed
eval "$(conda shell.bash hook)"
conda activate CRISPRi_Project

ref_fasta="/home/surya/Downloads/MERF_runs/CRISPRi_Project_SCRIPTS_datasets/Ref_genome_Ecoli_NC_000913/NC_000913.3.fasta"
ref_gff="/home/surya/Downloads/MERF_runs/CRISPRi_Project_SCRIPTS_datasets/Ref_genome_Ecoli_NC_000913/NC_000913.3.gff3"

indir="/home/surya/Downloads/MERF_runs/CRISPRi_Project_SCRIPTS_datasets/Rousset_2018_GW_phagefactors/Supplementary" 



#growth screen

outdir1="/home/surya/Downloads/MERF_runs/CRISPRi_Project_SCRIPTS_datasets/Rousset_2018_GW_phagefactors/00_growth_LCE75_screen/01_sgRNA_preprocessing_growthV2"
python 00_machine_learning_data_Rousset_final_original_morefeatures.py $ref_fasta $ref_gff $indir/01_sgRNAs_growthLC_E75_screen.csv -o $outdir1 

#phage screen
 
outdir2="/home/surya/Downloads/MERF_runs/CRISPRi_Project_SCRIPTS_datasets/Rousset_2018_GW_phagefactors/00_phage_screen/01_sgRNA_preprocessing_phageV2" 
python 00_machine_learning_data_Rousset_final_original_morefeatures.py $ref_fasta $ref_gff $indir/04_sgRNAs_phages_screen.csv -o $outdir2 

#transduction screen
outdir3="/home/surya/Downloads/MERF_runs/CRISPRi_Project_SCRIPTS_datasets/Rousset_2018_GW_phagefactors/00_transduction_screen/01_sgRNA_preprocessing_transductionV2"
python 00_machine_learning_data_Rousset_final_original_morefeatures.py $ref_fasta $ref_gff $indir/06_sgRNAs_transduction_screen.csv -o $outdir3

conda deactivate
