def add(a, b):
    print(a+b)

def sub(a, b):
    print(a-b if a>b else b-a)

def mul(a, b):
    print(a*b)

def div(a, b):
    print("0이 포함되어 있어 계산X" if a == 0 or b == 0 else a/b)

def main():
    operator = int(input("1. 덧셈 2. 뺄셈 3. 곱셈 4. 나눗셈"))
    a = int(input("a를 입력하세요."))
    b = int(input("b를 입력하세요."))

    if operator == 1:
        add(a, b)

    elif operator == 2:
        sub(a, b)

    elif operator == 3:
        mul(a, b)

    elif operator == 4:
        div(a,b)

if __name__ == "__main__":
    main()