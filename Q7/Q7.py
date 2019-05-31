import sys
from numpy import asarray, sort, unique

print(' '.join([str(st)for st in list(sort(unique(asarray([int(sys.argv[i+1]) for i in range(len(sys.argv)-1) if (int(sys.argv[i+1]) % 6 == 0) and (i+1) % 6 == 0]))))]))
