
def fib(n):    # 打印小于 n 的斐波那契数列
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fibx3(n):  # 返回斐波那契数组直到 n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # 见下
        a, b = b, a+b
    return result

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])



if __name__ == '__main__':
    # fib(2000)
    # result =fibx3(100)
    # print(result)
    # result = ask_ok('Do you really want to quit?')
    # print(result)
    # ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

    cheeseshop("Limburger", "It's very runny, sir.",
               "It's really very, VERY runny, sir.",
               shopkeeper="Michael Palin",
               client="John Cleese",
               sketch="Cheese Shop Sketch")
