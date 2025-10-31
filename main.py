'''
---------------------------------------------------------------
rules
     ->rock will win  against scinssor
     ->scinssor win against paper
     ->paper win against rock
     #reprsesinting in number
     rock=0
     paper=1
     scissor=2
     ----------------------------------------------------------------
'''
import random
print('''
Ente the number according to your choice
0 ->Rock ✊
1  -> Paper ✋
2 -> scissor ✌️
''')
Rock,Paper,scissor,Winer,Loser,wrongchoice=('✊',"✋","✌️",'✅','❌','❓')
Game_list=[Rock,Paper,scissor]


while True:
   user_choice=int(input("Enter your choce:  "))
   if user_choice >2 or user_choice<0:
      print(f"{wrongchoice} you have entered wrong number.Please entered the correct choice ")
   else:
      print(f"Your choice is {Game_list[user_choice]}")
      computer_chice=random.randint(0,2)
      print(f"Computer chioce is{Game_list[computer_chice]}")
#identifing the winner

      if user_choice >2 or user_choice<0:
        print("you have entered wrong number.Please entered the c1"
              "orrect choice")
      elif user_choice==computer_chice:
        print("It's a draw")
      elif user_choice == 0 and computer_chice == 2:
        print(f"{Winer} You win.Keep it up")
      elif user_choice == 2 and computer_chice == 0:
        print(f"{Loser} You lost .Try again")
      elif user_choice > computer_chice:
        print(f" {Winer} You win.Keep it up")
      elif computer_chice < user_choice:
        print(f"{Loser} You lost .Try again")
