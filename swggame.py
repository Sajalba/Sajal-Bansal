import random
print("\n \t\t Welcome to Snake, Water, Gun Game \n")
totalcoice = int(input("Enter Total Number Of Attempts : "))
human=0
computer=0
i=1


while(i<=totalcoice):
    c1 = ["Snake", "Water", "Gun"]
    c = random.choice(c1)
    u1 = input("Enter Your Input : ")
    u = u1.capitalize()
    print(c)
    l=0

    if u=="Snake" and c=="Water":
        print("Human Win")
        l=totalcoice-i
        print(f"Total Left Attempts {l} \n")
        human=human+1
    elif u=="Water" and c=="Snake":
        print("Computer Win")
        l=totalcoice-i
        print(f"Total Left Attempts {l} \n" )
        computer=computer+1


    elif u=="Gun" and c=="Snake":
        print("Human Win")
        l=totalcoice-i
        print(f"Total Left Attempts {l} \n" )
        human=human+1
    elif u=="Snake" and c=="Gun":
        print("Computer Win")
        l=totalcoice-i
        print(f"Total Left Attempts {l} \n" )
        computer=computer+1


    elif u=="Water" and c=="Gun":
        print("Human Win")
        l=totalcoice-i
        print(f"Total Left Attempts {l} \n" )
        human=human+1
    elif u=="Gun" and c=="Water":
        print("Computer Win")
        l=totalcoice-i
        print(f"Total Left Attempts {l} \n" )
        computer=computer+1

    elif u==c:
        print("No Combination")
        l = totalcoice-i
        print(f"Total Left Attempts {l} \n")

    elif l==totalcoice-i:
        print("\nGame Over")

    else:
        print("Invalid Input")
        l = totalcoice - i
        print(f"Total Left Attempts {l} \n")

    i=i+1

print("Human Points : ",human)
print("Computer Points : ",computer)
if human>computer:
    print(f"Human Wins By {human} Poins")
elif computer>human:
    print(f"Computer Wins By {computer-human} Points")
else:
    print("Both Are Equal")