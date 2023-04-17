def say_hello_n_times(n: int) -> str:
    greeting = ""
    for i in range(0, n):
        greeting += "hello\n"
    return greeting

amount = int(input("введите количество раз: "))
print(say_hello_n_times(13451))