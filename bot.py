import discord
import random
import datetime

# Create intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize the client with intents
client = discord.Client(intents=intents)

# Initialize banned user IDs and other data
jaydnid = 947418695192436756
smallsid = 429634654190960650
bannedidlist = [jaydnid, smallsid]
sexual_words = [    "sex",
    "intercourse",
    "oral",
    "penetration",
    "orgasm",
    "climax",
    "foreplay",
    "arousal",
    "ejaculation",
    "masturbation",
    "erotic",
    "seduction",
    "lust",
    "kink",
    "fetish",
    "nude",
    "naked",
    "sensual",
    "carnal",
    "intimate",
    "coitus",
    "lovemaking",
    "thrust",
    "caress",
    "grope",
    "fondle",
    "moan",
    "groan",
    "orgasmic",
    "libido",
    "passion",
    "desire",
    "ecstasy",
    "pleasure",
    "satisfaction",
    "gratification",
    "copulation",
    "cunnilingus",
    "fellatio",
    "voyeurism",
    "exhibitionism",
    "BDSM",
    "domination",
    "submission",
    "bondage",
    "sensation",
    "tantric",
    "tantra",
    "ménage",
    "threesome",
    "orgy",
    "polyamory",
    "swinging",
    "seductive",
    "allure",
    "alluring",
    "stimulate",
    "stimulation",
    "erogenous",
    "sensuality",
    "aphrodisiac",
    "romance",
    "seductress",
    "seducer",
    "flirt",
    "flirtation",
    "seducing",
    "seductive",
    "seductively",
    "seductiveness",
    "seduction",
    "seductive",
    "arouse",
    "arousing",
    "arousal",
    "turn-on",
    "foreplay",
    "petting",
    "necking",
    "making out",
    "snogging",
    "smooch",
    "kiss",
    "kissing",
    "french kiss",
    "tongue",
    "lick",
    "suck",
    "bite",
    "nibble",
    "touch",
    "fondle",
    "caress",
    "stroke",
    "rub",
    "massage",
    "g-spot",
    "clitoris",
    "nipples",
    "breasts",
    "chest",
    "buttocks",
    "thighs",
    "genitalia",
    "penis",
    "vagina",
    "anus",
    "anal",
    "dildo",
    "vibrator",
    "toy",
    "sex toy",
    "lubricant",
    "lube",
    "condom",
    "contraception",
    "porn",
    "pornography",
    "erotica",
    "striptease",
    "strip",
    "exotic dance",
    "lap dance",
    "pole dance",
    "peep show",
    "burlesque",
    "fetishistic",
    "kinky",
    "deviant",
    "perverse",
    "perversion",
    "nymphomaniac",
    "satyr",
    "succubus",
    "incubus",
    "proclivity",
    "orientation",
    "bisexual",
    "gay",
    "lesbian",
    "queer",
    "pansexual",
    "asexual",
    "demisexual",
    "sapiosexual",
    "transgender",
    "non-binary",
    "genderqueer",
    "intersex",
    "sexuality",
    "sexual identity",
    "fartbox",
    "stink"
    ]  # Add actual inappropriate words here

# Possible responses for banned users
possible_reply = [
    "Please stop.", "Let's keep it friendly.", "Can we take a break from this?", "I’d prefer if you stopped.", 
    "Please respect the rules.", "This conversation is over for now.", "Let’s not do that.", "I don’t appreciate that.", 
    "Let’s be kind to each other.", "It’s time to cool down.", "Please be mindful.", "Can we move on?", 
    "Let’s keep the chat respectful.", "I’m not comfortable with that.", "Please think before you speak.", 
    "Let's focus on something else.", "I’m not engaging with that right now.", "Please give it a rest.", 
    "We need to keep things positive.", "Let's avoid that kind of conversation.", "Please don’t do that.", 
    "Let’s keep the chat safe for everyone.", "Let’s respect each other’s space.", "Can you please stop?", 
    "We should all be kind here.", "I’m going to have to ask you to stop.", "Please be more considerate.", 
    "This isn’t the right place for that.", "Let’s keep it fun and light.", "I’d prefer if you didn’t do that.", 
    "Please be respectful of others.", "We all need to be kind here.", "Let’s stick to the rules.", 
    "Kindness goes a long way.", "That’s not really okay.", "Please stop, we’re all here to have a good time.", 
    "Let’s try to keep the atmosphere positive.", "Let’s be respectful and kind to everyone.", 
    "This isn’t the time or place for that.", "Please be mindful of the community guidelines.", 
    "I’m going to have to ask for a little more respect.", "Let’s keep things friendly and welcoming.", 
    "I don’t think that’s appropriate right now.", "Please take a moment to think about that.", 
    "Let’s keep it civil.", "Please respect others in the chat.", "Let’s stick to the conversation at hand."
]


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
    if "snake" in message.content.lower() and message.author.id in bannedidlist:
        print(f"Message from {message.author.name} found.")

        # Send a random response to the user
        await message.channel.send(random.choice(possible_reply), reference=message)
        
        # Check for any inappropriate words (e.g., sexual words)
        if any(bad_word in message.content.lower() for bad_word in sexual_words):
            guild = message.guild
            if guild:
                try:
                    # Fetch the member from the guild (forces an API call)
                    member = await guild.fetch_member(message.author.id)
                    
                    # Apply a 5-minute timeout for inappropriate content
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
