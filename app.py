from flask import Flask
import random

app = Flask(__name__)

ship_prefixes = ["Black", "Crimson", "Drowned", "Storm", "Iron", "Golden", "Bleak",
    "Raven", "Sable", "Silent", "Sea", "Broken", "Cursed", "Burning",
    "Ghost", "Salt", "Shadow", "Howling", "Brine", "Eternal", "Wicked"]
ship_suffixes = ["Warden", "Serpent", "Crown", "Reaver", "Song", "Sovereign",
    "Maelstrom", "Wench", "Marrow", "Hollow", "Siren", "Hand", "Vengeance",
    "Cutlass", "Drift", "Wake", "Fortune", "Tide", "Skull", "Daughter"]
themes = ["buccaneer", "privateer", "ghost", "voodoo", "royal renegade",
    "smugglers", "merchant-raider", "corsair", "witch-crew",
    "storm-bound", "cursed", "naval deserters", "mutineers",
    "free-traders", "salt cult", "undead sailors", "exiled nobles"]
crew_roles = ["Captain", "First Mate", "Quartermaster", "Navigator", "Bosun",
    "Surgeon", "Cook", "Carpenter", "Master Gunner", "Helmsman",
    "Sailmaster", "Powder Monkey", "Cabin Boy", "Lookout",
    "Surge", "Ship’s Mage", "Chronicler", "Rigger",
    "Chaplain", "Musician", "Boatswain’s Mate", "Mutineer in Hiding", "Deckhand"]
first_names = ["Alaric", "Bea", "Corwin", "Dalia", "Eoghan", "Fiora", "Gideon",
    "Hester", "Ilya", "Joss", "Kelda", "Lars", "Mira", "Nolan", "Orla",
    "Pax", "Quinn", "Runa", "Soren", "Tamsin", "Ulric", "Vera", "Wyn",
    "Xander", "Yara", "Zed", "Cassian", "Edda", "Fenric", "Greta",
    "Hollis", "Inigo", "Jonas", "Kael", "Leona", "Maeve", "Niko",
    "Orren", "Petra", "Riven", "Silas", "Thane", "Una", "Vale", "Willa"]
surnames = ["Blackwater", "Ironhand", "Seaborn", "Grimsalt", "Thorn", "Crowe",
    "Mourne", "Harrow", "Voss", "Fen", "Marrow", "Nettle", "Drake",
    "Rook", "Bram", "Carter", "Gallow", "Hale", "Murk", "Shade",
    "Cross", "Kerrigan", "Brine", "Harrowfell", "Saltspire",
    "Dredge", "Vex", "Holloway", "Tideborn", "Under", "Grimm",
    "Moss", "Fleet", "Harker", "Deeplock"]
traits = ["scarred", "one-eyed", "peg-legged", "tattooed", "soft-voiced",
    "booming-laugh", "iron-jawed", "sly", "pious", "superstitious",
    "poker-faced", "humming constantly", "lisping", "fast with a blade",
    "deft with knots", "sleepwalker", "keeps a rosary", "chainsmoker",
    "keeps a secret", "night-vision", "loves dice", "collects teeth",
    "never sleeps", "terrified of water", "wears lucky bones", "sings to storms",
    "Loyal", "Brave", "Empathetic", "Honest", "Persistent",
    "Kind", "Patient", "Respectful", "Generous", "Determined",
    "Creative", "Adaptable", "Optimistic", "Resilient", "Curious",
    "Selfish", "Impatient", "Manipulative", "Greedy", "Egotistical",
    "Quiet", "Observant", "Methodical", "Spontaneous", "Witty"]
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

    crew_member = f"{role}: {first_name} {surname} | Traits: {char_traits}"
    return crew_member

def gen_ship(crew_roles, themes, traits):
    ship_name = gen_ship_name(ship_prefixes, ship_suffixes)
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
    crew_html = '<br>'.join(crew)
    crew_count = len(crew)
    ship = f"<h2>{ship_name}</h2><p><b>Ship Theme:</b> {theme}</p><p><b>Crew Count:</b> {crew_count}</p><p>{crew_html}</p>"

    return ship

@app.route("/")
def home():
    ship_html = gen_ship(crew_roles)
    return f"""
    <html>
    <head>
        <title>Pirate Ship Generator</title>
        <style>
            body {{
                background-color: #0b132b;
                color: #f0e9d2;
                font-family: Georgia, serif;
                text-align: center;
                padding: 30px;
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
            h1, h2 {{ color: #f5f5f5; }}
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












