from words1 import words
import random
w=random.choice(words).upper()
cpu,sui=[],''

for i in range(len(w)):
    cpu.append("_")

def hey(): 
    global sui
    for i in range(len(cpu)):
        print(cpu[i],end='')
        sui+=cpu[i]
    print()
hey()

chance=5
print("This word has",len(w),"words.")
while chance!=0:
    if sui!=w:
        play=(input("Enter a string:")).strip()
        play=play.upper()
        if len(play)==len(w):
            chance-=1
            for i in range(len(play)):
                if play[i]==w[i]:
                    cpu[i]=play[i].upper()
                elif play[i] in w or (play[i] in cpu and w.count(play[i])>1):
                    print(play[i],"is in the word, but not in the",(i+1),"position.")
            print()
            
            sui=''
            hey()
            print("You have",chance,"lives remaining.")
        else:
            print("Try again! That word does not have",len(w),"letters.")
            print()
    if sui==w:
        print("That's right! You won!")
        break
if chance==0 and sui!=w:
    print("Sorry! You have no lives remaining. The word was",w)

                
