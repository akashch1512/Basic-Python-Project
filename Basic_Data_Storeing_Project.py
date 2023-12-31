#Program to store and know if it is a boy or girl name
i=100
boy_word=["krishna","shripaad"]
girl_word=["ankita","savita"]
while i!=0:
    print("Welcome To Girl or boy name Suggester")
    word_input=input("please enter any word\n")
    if word_input in boy_word:
        print("he is a boy, good name btw")
    elif word_input in girl_word:
        print("she is a girl ,cute name btw")
    else:
        print("we dont know this please tell if he/she is a girl or boy word")
        print("if you dont want to tell than please type 1 and end the program")
        data_user=input()
        if  data_user!=1:
            if data_user=="girl":
                girl_word.append(word_input)
            elif data_user=="boy":
                boy_word.append(word_input)
            else :
                print("you can either store boy or girl name other words are not accpetable\n\n")
    i=i-1 
    print("\n\n\n")