
def buyComputer(balance):
    computer = 500;
    if balance < computer:
        print("I don't have enough for this computer!");
    elif balance >= computer:
        print("I can buy this computer!");
    else:
        print("Something went wrong...")    

buyComputer(500);
buyComputer(400);

#While Loop

x = 0;
while (x<5):
    print(x);
    x+=1;

#For Loop

for x in range(1,10):
    print(x);