import fibo, sys,builtins
# from fibo import fib, fib2
# from fibo import fib as fibonacci

# todo

# 如果经常使用某个函数，可以把它赋值给局部变量：
fib = fibo.fib

for i in sys.path:
    print(i)


print(dir(fib))

print("------------")

if __name__ == '__main__':
    print(fibo.fib(5))
    list = fibo.fib2(5)
    print(list)
    fib(10)
    dir(builtins)
    pass