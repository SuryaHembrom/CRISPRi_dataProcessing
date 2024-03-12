from multiprocessing import process
from token import RPAR
from xml.etree.ElementPath import prepare_parent
import pandas as pd
from Bio.Seq import Seq
from Bio import SeqIO
import numpy as np
import os 
import argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)

parser.add_argument("preprocessed_sgRNA_library",
                    help = "processing results of sgRNA library in csv format (comma separated file)" )
parser.add_argument("-o", "--output", help="output directory name")

args = parser.parse_args()
#print(args.echo)
sgRNAlibrary=args.preprocessed_sgRNA_library
output=args.output


#output="/home/surya/01_Datasets/Rousset_2018_GW_phagefactors/00_growth_LCE75_screen/01_sgRNA_preprocessing_growth"
newlibrary=pd.read_csv(output + "/00_processed_sgRNAlibrary.tsv", sep = "\t")  
 
def procfile(newlibrary):
    processedfile=newlibrary[['guide', 'geneid']]
    processedfile = processedfile.rename({'guide': 'seq', 'geneid': 'geneid'}, axis = 1)
    processedfile.to_csv(output + "/01_FeatureEngg_input.tsv", sep= '\t',index = False)
procfile(newlibrary)

 

sqs=list()
def procfile2(newlibrary): # keep the guides targeting genes at the coding strand only  
    processedfile=newlibrary[(newlibrary['intergenic']==0.0)] 
    processedfile=processedfile.reset_index()
    for i in range(len(processedfile)):
        if str(processedfile['guide'][i]) not in str(processedfile['sequence_30nt'][i]): # check if the guide sequences are in sequence_30 nt or not
            sqs.append(processedfile['guide'][i])
    processedfile=processedfile[~(processedfile['guide'].isin(sqs))] # remove the guides which are not found in sequence 30nt
    processedfile=processedfile[processedfile['geneid'].str.contains("^b")] #locus id with b...
    processedfile['geneid'].replace('-.*$', '', inplace=True, regex=True)# replace the second fragment of locus id -.. with ''
    processedfile=processedfile[['guide', 'geneid']]
    processedfile = processedfile.rename({'guide': 'seq', 'geneid': 'geneid'}, axis = 1)
    processedfile.to_csv(output + "/02_FeatureEngg_input.tsv", sep= '\t', index = False)

procfile2(newlibrary)
