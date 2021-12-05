# code for explaining python decorators
def decor1(func):
  print("Inside decor1")
  def inner():
    print("Inside decor1_inner")
    x = func()
    return 2 * x
  return inner

def decor2(func):
  print("Inside decor2")
  def inner():
    print("Inside decor2_inner")
    x = func()
    return x * x
  return inner

@decor2
@decor1
def num():
  print("Inside num")
  return 10

print(num())


## BELOW IS THE OUTPUT WHEN "print(num())" IS COMMENTED
Inside decor1
Inside decor2

## BELOW IS THE OUTPUT WHEN "print(num())" IS NOT COMMENTED
Inside decor1
Inside decor2
Inside decor2_inner
Inside decor1_inner
Inside num
400
