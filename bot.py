import discord
import random
import datetime


# Create intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize the client with intents
client = discord.Client(intents=intents)

# Initialize banned user IDs and other data
bannedidlist = []

with open('badwords.txt', 'r') as file:
    sexual_words = file.readlines()
    sexual_words = [line.strip() for line in sexual_words]  # Remove newline characters

with open('insults.txt', 'r') as file:
    possible_reply = file.readlines()
    possible_reply = [line.strip() for line in possible_reply]  # Remove newline characters




# Possible responses for banned users
possible_reply = []




# Function to handle adding more banned users
def add_banned_ids():
    while True:
        print("Banned ID list:", bannedidlist)
        print("Enter the ID of the user you want to ban from messaging snake. If you are done, type 'done'")
        bannedid = input()
        
        if bannedid.lower() == "done":
            break
        
        try:
            bannedid_int = int(bannedid)
            if bannedid_int not in bannedidlist:
                bannedidlist.append(bannedid_int)
            else:
                print("ID is already banned.")
        except ValueError:
            print("Please enter a valid number for ID.")

# Handle banned users' messages and timeout inappropriate ones
async def handle_banned_users(message):
    # Check if the message contains "snake" and if the user is banned
    if "snake" in message.content.lower(): #and message.author.id in bannedidlist:
        print(f"Message from {message.author.name} found.")

        # Send a random response to the user
        
        
        # Check for any inappropriate words (e.g., sexual words)
        if any(bad_word in message.content.lower() for bad_word in sexual_words):
            guild = message.guild
            if guild:
                try:
                    # Fetch the member from the guild (forces an API call)
                    member = await guild.fetch_member(message.author.id)
                    
                    # Apply a 5-minute timeout for inappropriate content
                    await message.channel.send(random.choice(possible_reply), reference=message)
                    await member.timeout(datetime.timedelta(minutes=5), reason="Inappropriate message content")
                    print(f"User {member.name} has been timed out.")
                except discord.Forbidden:
                    # In case the bot doesn't have permission to timeout users
                    print(f"Permission error: Unable to timeout user {message.author.name}.")
                except discord.HTTPException as e:
                    # Catch any HTTP exceptions from Discord API
                    print(f"An error occurred when trying to timeout user {message.author.name}: {e}")
                except discord.NotFound:
                    # If the member is not found even after fetching, log it
                    print(f"User with ID {message.author.id} was not found in the guild.")

                
# Event for when the bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Event for when a message is received
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # Handle banned users' messages
    await handle_banned_users(message)

# Ask for the bot's token and run the bot
def start_bot():
    apikey = input("Enter your bot token: ")
    client.run(apikey)

# Run the bot
if __name__ == "__main__":
    # This part only runs if the script is executed directly
    add_banned_ids()  # Let the user add banned IDs
    start_bot()  # Start the bot
