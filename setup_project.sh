#!/bin/bash

#Create main project directory 
mkdir -p bioinformatics_project

#Change into project directory 
cd bioinformatics_project

#Create subdirectories 
mkdir -p data scripts results 

#Create empty Python files in the scripts directory
touch scripts/generate_fasta.py
touch scripts/dna_operations.py
touch scripts/find_cutsites.py

#Create empty files in results and data directories 
touch results/cutsite_summary.txt
touch data/random_sequence.fasta

#Create README.md with project structure description
touch results/cutsite_summary.txt
touch data/random_sequence.fasta

#Create README.md with project structure description 
cat > README.md << 'EOF'
#DS217 Midterm Bioinformatics Project
This project contains three directories: data, scripts, and results." 

## Project Structure

- `data/`: Contains input data files
  - random_sequence.fasta: Input FASTA sequence file
  
- `scripts/`: Contains analysis scripts
  - generate_fasta.py: Script to generate random DNA sequences
  - dna_operations.py: Core DNA manipulation functions
  - find_cutsites.py: Script to identify restriction enzyme cut sites
  
- `results/`: Contains analysis outputs
  - cutsite_summary.txt: Summary of identified cut sites

## Usage

The scripts in this project are designed to work with DNA sequence data and identify
restriction enzyme cut sites. Each script can be run independently or as part of a
complete workflow.
EOF

#Print success message and directory structure
echo "Project directory structure was created successfully!"
if command -v tree &> tree /dev/null; then
    tree
else 
    echo "bioinformatics_project/"
    echo "├── data/"
    echo "│   └── random_sequence.fasta"
    echo "├── scripts/"
    echo "│   ├── generate_fasta.py"
    echo "│   ├── dna_operations.py"
    echo "│   └── find_cutsites.py"
    echo "├── results/"
    echo "│   └── cutsite_summary.txt"
    echo "└── README.md"

chmod +x setup_project.sh
