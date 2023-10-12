import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

TOK_FILE = "token.txt"

card_deck = {
  "Ace_Of_Hearts": 1,
  "Ace_Of_Spades": 1,
  "Ace_Of_Clubs": 1,
  "Ace_Of_Diamonds": 1,
  "Two_Of_Hearts": 2,
  "Two_Of_Diamonds": 2,
  "Two_Of_Clubs": 2,
  "Two_Of_Spades": 2,
  "Three_Of_Hearts": 3,
  "Three_Of_Diamonds": 3,
  "Three_Of_Clubs": 3,
  "Three_Of_Spades": 3,
  "Four_Of_Hearts": 4,
  "Four_Of_Diamonds": 4,
  "Four_Of_Clubs": 4,
  "Four_Of_Spades": 4,
  "Five_Of_Hearts": 5,
  "Five_Of_Diamonds": 5,
  "Five_Of_Clubs": 5,
  "Five_Of_Spades": 5,
  "Six_Of_Hearts": 6,
  "Six_Of_Diamonds": 6,
  "Six_Of_Clubs": 6,
  "Six_Of_Spades": 6,
  "Seven_Of_Hearts": 7,
  "Seven_Of_Diamonds": 7,
  "Seven_Of_Clubs": 7,
  "Seven_Of_Spades": 7,
  "Eight_Of_Hearts": 8,
  "Eight_Of_Diamonds": 8,
  "Eight_Of_Clubs": 8,
  "Eight_Of_Spades": 8,
  "Nine_Of_Hearts": 9,
  "Nine_Of_Diamonds": 9,
  "Nine_Of_Clubs": 9,
  "Nine_Of_Spades": 9,
  "Ten_Of_Hearts": 10,
  "Ten_Of_Diamonds": 10,
  "Ten_Of_Clubs": 10,
  "Ten_Of_Spades": 10,
  "Jack_Of_Hearts": 10,
  "Jack_Of_Diamonds": 10,
  "Jack_Of_Clubs": 10,
  "Jack_Of_Spades": 10,
  "Queen_Of_Hearts": 10,
  "Queen_Of_Diamonds": 10,
  "Queen_Of_Clubs": 10,
  "Queen_Of_Spades": 10,
  "King_Of_Hearts": 10,
  "King_Of_Diamonds": 10,
  "King_Of_Clubs": 10,
  "King_Of_Spades": 10
  }

player_value = {}
dealer_value = 0

def get_token():
  tokfile = open(TOK_FILE, 'r')
  token = tokfile.read()
  tokfile.close()
  return token

def pull_cards():
   card_list = list(card_deck.keys())
   card = random.choice(card_list)
   return card
   
def check_win(id):
   if player_value[id] == 21:
      return "Win"
   elif player_value[id] > 21:
      return "Lose"
   else:
      return "Neutral"
      
@client.event
async def on_ready():
    print("Connected!")

@client.event
async def on_message(message):
    contents = message.content
    user_id = message.author.id

    if contents.startswith("!playblackjack"):
      player_card1 = pull_cards()
      player_card2 = pull_cards()
      if player_card2 == player_card1:
         player_card2 = pull_cards()
      player_value[user_id] = card_deck[player_card1] + card_deck[player_card2]
      await message.channel.send ("you pulled " + str(player_card1) + " and " + str(player_card2))
      await message.channel.send ("your value is " + str(player_value[user_id]))
      await message.channel.send ("would you like to hit [!hit] or stand? [!stand]")
    
    if contents.startswith("!hit"):
      player_card3 = pull_cards()
      player_value[user_id] += card_deck[player_card3]
      win_check = check_win(user_id)
      if win_check == "Win":
         await message.channel.send ("you pulled " + str(player_card3) + " your new value is " + str(player_value[user_id]))
         await message.channel.send ("WHATS 9+10? THATS RIGHT 21!!!!!!")
      elif win_check == "Lose":
         await message.channel.send ("you pulled " + str(player_card3) + " your new value is " + str(player_value[user_id]))
         await message.channel.send ("looks like you went bust, your value is above 21 and therefore you lose.")
      else:
         await message.channel.send ("you pulled " + str(player_card3) + " your new value is " + str(player_value[user_id]))
         await message.channel.send ("your new value is " + str(player_value[user_id]))
         await message.channel.send ("would you like to hit [!hit] or stand? [!stand]")

      


token = get_token()
client.run(token)