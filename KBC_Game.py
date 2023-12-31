#KBC game 
questions=["who is math hod jnec","who is phy hod jnec","which collage is nearer to IIRC"]
answers=["lomte sir,kranti mam,SOET"]

welcome="* Welcome to KBC Made by Akash *"
welcome.upper
print(welcome.upper().center(110))
n=0
for n in range(3):
    print("Question Number",(n+1),"is here",sep=None,end=None)
    print("Q. ",questions[n],sep=None,end=None)
    print("\n\n\noption 1 : lomte sir\noption 2 : kranti zhakde\noption 3 : SOET \noption 4 : None \n\n\nenter anser as 1 or 2 or 3 or 4",sep=None,end=None)
    gamans=int(input())
    if gamans==n+1:
        money=1000*(n+1)
        print("Your answer is Correct ,Your earnerd money is ",money,"\n\n",sep=None,end=None)
        n=n+1
    else:
        print("your answer is wrong You lost the game",sep=None,end=None)
        exit()



