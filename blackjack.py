import random
from art import logo
from replit import clear
cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
player_score,computer_score=0,0
player_cards,computer_cards=[],[]
game=False
end=False

def generate(user, user_score):
  next_card=random.choice(cards)
  if next_card=="A":
    user.append(next_card)
    if user_score<11:
      user_score+=11
    else:
      user_score+=1
  elif next_card=="J" or next_card=="Q" or next_card=="K":
    user.append(next_card)
    user_score+=10
  elif next_card==2 or next_card==3 or next_card==4 or next_card==5 or next_card==6 or next_card==7 or next_card==8 or next_card==9 or next_card==10:
    user.append(next_card)
    user_score+=next_card
  return user_score
      
def clean():
  clear()
  print(logo)
  print("Your hand: ", player_cards, "Current score: ", player_score)
  print("Dealer's hand: ", computer_cards, "Dealer's score: ", computer_score)


while not end:
  if input("Do you want to play a game of blackjack? Y/N ").lower()=="y":
    game=True
    player_score,computer_score=0,0
    player_cards,computer_cards=[],[]
    player_score=generate(player_cards,player_score)
    player_score=generate(player_cards,player_score)
    computer_score=generate(computer_cards,computer_score)
    clean()
  else:
    end=True
  while game:
    continue_select=True
    bust=False
    while continue_select:
      if input("Do you want to draw another card? Y/N ").lower()=="y":
        player_score=generate(player_cards,player_score)
        clean()
        if player_score==21:
          clean()
          continue_select=False
          game=False
        if player_score>21:
          if "A" in player_cards and player_score-10<21:
                player_score-=10
                clean()
          else:
            continue_select=False
            game=False
            bust=True
            print("You went bust! You lose")
      else:
        continue_select=False
    while computer_score<17 and game:
      computer_score=generate(computer_cards,computer_score)
      clean()
  
    if computer_score>21 and not bust:
      if "A" in computer_cards and computer_score-10<21:
            computer_score-=10
            clean()
      else:
        print("Dealer went bust! You won!")
        continue_select=False
        game=False
      
    elif computer_score>player_score and not bust:
      print("You lose")
      game=False
    elif computer_score==player_score and not bust:
      print("Draw")
      game=False
    elif player_score>computer_score and not bust:
      print("You won")
      game=False
  
