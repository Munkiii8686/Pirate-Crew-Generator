from flask import Flask
import random

app = Flask(__name__)

ship_prefixes = ["Black", "Crimson", "Drowned", "Storm", "Iron", "Golden", "Bleak",
    "Raven", "Sable", "Silent", "Sea", "Broken", "Cursed", "Burning",
    "Ghost", "Salt", "Shadow", "Howling", "Brine", "Eternal", "Wicked",
    "Obsidian", "Silver", "Scarlet", "Gilded", "Dusky", "Vengeful", "Emerald",
    "Ivory", "Copper", "Midnight", "Bloody", "Forsaken", "Grinning", "Lost",
    "Shattered", "Tidal", "Infernal", "Ashen", "Drifting", "Savage", "Haunted",
    "Pale", "Rusted", "Leviathan", "Moonlit", "Ironclad", "Thundering", "Serpent’s",
    "Wild", "Deadman’s", "Raging", "Verdant", "Weeping", "Free", "Mariner’s",
    "Severed", "Ebon", "Grim", "Tempest", "Velvet", "Screaming", "Bloated",
    "Eternal", "Bitter", "Frozen", "Bleeding", "Risen", "Twilight", "Fallen",
    "Grave", "Dusken", "Mournful", "Sorrowful", "Whispering", "Tattered",
    "Endless", "Rotten", "Pierced", "Harbored", "Searing", "Scalded", "Coral",
    "Drunken", "Doomed", "Brazen", "Fireborne", "Stormborne", "Waveborne",
    "Dire", "Spectral", "Golden-Eyed", "Silverfin", "Blooded", "Wretched",
    "Gnarled", "Creaking", "Splintered", "Risen", "Gallant", "Maiden’s",
    "Old", "Clever", "Blackhearted", "Ruthless", "Unholy", "Verdigris",
    "Salted", "Whispered", "Oathbound", "Lurking", "Greedy", "Merciless",
    "Torn", "Scarred", "Unbroken", "Cracked", "Wandering", "Eerie", "Tempestuous"]
ship_suffixes = ["Warden", "Serpent", "Crown", "Reaver", "Song", "Sovereign",
    "Maelstrom", "Wench", "Marrow", "Hollow", "Siren", "Hand", "Vengeance",
    "Cutlass", "Drift", "Wake", "Fortune", "Tide", "Skull", "Daughter",
    "Voyager", "Mist", "Fang", "Harbinger", "Bane", "Chalice", "Banner",
    "Bounty", "Fury", "Raven", "Dagger", "Queen", "Trident", "Anchor",
    "Tempest", "Hunter", "Whisper", "Beacon", "Cross", "Promise", "Saint",
    "Curse", "Lament", "Wave", "Arrow", "Eclipse", "Grave", "Corsair",
    "Promise", "Star", "Gale", "Reckoning", "Wraith", "Wrath", "Prize",
    "Horizon", "Gambit", "Doom", "Echo", "Delight", "Spite", "Spear",
    "Voyage", "Embrace", "Blade", "Spirit", "Grace", "Throne", "Sway",
    "Terror", "Fate", "Mariner", "Cutter", "Specter", "Crescent", "Ghost",
    "Moon", "Sun", "Pearl", "Torch", "Depths", "Breaker", "Abyss",
    "Dawn", "Dusk", "Night", "Sky", "Reef", "Shore", "Plunder",
    "Omen", "Compass", "Wheel", "Anchor", "Tempest", "Crest", "Crossing",
    "Reprisal", "Vow", "Seeker", "Remnant", "Scourge", "Bastion",
    "Endeavor", "Dream", "Pact", "Voyager", "Haven", "Bloom", "Legacy",
    "Edge", "Shroud", "Talon", "Ruin", "Eternity", "Faith", "Scepter",
    "Banner", "Prophet", "Delirium", "Wake", "Drifter", "Stranger"]
ship_types = ["Sloop", "Brigantine", "Galleon", "Man-o-War", "Frigate", "Corsair", "Cutter"]
themes = ["buccaneer", "privateer", "ghost", "voodoo", "royal renegade",
    "smugglers", "merchant-raider", "corsair", "witch-crew",
    "storm-bound", "cursed", "naval deserters", "mutineers",
    "free-traders", "salt cult", "undead sailors", "exiled nobles"]
crew_roles = ["Captain", "First Mate", "Quartermaster", "Navigator", "Bosun",
    "Surgeon", "Cook", "Carpenter", "Master Gunner", "Helmsman",
    "Sailmaster", "Powder Monkey", "Cabin Boy", "Lookout",
    "Surge", "Ship’s Mage", "Chronicler", "Rigger",
    "Chaplain", "Musician", "Boatswain’s Mate", "Mutineer in Hiding", "Deckhand"]
first_names = ["Alaric", "Bea", "Corwin", "Dalia", "Eoghan", "Fiora", "Gideon", "Hester",
    "Ilya", "Joss", "Kelda", "Lars", "Mira", "Nolan", "Orla", "Pax", "Quinn",
    "Runa", "Soren", "Tamsin", "Ulric", "Vera", "Wyn", "Xander", "Yara",
    "Zed", "Cassian", "Edda", "Fenric", "Greta", "Hollis", "Inigo", "Jonas",
    "Kael", "Leona", "Maeve", "Niko", "Orren", "Petra", "Riven", "Silas",
    "Thane", "Una", "Vale", "Willa", "Adric", "Belwyn", "Caela", "Doran", "Elara", "Finn", "Galen", "Halvard",
    "Isolde", "Jareth", "Korrin", "Lyra", "Magnus", "Nessa", "Odel", "Perrin",
    "Rhea", "Sabine", "Torin", "Uriah", "Vayne", "Wendell", "Xela", "Yorrin",
    "Zara", "Alden", "Bran", "Calla", "Darius", "Eamon", "Faelan", "Griff",
    "Hadric", "Ianthe", "Juna", "Kestrel", "Lorien", "Merrin", "Nairn",
    "Orin", "Pavel", "Quora", "Ronan", "Sable", "Tarin", "Ulma", "Voss",
    "Wren", "Xyra", "Yann", "Zephyr", "Asha", "Bram", "Corra", "Dax", "Eleni", "Flint", "Gavril", "Helaine",
    "Idric", "Juno", "Kara", "Lucan", "Marek", "Niall", "Ophel", "Phineas",
    "Rex", "Selene", "Thorne", "Ursa", "Viktor", "Willem", "Xanthe", "Yves",
    "Zora", "Arlen", "Brynn", "Cyrus", "Drea", "Eldric", "Fenn", "Gisa",
    "Hale", "Ilara", "Jory", "Keir", "Luna", "Malric", "Nira", "Oskar",
    "Pyra", "Rivena", "Sol", "Tirra", "Vyn", "Wald", "Ysolde", "Zayne"]
surnames = ["Blackwater", "Ironhand", "Seaborn", "Grimsalt", "Thorn", "Crowe",
    "Mourne", "Harrow", "Voss", "Fen", "Marrow", "Nettle", "Drake",
    "Rook", "Bram", "Carter", "Gallow", "Hale", "Murk", "Shade",
    "Cross", "Kerrigan", "Brine", "Harrowfell", "Saltspire",
    "Dredge", "Vex", "Holloway", "Tideborn", "Under", "Grimm",
    "Moss", "Fleet", "Harker", "Deeplock",
    "Ashvale", "Windmere", "Stormborn", "Gravetide", "Corvin",
    "Darkmoor", "Rimeshade", "Wyrick", "Hollowbrook", "Saltbane",
    "Redmarsh", "Coldharbor", "Greymast", "Ironreef", "Thistledown",
    "Driftwind", "Longshore", "Mireborn", "Cragg", "Roughwake",
    "Wraithson", "Emberlane", "Fairharbor", "Locke", "Cindervale",
    "Nightrill", "Silt", "Broadkeel", "Wavecrest", "Brinemouth",
    "Korr", "Ironvale", "Lowtide", "Briarhelm", "Frostwell",
    "Eldmar", "Galespire", "Shard", "Havenshade", "Gravetree",
    "Sunfell", "Larksong", "Orrinvale", "Brack", "Mournspire",
    "Quickwater", "Windrow", "Stillwell", "Darkhaven", "Marlin",
    "Tallow", "Kindred", "Runeward", "Shatterbay", "Deepmere",
    "Brackwater", "Tern", "Saltlock", "Hollowstrand", "Dunwell",
    "Cask", "Wicklow", "Ironspire", "Oathwell", "Verrin"]
traits = ["scarred", "one-eyed", "peg-legged", "tattooed", "soft-voiced",
    "booming-laugh", "iron-jawed", "sly", "pious", "superstitious",
    "poker-faced", "humming constantly", "lisping", "fast with a blade",
    "deft with knots", "sleepwalker", "keeps a rosary", "chainsmoker",
    "keeps a secret", "night-vision", "loves dice", "collects teeth",
    "never sleeps", "terrified of water", "wears lucky bones", "sings to storms",
    "Loyal", "Brave", "Empathetic", "Honest", "Persistent", "Kind", "Patient",
    "Respectful", "Generous", "Determined", "Creative", "Adaptable",
    "Optimistic", "Resilient", "Curious", "Selfish", "Impatient",
    "Manipulative", "Greedy", "Egotistical", "Quiet", "Observant",
    "Methodical", "Spontaneous", "Witty",
    "scarred by lightning", "missing fingers", "haunted by dreams",
    "can’t swim", "always smiling", "wears a tattered coat",
    "collects coins from every port", "fears seagulls", "has a false eye",
    "mutters old prayers", "keeps a pet crab", "smells of rum",
    "hates music", "writes poetry secretly", "carves charms from driftwood",
    "won’t eat fish", "claims royal blood", "believes storms talk to them",
    "keeps a cursed locket", "draws maps at night", "dances when nervous",
    "lost a sibling to pirates", "speaks to ghosts", "trusts no captain",
    "paints the sea every morning", "wears mismatched boots",
    "laughs at funerals", "follows strange omens", "hears whispers in the wind",
    "chews seaweed for luck", "has webbed fingers", "can read the stars perfectly",
    "hates silence", "collects knives", "can mimic voices", "never blinks",
    "has a clockwork hand", "drinks only rainwater", "carries a black pearl",
    "claims to have killed a sea god", "is secretly literate",
    "recites poetry mid-battle", "has an unhealing wound", "loves riddles",
    "always cold", "blind in one eye", "has gills", "believes they’re immortal",
    "keeps feathers in their hair", "has a ship tattoo on their chest",
    "never lies", "always lies", "afraid of mirrors", "wears gloves at all times",
    "hums lullabies to the sea", "never removes their hat", "collects seashells",
    "writes letters to the dead", "counts steps wherever they go",
    "refuses to kill", "enjoys storms", "has a ghostly twin",
    "dreams of fire", "cheats at cards", "prays before battle",
    "carves runes into their blade", "never forgets a face", "can’t read",
    "follows the moon’s phases", "is tone-deaf", "smells of lavender",
    "worships an old sea god", "always hungry", "wears spectacles",
    "believes fish talk to them", "walks barefoot", "laughs like thunder",
    "weeps in rain", "collects feathers", "obsessed with luck charms",
    "believes death owes them a favor", "keeps a broken compass",
    "claims to see the future", "refuses to drink rum", "counts stars every night",
    "carries an old sea journal", "won’t speak their real name"]
backstory_bones = ["escaped a slaver’s hold",
    "lost their family to a sea monster",
    "served in a royal navy then deserted",
    "betrayed an admiral for a chest of coins",
    "was cursed by a coastal witch",
    "seeks a lost map to a sunken city",
    "owes a blood debt to a dockside crime lord",
    "swore revenge on a mutinous crewmate",
    "hunted by a vengeful priesthood",
    "is the heir to a ruined trading house",
    "stole a ship from their own captain",
    "heard the sea whisper their true name",
    "was the only survivor of the Stone Village wreck",
    "dreams of a city beneath the waves",
    "made a pact with something in the deep",
    "smuggled relics for a cult",
    "pretends to be human",
    "is haunted by drowned voices",
    "once commanded a fleet before the curse"]


def gen_ship_name(ship_prefixes, ship_suffixes):
    prefix = random.choice(ship_prefixes)
    suffix = random.choice(ship_suffixes)
    return (f"The {prefix} {suffix}")

def gen_crew_member(role, first_names, surnames, traits):
    first_name = random.choice(first_names)
    surname = random.choice(surnames)
    traits_copy = traits.copy()
    trait_num = random.randint(1, 3)
    trait_list = []
    for x in range(trait_num):
        trait = random.choice(traits_copy)
        trait_list.append(trait)
        traits_copy.remove(trait)
        
    char_traits = ', '.join(trait_list)

    crew_member = f"<b>{role}:</b> {first_name} {surname} | <b>Traits:</b> {char_traits}"
    return crew_member

def gen_ship(crew_roles, themes, traits, ship_types):
    ship_name = gen_ship_name(ship_prefixes, ship_suffixes)
    ship_type = random.choice(ship_types)
    crew = []
    theme = random.choice(themes)
    roles = crew_roles.copy()
    random.shuffle(roles)
    random_int = random.randint(15, 50)

    captain = gen_crew_member("Captain", first_names, surnames, traits)
    crew.append(captain)

    if "Captain" in roles:
        roles.remove("Captain")

    for i in range(random_int - 1):
        role = roles[i] if i < len(roles) else "Deckhand"
        crew_member = gen_crew_member(role, first_names, surnames, traits)
        crew.append(crew_member)

    crew.sort(key=lambda member: crew_roles.index(member.split(":")[0])
                if member.split(":")[0] in crew_roles else 999)
    crew_html = ''.join(f"<li>{member}</li>" for member in crew)
    crew_count = len(crew)
    ship = f"<h1>{ship_name}</h1><p><b>Ship Type:</b> {ship_type}</p><p><b>Ship Theme:</b> {theme}</p><p><b>Crew Count:</b> {crew_count}</p><ul>{crew_html}</ul>"
    ship = f"<div class='ship-card'>{ship}</div>"
    return ship

@app.route("/")
def home():
    ship_html = gen_ship(crew_roles, themes, traits, ship_types)
    return f"""
    <html>
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Pirata+One&display=swap" rel="stylesheet">
        <title>Pirate Ship Generator</title>
        <style>
            body {{
                background-image: url('https://www.transparenttextures.com/patterns/aged-paper.png');
                background-color: #0b132b;
                color: #f0e9d2;
                font-family: Pirata One, serif;
                text-align: justify;
                padding: 30px;
                max-width: 900px;
                margin: auto;
            }}
            title {{
                font-family: Pirata One, serif;
                color: #ffffff;
                text-align: centre;
                padding: 30px;
            }}
            h1, h2 {{
                font-family: Pirata One, serif;
                color: #000000;
                text-align: centre;
                padding: 30px;
            }}
            p, li {{
                font-family: Georgia, serif;
                color: #000000;
                text-align: justify;
                padding: 30px;
                margin-top: 4px;
                margin-bottom: 4px
                line-height: 1.4;
            }}
            ul {{
                list-style-type: none;
                padding-left: 0;
            }}
            .ship-card {{
                background-color: #e6e8cf;
                background-image: url("https://www.transparenttextures.com/patterns/aged-paper.png");
                background-blend-mode: multiply;
                border: 1px solid #3a506b;
                border-radius: 12px;
                padding: 20px;
                margin: 20px auto;
                max-width: 900px;
                box-shadow: 0 0 10px rgba(0,0,0,0.5);
            }}
            button {{
                margin-top: 20px;
                padding: 10px 20px;
                background-color: #3a506b;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }}
            button:hover {{
                background-color: #5bc0be;
            }}
        </style>
    </head>
    <body>
        <h1>Pirate Ship & Crew Generator</h1>
        {ship_html}
        <form action="/" method="get">
            <button>Generate Another</button>
        </form>
    </body>
    </html>
    """

# === START APP ===
if __name__ == "__main__":
    app.run(debug=True)
























