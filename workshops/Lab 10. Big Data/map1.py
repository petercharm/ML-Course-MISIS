import sys

for line in sys.stdin:
    line = line.strip().split('\t')
    print(line[1]+'\t'+line[2])