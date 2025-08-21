#--------------------------------#
#          FUNCTIONS
#--------------------------------# 


#costum function for creating the DNA/RNA sequences (according to users' selected option) and appending them in a list
def dna_manipulator(dna, user_selected_option):
    def complement(dna, user_selected_option):
        result = []
        for nucleotide in dna:
            if nucleotide == "A":
                if user_selected_option == 4:
                    result.append("U")
                else:
                    result.append("T")
            elif nucleotide == "T":
                result.append("A")
            elif nucleotide == "C":
                result.append("G")
            elif nucleotide == ("G"):
                result.append("C")
        return "".join(result)
              

    if user_selected_option == 1:
        manipulated_dna = complement(dna, user_selected_option)
    
    elif user_selected_option == 2:
        manipulated_dna = dna[::-1]
        
    elif user_selected_option == 3:
        reverse_dna = dna[::-1]
        manipulated_dna = complement (reverse_dna, user_selected_option)
        
        
    elif user_selected_option == 4:
        manipulated_dna = complement(dna, user_selected_option)
        
    return manipulated_dna        

#costum function for opening the given fasta file, processing the DNA sequences and returning a list of the produced sequences
def process_fasta_file (infile, user_selected_option):
    with open(infile, "r") as file:
        infile_contents = file.readlines()
    outfile_contents = []
    for line in infile_contents:
        if line.startswith(">"):
            outfile_contents.append(line)
        else:
            sample = line.strip("\n")
            sample_manipulated = dna_manipulator(sample, user_selected_option)
            sample_manipulated_n = sample_manipulated + "\n"
            outfile_contents.append(sample_manipulated_n)
    return outfile_contents
    
#costum function for creating fasta files from the lists of the produced sequences
def filename(infile, user_selected_option):
    if user_selected_option == 1:
        outfile_name = infile.strip(".fasta") + "_complement.fasta"
    elif user_selected_option == 2:
        outfile_name = infile.strip(".fasta") + "_reverse.fasta"
    elif user_selected_option == 3:
        outfile_name = infile.strip(".fasta") + "_reverse_complement.fasta"
    elif user_selected_option == 4:
        outfile_name = infile.strip(".fasta") + "_complement_mRNA.fasta"
        
        
    with open(outfile_name, "w") as outfile: 
        outfile.writelines(process_fasta_file (infile, user_selected_option))

#--------------------------------#
#            INPUTS
#--------------------------------#

#asking the user for the fasta file they wish to process
infile = input("Please enter the name of a fasta file that you wish to process: ")

#asking the user the manipulation they wish to do
user_selected_option = int(input("""

Please enter the manipulation that you wish to perform:
    Type 1 for the complement DNA sequences.
    Type 2 for the reverse DNA sequences.
    Type 3 for the reverse complement DNA sequences.
    Type 4 for the complement mRNA sequences.
    Type 9 for all of the above conversions.

"""))

#--------------------------------#
#             CODE
#--------------------------------#  

#performing the task
if user_selected_option != 9: 
    filename(infile, user_selected_option)
else:
    filename(infile,1)
    filename(infile,2)
    filename(infile,3)
    filename(infile,4)

print("Process completed!")
