weight = input('请输入重量：')
if weight[-2:] == 'kg':
  exchange = (eval(weight[0:-1])) * 2.2046
  print('对应的英制重量为｛:.3f｝磅'.format(exchange))
elif weight[-2:] == 'pd':
  exchange = (eval(weight[0:-1])) / 2.2046
  print('对应的公制重量为｛:.3f｝公斤'.format(exchange))
else:
  print('输入错误')

