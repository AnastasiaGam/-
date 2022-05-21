class Calculator:
    while True:
        s = input("Введите операцию, которую хотите сделать или введите 0 для выхода: ")
        if s in ('+','-','*','/','^','%'):
            a = int(input("Введите первое число: "))
            b = int(input("Введите второе число: "))

            def __init__(self, a, b):
                self.a = a
                self.b = b
            if s == "+":
                def plus(self, a, b): return a + b
                print(a + b)
            elif s == "-":
                def minus(self, a, b): return a - b
                print(a - b)
            elif s == "*":
                def proisv(self, a, b): return a * b
                print(a * b)
            elif s == "/":
                def delen(self, a, b):
                    return a / b
                try:
                    r = a / b
                except ZeroDivisionError:
                    r = 0
                    print('Произошла ошибка: деление на ноль')
                else:
                    print(a / b)
            elif s == "%":
                def q(self, a, b): return a % b
                print(a % b)

            elif s == "^":
                def w(self, a, b): return a ** b
                print(a ** b)
        else:
            s == 0
            break