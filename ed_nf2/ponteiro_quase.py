a = [42]      # lista com um elemento
b = a         # b referencia o mesmo objeto
print(a[0])   # 42
b[0] = 100
print(a[0])   # 100, alteração reflete em a
