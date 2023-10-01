# Use randint to generate random cards. 
from random import randint 
first_card = randint(1, 13)

if first_card == 1:
  card_name = "Ace"
elif first_card == 11:
  card_name = "Jack"
elif first_card == 12:
  card_name = "Queen"
elif first_card == 13:
  card_name = "King"
else:
  card_name = str(first_card)

if first_card == 11 or first_card == 12 or first_card == 13:
  card_value1 = 10
elif first_card == 1:
  card_value1 = 11
else:
  card_value1 = first_card 

if first_card == 1 or first_card == 8:
  drew_prefix = 'Drew an '
else:
  drew_prefix = 'Drew a '

if first_card < 1 or first_card > 13:
  print('BAD CARD')
else:
  print(drew_prefix + card_name)

second_card = randint(1, 13)

if second_card == 1:
  card_name = "Ace"
elif second_card == 11:
  card_name = "Jack"
elif second_card == 12:
  card_name = "Queen"
elif second_card == 13:
  card_name = "King"
else:
  card_name = str(second_card)

if second_card == 11 or second_card == 12 or second_card == 13:
  card_value2 = 10
elif second_card == 1:
  card_value2 = 11
else:
  card_value2 = second_card

if second_card == 1 or second_card == 8:
  drew_prefix = 'Drew an '
else:
  drew_prefix = 'Drew a '

if second_card < 1 or second_card > 13:
  print('BAD CARD')
else:
  print(drew_prefix + card_name)

hand_value = card_value1 + card_value2

if hand_value > 21:
  print("Final hand: " + str(hand_value) + ".")
  print("BUST.")

elif hand_value == 21:
  print("Final hand: " + str(hand_value) + ".")
  print("BLACKJACK!")

while hand_value < 21:
  next_card = input("You have " + str(hand_value) + ". Hit (y/n)? ")


  if next_card == "y":
    next_card = randint(1, 13)

    if next_card == 1:
      card_name = "Ace"
    elif next_card == 11:
      card_name = "Jack"
    elif next_card == 12:
      card_name = "Queen"
    elif next_card == 13:
      card_name = "King"
    else:
      card_name = str(next_card)

    if next_card == 11 or next_card == 12 or next_card == 13:
      card_value3 = 10
    elif next_card == 1:
      card_value3 = 11
    else:
      card_value3 = next_card

    if next_card == 1 or next_card == 8:
      drew_prefix = 'Drew an '
    else:
      drew_prefix = 'Drew a '
        
    print(drew_prefix + card_name)

    hand_value = hand_value + card_value3


    if hand_value == 21:
      print("Final hand: " + str(hand_value) + ".")
      print("BLACKJACK!")
    elif hand_value > 21:
      print("Final hand: " + str(hand_value) + ".")
      print("BUST.")

  elif next_card == "n":
    print("Final hand: " + str(hand_value) + ".")
    
    if hand_value == 21:
      print("BLACKJACK!")
    elif hand_value > 21:
      print("BUST.")
    hand_value = hand_value + 100

      

  else: 
    print("Sorry I didn't get that.")
