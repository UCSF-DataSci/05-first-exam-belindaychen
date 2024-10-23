import sys 
import argparse
import os 

#read and clean sequence from FASTA file
def read_fasta(file_path):
    try: 
        with open(file_path, 'r') as f: 
            sequence = ''.join(line.strip() for line in f)
        return sequence
    except Exception as e: 
        raise Exception(f"Error reading FASTA line: {str(e)}")

def find_cut_sites(sequence, cut_site):
    if not isinstance(sequence, str) or not isinstance(cut_site, str):
        raise ValueError("Sequence and cut site must be strings")
    
    if '|' not in cut_site:
        raise ValueError("Cut site must contain '|' to indicate cut position")
    
    # Process cut site
    cut_index = cut_site.find('|')
    target = cut_site.replace('|', '')
    target_length = len(target)
    
    # Find all cut site positions
    cut_positions = []
    for i in range(len(sequence) - target_length + 1):
        if sequence[i:i + target_length] == target:
            cut_positions.append(i + cut_index)
    

    # Find pairs of cut sites that are 80k-120k bases apart
    cut_site_pairs = []
    cut_positions.sort()

    for i in range(0, len(cut_positions)): 
        for j in range(i+1, len(cut_positions)): 
            if ((cut_positions[j] - cut_positions[i]) >= 80000) and ((cut_positions[j] - cut_positions[i]) <= 120000):
                cut_site_pairs.append((cut_positions[i], cut_positions[j])) 
    
    return len(cut_site_pairs), cut_site_pairs[:5], len(cut_positions)

# Example usage:
if __name__ == "__main__":
    dna = read_fasta(sys.argv[1])
    
    try:
        cut_pairs, pairs, count = find_cut_sites(dna, sys.argv[2])
        print(f"Found {cut_pairs} cut site pairs")
        print(f"First 5 pairs: {pairs}")

        output_file = os.path.join("../results", "cutsite_summary.txt")
        with open(output_file, 'w') as f: 
            f.write(f"Analyzing cut site: {sys.argv[2]}\n")
            f.write(f"Total cut site founds: {count}\n")
            f.write(f"Cut site pairs 80-120 kbp apart: {cut_pairs}\n")
            f.write("First 5 pairs: \n")

            for i in range(0, 5):
                f.write(f'{i+1}. {pairs[i][0]} - {pairs[i][1]}\n')
    except ValueError as e:
        print(f"Error: {e}")
