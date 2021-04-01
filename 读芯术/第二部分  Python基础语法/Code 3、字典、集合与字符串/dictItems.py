data = dict(name='张三', age=18, sex='M')
print(data['name'])                         # 使用“键”作为下标，访问“值”
print(data.get('age'))
print(data.get('address', '不存在这个键'))   # “键”不存在，返回默认值
print(list(data))                           # 把所有的“键”转换为列表
print(list(data.values()))                  # 把所有的“值”转换为列表
print(list(data.items()))                   # 把所有的元素转换为列表
for key, value in data.items():             # 遍历字典的“键：值”元素
    print(key, value, sep='\t')



# 字典元素操作
sock = {'IP': '127.0.0.1', 'port': 80}
sock['port'] = 8080                  # 修改已有元素的“值”
sock['protocol'] = 'TCP'             # 增加新元素
print(sock)

sock = {'IP': '127.0.0.1', 'port': 80}
# 更新了一个元素的“值”，增加了一个新元素
sock.update({'IP':'192.168.9.62', 'protocol':'TCP'})
print(sock)

sock = {'IP': '192.168.9.62', 'port': 80, 'protocol': 'TCP'}
print(sock.pop('IP'))           # 删除并返回指定“键”的元素
print(sock.popitem())           # 删除并返回一个元素
del sock['port']                # 删除指定“键”的元素
print(sock)

