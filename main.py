weight = input()
if weight[-2:] == 'kg':
    exchange = eval(weight[0:-2]) * 2.2046
    print('对应的英制重量为22.046磅')
elif weight[-2:] == 'pd':
    exchange = eval(weight[0:-2]) / 2.2046
    print('对应的公制重量为4.535公斤')


