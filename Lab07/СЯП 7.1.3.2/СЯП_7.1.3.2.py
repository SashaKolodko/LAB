from cgitb import strong


def count_punctuation(line):
    punctuation_count = sum(1 for char in line if char in strong.punctuation)
    return punctuation_count
input_file = 'input.txt'
output_file = 'output.txt'
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        count = count_punctuation(line)
        outfile.write(f'{count}\n')
        print("zaconthen")
