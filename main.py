def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Error: division by zero"
    return a/b
def power(a,b):
    return a**b
def modulus(a,b):
    return a%b
ops = {
    '+': add, '-': subtract, '*': multiply, '/': divide, '**': power, '%': modulus
}

def parse_and_calculate(expression:str):
    return eval(expression,{__builtins__:{}})
def main():
    print("Simple CLI Calculator. Type 'quit' to exit.")
    while True:
        s = input("expression> ").strip()

        if s.lower() in ('q', 'quit', 'exit'):
            print("Exiting calculator. Goodbye!")
            break
        
        if not s:
            continue

        try:
            result = parse_and_calculate(s)
            print("= ", result)
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()

   