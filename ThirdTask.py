def decoratorFunc(functionDecorate):
    def wrapperFunc(n):
        print(n)
        functionDecorate(n)
    return wrapperFunc

def untouchable_function(n):
    if n == 0:
        return
    untouchable_function(n-1)

untouchable_function = decoratorFunc(untouchable_function)

if __name__ == '__main__':
    untouchable_function(100)