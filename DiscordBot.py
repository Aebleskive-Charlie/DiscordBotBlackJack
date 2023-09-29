import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

TOK_FILE = "token.txt"

card_deck = {
            "Ace_Of_Hearts": [1,11],
            "Ace_Of_Spades": [1,11],
            "Ace_Of_Clubs": [1,11],
            "Ace_Of_Diamonds": [1,11],
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

def get_token():
  tokfile = open(TOK_FILE, 'r')
  token = tokfile.read()
  tokfile.close()
  return token

@client.event
async def on_ready():
    print("Connected!")

@client.event
async def on_message(message):
    contents = message.content
    user_id = message.author.id


