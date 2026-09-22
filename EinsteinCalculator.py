def isfloat(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def calculator(operations):
    tokens = ['0','+'] #token  is operator or operand

    #splitting
    for ch in operations:
        if ch.isdigit():
            if tokens[-1].isdigit() or isfloat(tokens[-1]):
                tokens[-1]=str(int(tokens[-1])*10+int(ch))
                continue
        tokens.append(ch)
    
    print("Q.",operations)

    #calculation
    while len(tokens)>1:
        operand1=float(tokens[0])
        operand2=float(tokens[2])
        if tokens[1] == '+':
            result=operand1+operand2
        elif tokens[1] == '-':
            result=operand1-operand2
        elif tokens[1] == '/':
            result=operand1/operand2
        elif tokens[1] == '*':
            result=operand1*operand2
        elif tokens[1] == '%':
            result=operand1%operand2
        tokens.pop(0)
        tokens.pop(1)
        tokens[0]=str(result)
    print("A.",tokens[0])
#ELYSIUM
#MAIN
calculator("2*65-94*21/643-12+94/2100")
