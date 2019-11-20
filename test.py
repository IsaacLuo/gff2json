import argparse
parser = argparse.ArgumentParser(description='convert gff file format to json')

parser.add_argument('--fasta',
                    help='user external fasta file')

parser.add_argument('--out',
                    help='specify the output name')

parser.add_argument('gff_file', help='gff file')

args = parser.parse_args()
print(args.fasta, args.out, args.gff_file)