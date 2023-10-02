num1=float(input("Enter first number"))
num2=float(input("Enter second number"))
print("Choose an operator /n 1.Add 2.Sub 3.Mul 4.Div.")
n=int(input())
def cal(n):
    match n:
        case 1:
            return num1+num2
        case 2:
            return num1-num2
        case 3:
            return num1*num2
        case 4:
            return num1/num2
        case default:
            return "invalid"
print(cal(n))