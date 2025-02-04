print("hello world");

balance = 25;
computer = 800;

if balance < computer:
    print("I don't have enough for this computer!")
    balance += 800;
    print(balance);
else:
    print("I can purchase this computer!")

def say_hello(text):
    print(text);    

say_hello("This is the text from the say hello function");