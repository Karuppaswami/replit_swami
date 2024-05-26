operator = { 
  "+" : "add", 
  "-" : "sub", 
  "*" : "mul", 
  "/" : "div", 
  "%" : "mod"
}

def add(n1 , n2):
  return n1 + n2
def sub(n1 , n2):
  return n1 - n2
def mul(n1 , n2):
  return n1 * n2
def div(n1 , n2):
  return n1 / n2
def div(n1 , n2):
  return n1 % n2

n1 = int(input("Enter the first number:" ))
n2 = int(input("Enter the secound number: "))

for symbol  in operator:
  print(symbol)
operation_symbol = input("Pick an operation from above line: ")
calculation_function = operator[operation_symbol]
print(calculation_function)
answer = calculation_function(n1,n2)
print(f"{n1} {operation_symbol} {n2} = {answer}")
