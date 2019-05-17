def func(a, b, *args, **keywords):
    print('a :', a, 'b :', b, sep=' ')
    print('*args : ', args)
    print('**keywords : ', keywords)


func(31, 'str1', 546, 464, 'str2', [1, 1], d=1, s='str3')
