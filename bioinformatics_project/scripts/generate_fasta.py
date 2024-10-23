import random 
import textwrap 
import os 

#generate random DNA sequence of a specified length
def generate_random_dna(length):
    nucleotides = ["A", "C", "G", "T"]
    return ''.join(random.choice(nucleotides) for i in range(length))

#save DNA sequence in FASTA format with specified line length + create data directory if it doesn't exist 
def save_fasta(sequence, filename, line_length = 80):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    #use textwrap to format sequences into lines 
    formatted = textwrap.fill(sequence, width=line_length)

    #write to file 
    with open(filename, 'w') as f: 
        f.write(formatted)

def main(): 
    sequence_length = 1000000
    output_file = os.path.join("../data", "random_sequence.fasta")

    try: 
        dna_sequence = generate_random_dna(sequence_length)
        save_fasta(dna_sequence, output_file)

        print(f"Random DNA sequence generated and saved to {output_file}")
    except Exception as e: 
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
