print('Enter an integer')
def validate():
 num = input()
 try:
  num = int(num)
  print("Thank you")
 except ValueError:
  print("It must be an integer")
  validate()


validate()
