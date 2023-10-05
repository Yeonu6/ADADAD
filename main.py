
    
def add(a, b):
    



def sub(a, b):
    



def mul(a, b):




def div(a, b):





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