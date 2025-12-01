def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b
def power(a, b): return a ** b
def mod(a, b): return a % b

ops = {
    '+': add, '-': sub, '*': mul, '/': div, '**': power, '%': mod
}

def parse_and_calc(expr: str):
    return eval(expr, {"__builtins__":{}})

def main():
    print("Simple CLI Calculator. Type 'quit' to exit.")
    while True:
        s = input("expr> ").strip()
        if s.lower() in ('q','quit','exit'):
            break
        if not s:
            continue
        try:
            result = parse_and_calc(s)
            print("= ", result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
