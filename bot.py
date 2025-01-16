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
#i just used grok for this lol
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
    "stink",
    "hole"
    ]  # Add actual inappropriate words here

# Possible responses for banned users
possible_reply = [
    "Did you just try to 1v1 me with that move?", "Did you forget to press the 'win' button?", 
    "I’ve seen NPCs with better decision-making.", "That’s the kind of play that gets you banned in ranked.", 
    "Your aim is like a ping of 999, all over the place.", "You call that a strategy? I’ve seen bots with better tactics.", 
    "Is that your best? My grandma could do better in a speedrun.", "That move was so bad, even the game crashed.", 
    "Are you even trying, or just pressing buttons?", "I’ve seen better plays in tutorial mode.", 
    "You’re like the AFK teammate in every match.", "Was that a tactic or were you just mashing your keyboard?", 
    "That was so bad, the enemy team sent you a sympathy message.", "Your game sense is as bad as your internet connection.", 
    "Bro, you’re about as useful as a broken controller.", "That wasn’t a play, that was a disaster waiting to happen.", 
    "If that was your ultimate move, I’m glad it’s on cooldown.", "That was so slow, even lag would’ve beaten you.", 
    "Is this your first time playing? You sure about that?", "You wouldn’t even hit a target if it was standing still.", 
    "Did you take a detour through the noob zone?", "Not even a bot would mess up that badly.", 
    "You’ve got more mistakes than a speedrun glitch.", "Is this a *tactical* retreat or just bad gameplay?", 
    "Did you just throw your controller at the screen and hope for a win?", "I’ve seen better plays in low-level matchmaking.", 
    "You’ve got a better chance at winning a coin flip than winning this game.", "Are you trying to play or just watching the game happen?", 
    "That was like a *level 1* noob trying to solo a raid boss.", "I’ve seen better tactics in a mobile game tutorial.", 
    "Bro, you’re playing like you just discovered the WASD keys.", "Is that your strategy, or did you just forget what the game is?", 
    "Did you forget that pressing all the buttons doesn’t make you a pro?", "You’re about as useful as a healing potion in a speedrun.", 
    "The only thing you’re good at is feeding the enemy team.", "Your skills are as weak as a low-level armor set.", 
    "You’re playing like you’ve never touched a game before.", "That was so bad, even the game gave up on you.", 
    "Is that a plan or were you just hoping for a lucky shot?", "Your gameplay is like a lag spike—totally unpredictable.", 
    "I’ve seen AI players with more creativity than that move.", "You just activated my trap card... and then walked into it.", 
    "You’re the kind of player who gets stuck on tutorial stages.", "You’re not even a speed bump, you're a whole traffic jam.", 
    "That play was a bigger fail than a noob in ranked matches.", "Nice job, you just triggered the *rage quit* emote.", 
    "You’ve got the reflexes of a lagging server.", "That was a *strategic* disaster. 10/10 would not recommend.", 
    "I’ve seen bots play smarter than that.", "If I had a nickel for every time you missed, I’d be buying upgrades.", 
    "You’re as useful as a broken respawn timer.", "I’ve seen bots perform better than that strategy.", 
    "Did you just roll for stats or was that random chaos?", "That move was so bad, even the enemy team sent a thank-you note.", 
    "You’ve got the aim of a potato and the strategy of a banana.", "That’s one way to throw the game, I guess.", 
    "I’ve seen better coordination in a 3v3 match of Rock, Paper, Scissors.", "Is that your special tactic? Because it’s not working.", 
    "your so common your like Khostov!! ",
    "Did you just miss that super? That’s like shooting a Thunderlord into a wall.",
    "I’ve seen more kills from a level 1 Guardian than you just got in that strike.",
    "Are you running *that* exotic? You might as well be wielding a green weapon.",
    "You have the accuracy of a Titan trying to jump over a gap on the Dreadnaught.",
    "That was a worse play than trying to solo a Nightfall without any heavy ammo.",
    "I’ve seen better strategies in the Tower during a Crucible downtime.",
    "Nice work, you almost got a kill! Too bad your grenade was a dud.",
    "That play was like using a Gjallarhorn on a group of Dregs. Overkill.",
    "Are you sure you're a Hunter? I think you're just an NPC in the wrong subclass.",
    "You’re playing like you're still stuck on the Cosmodrome tutorial.",
    "That move was as effective as trying to kill a Kell with a hand cannon from across the map.",
    "That’s a play worthy of a *Destiny 1* PvP match. Everyone’s confused and no one’s having fun.",
    "Bro, even a Fallen Shank could dodge that shot.",
    "You’re running around like a Warlock with no Armor of Light. Good luck out there.",
    "I’d say you were using a low-level weapon, but that’s an insult to green gear.",
    "You know it's bad when even Eris Morn is like, 'Not again.'",
    "Did you just try to raid solo with a green weapon? That’s like showing up to the Vault of Glass with a potato gun.",
    "I’ve seen more coordination in a 6v6 match of Control with six randoms.",
    "You’re playing like you’re trying to teach a Cabal how to raid.",
    "That was like trying to do a flawless run in the Crucible with a Rocket Launcher. Just no.",
    "Nice super, too bad it was wasted on a couple of Scorn. Real threat, huh?",
    "You’ve got the timing of a Hunter trying to dodge in the middle of a rocket barrage.",
    "Even a Fallen Kalli would do better in Gambit than you just did in that invasion.",
    "You’re running around like you’re trying to solo the Last Wish raid with a bow.",
    "That was more embarrassing than when we all realized the Taken weren't really gone in Destiny 2.",
    "You missed your shot like a Titan trying to jump across the *Leviathan* without Wings of Sacred Dawn.",
    "I think you’d have better luck winning a game of Crucible with a PvE loadout.",
    "That play was as smooth as trying to revive during a heavy phase in the *Leviathan* raid.",
    "Bro, you're playing Destiny like you just picked up the game during *Season of the Splicer*.",
    "Did you just pop your super and then miss everything? That’s a real *Titan* move.",
    "I’ve seen more movement from a Vex Minotaur stuck in a wall.",
    "You’re as clueless as a Hunter with no throwing knives trying to melee in the Crucible.",
    "That was like running into the Cabal’s *Red Legion* with a broken sparrow and no ammo.",
    "You’re acting like you're the *Crota* raid's easiest encounter and not the final boss.",
    "That was as bad as trying to get a flawless completion of *Prison of Elders* in Destiny 1 with no revives.",
    "You’re moving around like a Warlock without the *Dawnblade* glide perk.",
    "Did you really just try to revive in the middle of a *Nightfall*? That’s like reading the grimoire cards in reverse.",
    "You’re the kind of player who spends 20 minutes in the Tower just to wipe in the first 5 minutes of a raid.",
    "Is that your version of clutching the *Vault of Glass* solo? Looked more like a wipe.",
    "That was as effective as a Hunter trying to *Golden Gun* an Archon Priest from across the map.",
    "I’ve seen more finesse in the Crucible with a primary weapon and no perks.",
    "Trying to beat that boss with your gear is like trying to take on Riven with a *Zalo Supercell*.",
    "You’re playing like you're still figuring out how to use the Ghost during a *Destiny 2* strike.",
    "That move was as useful as using a *Plan C* in PvE. Nice try, though.",
    "Your gameplay is like trying to kill a Taken Acolyte with a fusion rifle at point-blank range.",
    "That was like trying to solo a *Nightmare Hunt* with no mods and no heavy ammo.",
    "Bro, you missed that super like you were trying to hit a *Vex Minotaur* with a Scout Rifle from orbit.",
    "That was as bad as trying to do a *Nightfall* without a proper burn. You’re just setting yourself up to fail."

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
    if "snake" in message.content.lower(): #and message.author.id in bannedidlist:
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
