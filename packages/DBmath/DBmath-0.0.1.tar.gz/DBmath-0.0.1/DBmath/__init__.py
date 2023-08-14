def AddNum(a, b):
    num = a + b
    return num

def MinusNum(a, b):
    num = a - b
    return num

def TimesNum(a, b):
    num = a * b
    return num

def DivideNum(a, b):
    num = a / b
    return num

def Squared(a):
    num = a ** 2
    return num

def Cubed(a):
    num = a ** 3
    return num

def Power(a, b):
    num = a ** b
    return num

def ListCommands():
    print("commands:")
    print("bettermath.AddNum(num1, num2)")
    print("bettermath.MinusNum(num1, num2)")
    print("bettermath.TimesNum(num1, num2)")
    print("bettermath.DivideNum(num1, num2)")
    print("bettermath.Squared(num)")
    print("bettermath.Cubed(num)")
    print("bettermath.Power(num, powerlevel)")