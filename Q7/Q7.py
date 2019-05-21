

# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# A = [3, 4, 1, 37, 21, 18, 23, 21, 27, 22, 43, 21]
# A = set(input('Enter : '))
# print(' '.join(set([str(i) for i in input().split() if ((i % 6 == 0) and ((A.index(i)+1) % 6) == 0)])))

print(' '.join(list(filter((lambda x: int(x) % 6 == 0), input().split()))))


#print(' '.join(list(set([i for i in input().split() if (int(i) % 6 == 0)]))))

