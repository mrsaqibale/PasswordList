import subprocess
import time
input_file = '../in.txt'
output_file = 'passList.txt'

def commitMe(line):
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', f'Automated commit: {line}'])
def commit_and_push(line):
    with open(output_file, 'a') as outfile:
        outfile.write(line)
        commitMe(line)
            
with open(input_file, 'r') as infile:
    for i in range(5166):
        line = infile.readline()
        commit_and_push(line)