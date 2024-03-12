import pandas as pd


inputdir="/home/surya/01_Datasets/Rousset_2018_GW_phagefactors/Supplementary"
outdir_growth="/home/surya/01_Datasets/Rousset_2018_GW_phagefactors/00_growth_LCE75_screen/"
outdir_phage="/home/surya/01_Datasets/Rousset_2018_GW_phagefactors/00_phage_screen/"
outdir_transduction="/home/surya/01_Datasets/Rousset_2018_GW_phagefactors/00_transduction_screen/"
# load the supplementary file with the sgRNA sequences and sgRNA names
# growth screen

seqfasta=pd.read_csv(inputdir + "/01_sgRNAs_growthLC_E75_screen.csv", sep= ",")
# create the fasta file in the desired dir 
with open( outdir_growth + "00_sgRNAs.fasta", "a") as fh:
    for line in range(len(seqfasta["target"])):
        header=">" + str(seqfasta["gene"][line]) + "|" + str(seqfasta["position"][line]) + "\n"
        seq= str(seqfasta["target"][line]) + "\n"
        fh.write(header)
        fh.write(seq) 
fh.close()

# phage screen

seqfasta=pd.read_csv(inputdir + "/04_sgRNAs_phages_screen.csv", sep= ",")
# create the fasta file in the desired dir 
with open( outdir_phage + "00_sgRNAs.fasta", "a") as fh:
    for line in range(len(seqfasta["target"])):
        header=">" + str(seqfasta["gene"][line]) + "|" + str(seqfasta["position"][line]) + "\n"
        seq= str(seqfasta["target"][line]) + "\n"
        fh.write(header)
        fh.write(seq) 
fh.close()

# transduction screen 

seqfasta=pd.read_csv(inputdir + "/06_sgRNAs_transduction_screen.csv", sep= ",")
# create the fasta file in the desired dir 
with open( outdir_transduction + "00_sgRNAs.fasta", "a") as fh:
    for line in range(len(seqfasta["target"])):
        header=">" + str(seqfasta["gene"][line]) + "|" + str(seqfasta["pos"][line]) + "\n"
        seq= str(seqfasta["target"][line]) + "\n"
        fh.write(header)
        fh.write(seq) 
fh.close()




