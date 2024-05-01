def A():
    print("Hello")
def B():
    print("How are you")
def C():
    print("Hi")

x = input("Please enter in capital A, B, or C> ")
if x == "A":
    A()
if x == "B":
    B()
if x == "C":
    C()
else:
    print("You've entere an incorrect value")