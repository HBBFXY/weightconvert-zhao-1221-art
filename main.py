weight = input('请输入重量：')
if weight[-2:] == 'kg':
  exchange = eval(weight[0:-2]) * 2.2046
  print(f'对应的英制重量为{exchange:.3f}磅')
elif weight[-2:] == 'pd':
  exchange = eval(weight[0:-2]) / 2.2046
  print(f'对应的公制重量为{exchange:.3f}公斤')
else:
  print('输入错误')

