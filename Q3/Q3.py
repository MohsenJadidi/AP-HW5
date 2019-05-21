import itertools

A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), ('1', '2', '3', '4', '5')))
A1 = range(10)
A2 = [i for i in A1 if i in A0]
A3 = sorted(A0[i] for i in A0)
A4 = [[i, i*i] for i in A1]

# First way
# for f in itertools.chain(A0, A1, A2, A3, A4):
#     print(f, end=', ')

# Second way
global_dict = globals().copy()
for key in global_dict:
    if key.startswith('A'):
        print(key, ' is ', global_dict[key])

