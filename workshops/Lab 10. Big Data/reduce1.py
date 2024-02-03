import sys

cur_key = None
cur_val = None

for line in sys.stdin:
    key,value = line.strip().split('\t')
    
    if key != cur_key:
        if cur_key:
            print(cur_key+'\t'+str(cur_val))

        cur_key = key
        cur_val = float(value)
    else:
        cur_val += float(value)
        
if cur_key:
    print(cur_key+'\t'+str(cur_val))
