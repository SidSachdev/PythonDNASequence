#!/usr/bin/env python3

"""
Zymergen Coding Challenge
"""

__author__ = "Sid Sachdev"
__email__ = "sid.sachdev9@icloud.com"

import sys, getopt
from Bio import SeqIO


# Accepting arguments from the command line
def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('USAGE: fasta.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    # Creating a new output and input file with the desired name from the command line.
    inputFileName = inputfile
    outputFileName = outputfile

    # Opening the file
    outputFile = open(outputFileName+'.csv', 'w')

    def gc_content(sequence, desc):
        """
       :param sequence: The Sequence of the DNA as a parameter
       :param desc: The description (NAME) of the the sequence
       :return: The returned output will directly append to a CSV file
       """
        # This section will calculate the GC Content
        gc_count = sequence.count("G") + sequence.count("C")
        gc_fraction = float(gc_count) / len(sequence)
        gcPercentage = str(100 * gc_fraction)

        # This section will handle the cases of the names.
        # The join function with the split function will handle the additional/extra spaces
        # The replace function will replace the spaces with the required underscores
        name = " ".join(desc.split()).replace(" ", "_")

        # This section will write to the output file.
        final = name + ',' + gcPercentage + '\n'
        outputFile.write(final)

    # Creating the record of each individual sequence
    # Calling the function above
    # Using the system call to allow parameters to accept different types of fasta files

    for record in SeqIO.parse(inputFileName+'.fa', "fasta"):
        gc_content(record.seq, record.description)


if __name__ == "__main__":
    main(sys.argv[1:])
