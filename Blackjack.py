import random
def logo():
  print ('''
  _     _            _    _            _    
  | |   | |          | |  (_)          | |   
  | |__ | | __ _  ___| | ___  __ _  ___| | __
  | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
  | |_) | | (_| | (__|   <| | (_| | (__|   < 
  |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                        _/ |                
                        |__/          
  ''')
def draw_card():
  return random.choice(cards_deck)

def cal_score(cards):
  global cards_deck
  score = 0
  cards_score = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  if 'A' in cards and ('J'in cards or 'Q'in cards or 'K'in cards or '10' in cards) and len(cards) == 2:
    return 0
  else :
    for i in cards:
      score+= cards_score[cards_deck.index(i)]
    if score > 21 and 'A' in cards:
      score-=10
  return score

def check_score(p,c):
    if p > 21 and c > 21:
      print ("you lose! Both went over.")
    if c == p:
      print ("Its a Draw.")
    elif c > 21:
      print("you win!. Computer went over.")
    elif p > 21:
      print("you lose!. you went over.")
    if c == 0:
       print ("Black Jack! Computer wins! ")
    elif p == 0:
       print ("Black Jack! You win! ")
    elif c > p :
      print("Computer Wins!")
    elif c < p :
      print("You win!")
    

def game_on():
  play = True
  logo()
  player_c = []
  comp_c = [] 
  for i in range (2):
    player_c.append(draw_card())
    comp_c.append(draw_card())
  while play:
     pla_score = cal_score(player_c)
     comp_score = cal_score(comp_c)
     print (f"   Your cards : {player_c}, current score : {pla_score}")
     print(f"Computer's first card : {comp_c[0]}")
  
     if pla_score == 0 or comp_score == 0 or pla_score > 21:
      play = False
     else: 
        draw=input("Type 'y' to get another card, type n to pass : ").lower()
        if draw == 'y' :
          player_c.append(draw_card())
        else: 
          play = False
     while comp_score != 0 and comp_score <= 17:
        comp_c.append(draw_card())
        comp_score = cal_score(comp_c)

  print(f"Your final hand: {player_c}, final score : {pla_score}")
  print(f"Computer final hand: {comp_c}, final score : {comp_score}")
  check_score(pla_score,comp_score)
  
if __name__ == '__main__':
  cards_deck = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
  choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ").lower()
  if choice == 'y':
    game_on()
