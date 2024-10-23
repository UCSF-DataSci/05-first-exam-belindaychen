import sys 
import argparse

#create translation table for DNA complement
def setup_complement_table():
    bases = {'A': 'T', 'T':'A', 'C': 'G', 'G':'C',
             'a':'t', 't':'a', 'c':'g', 'g':'c'}
    return str.maketrans(bases)

#create the complement table 
complement_table = setup_complement_table()

#return complement of dna sequence
def complement(sequence):
    return sequence.translate(complement_table)

#returns reverse of sequence 
def reverse(sequence):
    return sequence[::-1]

#return the reverse complement
def reverse_complement(sequence):
    return reverse(complement(sequence))

#validate that the sequence only contains valid DNA bases 
def validate_sequence(sequence):
    valid_bases = set('ATCGatcg')
    if not all(base in valid_bases for base in sequence):
        raise ValueError("Invalid DNA sequence, contains bases other than A, T, C, and G.")
    return sequence 

#parse command line arguments 
def parse_arguments():
    parser = argparse.ArgumentParser(description="Perform DNA sequence operations.")
    parser.add_argument('sequence', type=str, help='DNA sequence to process')
    return parser.parse_args


def main():
    try:
        args = parse_arguments()
        sequence = validate_sequence(sys.argv[1])

        #perform operations and print results 
        print(f"Original sequence: {sequence}")
        print(f"Complement: {complement(sequence)}")
        print(f"Reverse: {reverse(sequence)}")
        print(f"Reverse complement: {reverse_complement(sequence)}")
    except ValueError as e: 
        print(f"Error: {str(e)}")
        sys.exit(1)
    except Exception as e: 
        print(f"An unexpected error has occured: {str(e)}")
        sys.exit(1)
    
if __name__ == "__main__":
    main()


