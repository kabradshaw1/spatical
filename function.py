def f1(x):
  return 2*x +1

def f2(x):
  x = x + 1
  return x*2 + 1

x = 1
print("f1 = ", f1(x))
print("after f1, x = ", x)
print("f2 = ", f2(x))
print("after f2, x = ", x)