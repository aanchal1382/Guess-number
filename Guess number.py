# 1st Approach

n=18
guess=9
print("No. of guesses is 9")
while (guess>0):
    number=int(input("Enter your number\n"))
    if number<18:
        print("Your number is smaller!!Try some big number")
        print(guess-1,"Guesses left\n")
    elif number>18:
        print("Your number is larger!!Try some small number")
        print(guess-1,"Guesses left\n")
    else:
        print("You entered the correct number\n")
        print("You wonnn!!!\n")
        print("you took",int(10-(guess)),
        "guesses to win")   
    guess=guess-1
 
    if (guess==0):
        print("Game Over")
        break






# # 2nd Approach
# n = 56
# i=0
# print("You have 10 gueses")
# while(1):
#     i=i+1
#     print("Guess No. ",i)
#     print("Guess the number")
#     x=int(input())
#     if x<n:
#         print(x," is lesser than the number!! Try Again!")
#     elif x==n:
#         print("You Won!! This is the number")
#         break
#     else:
#         print(x," is larger than the number!! Try Again!")
#     if i>10:
#         print("Game Over")
#         break


