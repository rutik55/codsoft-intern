import sys
def menu():
        print("*" * 50)
        print("\tWelcome To Calculator")
        print("*" * 50)
        print("\t1.ADDITION")
        print("\t2.SUBSTRACTION")
        print("\t3.MULTIPLICATION")
        print("\t4.DIVISION")
        print("\t5.MODULO DIVISION")
        print("\t6.EXPONENTIATION")
        print("\t7.EXIT")
        print("=" * 50)

def add():
        print("ENTER TWO NUMBERS FOR ADDITION:")
        a,b=float(input()),float(input())
        print("Addition of ({} + {})={}".format(a,b,a+b))
def sub():
    print("ENTER TWO NUMBERS FOR SUBSTRACTION:")
    a,b=float(input()),float(input())
    print("Subtraction of ({} - {})={}".format(a,b,a-b))
def mul():
    print("ENTER TWO NUMBERS FOR MULTIPLICATION:")
    a,b=float(input()),float(input())
    print("Multiplication of ({} * {})={}".format(a,b,a*b))
def div():
    print("ENTER TWO NUMBERS FOR DIVISION:")
    a,b=float(input()),float(input())
    print("Floor Division of ({} / {})={}".format(a,b,a//b))
def mod():
    print("ENTER TWO NUMBERS FOR MOD DIVISION:")
    a,b=float(input()),float(input())
    print("Mod Division of ({} % {})={}".format(a,b,a%b))
def expop():
    a,b=float(input("Enter Base:")),float(input("Enter Power:"))
    print("Power of ({},{})={}".format(a,b,a**b))

while(True):
     menu()
     d=int(input("Enter Your Choice:"))
     print("="*50)
     match(d):
         case 1:
             add()
         case 2:
             sub()
         case 3:
             mul()
         case 4:
             div()
         case 5:
             mod()
         case 6:
             expop()
         case 7:
             print("Thanks for using this Calculator")
             sys.exit()
         case _:
          print("Your selection of operation is wrong----Please try again")
