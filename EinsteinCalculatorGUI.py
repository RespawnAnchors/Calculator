import tkinter as tk


def isfloat(text):
    try:
        float(text)
        return True
    except ValueError:
        return False


def calculator(operations):
    tokens = ['0', '+']

    # Splitting
    for ch in operations:
        if ch.isdigit():
            if tokens[-1].isdigit() or isfloat(tokens[-1]):
                tokens[-1] = str(int(tokens[-1]) * 10 + int(ch))
                continue
        tokens.append(ch)

    # Calculation
    while len(tokens) > 1:
        operand1 = float(tokens[0])
        operand2 = float(tokens[2])

        if tokens[1] == '+':
            result = operand1 + operand2
        elif tokens[1] == '-':
            result = operand1 - operand2
        elif tokens[1] == '*':
            result = operand1 * operand2
        elif tokens[1] == '/':
            result = operand1 / operand2
        elif tokens[1] == '%':
            result = operand1 % operand2
        else:
            return "Invalid Operator"

        tokens.pop(0)
        tokens.pop(1)
        tokens[0] = str(result)

    return tokens[0]


def calculate():
    expression = entry.get()

    try:
        answer = calculator(expression)
        result_label.config(text="Answer: " + answer)
    except Exception as e:
        result_label.config(text="Error: " + str(e))


# ---------- GUI ---------- #

root = tk.Tk()
root.title("Calculator")
root.geometry("500x500")

title = tk.Label(root, text="Calculator", font=("Arial", 18))
title.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 16), width=25)
entry.pack()

button = tk.Button(root, text="Calculate", command=calculate)
button.pack(pady=10)

result_label = tk.Label(root, text="Answer:", font=("Arial", 14))
result_label.pack()

root.mainloop()