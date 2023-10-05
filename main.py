
    
def add(a, b):
    print(a+b)


def sub(a, b):
    if a>b:
        print(a-b)
    else:
        print(b-a)



def mul(a, b):
    print (a * b)



def div(a, b):
    if a == 0:
        print ("a가 0이니 계산 X")
    elif b == 0:
        print ("b가 0이니 계산 X")
    else:
        print (a/b)




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