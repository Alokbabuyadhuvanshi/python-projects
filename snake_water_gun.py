import random
x=["s","w","g"]
print("Welcome in Snake-Gun-Water game")
l=int(input("How many rounds you want to play:-"))
print("Enter your weapon as:\ns = snake \nw = water \ng = gun \nchoose any one ")
round=1
your_points=0
computer_points=0
while(l>=round):
    print("Round:-",round)
    rc=random.choice(x)
    e=input("Enter your weapon:-")
    print("computer weapon:-",rc)
    if rc==e:
        print("Draw")
        your_points+=1
        computer_points+=1
        print("your_point:-",your_points)
        print("computer_point:-",computer_points)
    elif rc=="s" and e=="g":
        print("you get two point")
        your_points+=2
        print("your_points:-",your_points)
        print("computer_point:-",computer_points)
    elif rc=="s" and e=="w":
        print("Computer get two point")
        computer_points+=2
        print("computer_point:-",computer_points)
        print("your_point:-",your_points)
    elif rc=="w" and e=="s":
        print("you get two point")
        your_points+=2
        print("your_points:-",your_points)
        print("computer_point:-",computer_points)
    elif rc=="w" and e=="g":
        print("Computer get two point")
        computer_points+=2
        print("computer_point:-",computer_points)
        print("your_point:-",your_points)
    elif rc=="g" and e=="w":
        print("you get two point")
        your_points+=2
        print("your_points:-",your_points)
        print("computer_point:-",computer_points)
    elif rc=="g" and e=="s":
        print("Computer get two point")
        computer_points+=2
        print("computer_point:-",computer_points)
        print("your_point:-",your_points)
    round+=1
print("Computer total points =", computer_points)
print("Your total points =",your_points)
if computer_points>your_points:
    print("So sad you lose the match")
elif your_points>computer_points:
    print("Hurray! you won the match")
else:
    print("Match draw!....play again")


    

