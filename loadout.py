from weapons import Weapon
import random
#list of weapons copied from Chat-GPT by the way


#Scout
sco_weapon_list_primary = [
    "Scattergun",
    "Force-A-Nature",
    "Shortstop",
    "Soda Popper",
    "Baby Face's Blaster",
    "Back Scatter"
]
sco_weapon_list_secondary = [
    "Bonk! Atomic Punch",
    "Crit-a-Cola",
    "MadMilk",
    "Winger",
    "Pretty Boy's Pocket Pistol"
]
sco_weapon_list_melee = [
    "Bat",
    "Holy Mackerel",
    "Unarmed Combat (Fish)",
    "Sandman",
    "Atomizer",
    "Wrap Assassin"
]

#Soldier
sol_weapon_list_primary = [
    "Rocket Launcher",
    "Direct Hit",
    "Black Box",
    "Liberty Launcher",
    "Cow Mangler 5000",
    "Beggar's Bazooka",
    "Air Strike",
    "Original"
]
sol_weapon_list_secondary = [
    "Shotgun",
    "Reserve Shooter",
    "Buff Banner",
    "Gunboats",
    "Mantreads",
    "Battalion's Backup",
    "Concheror",
    "Panic Attack",
    "Righteous Bison",
    "Equalizer",
    "Escape Plan"
]
sol_weapon_list_melee = [
    "Shovel",
    "Equalizer",
    "Pain Train",
    "Half-Zatoichi",
    "Disciplinary Action",
    "Market Gardener",
    "Escape Plan"
]

# Pyro
pyr_weapon_list_primary = [
    "Flamethrower",
    "Backburner",
    "Degreaser",
    "Phlogistinator",
    "Dragon's Fury"
]
pyr_weapon_list_secondary = [
    "Shotgun",
    "Reserve Shooter",
    "Panic Attack",
    "Detonator",
    "Manmelter",
    "Scorch Shot"
]
pyr_weapon_list_melee = [
    "Fire Axe",
    "Axtinguisher",
    "Homewrecker",
    "Powerjack",
    "Back Scratcher",
    "Sharpened Volcano Fragment",
    "Third Degree",
    "Neon Annihilator"
]

#Demoman
dem_weapon_list_primary = [
    "Grenade Launcher",
    "Loose Cannon",
    "Loch-n-Load",
    "Iron Bomber"
]
dem_weapon_list_secondary = [
    "Stickybomb Launcher",
    "Scottish Resistance",
    "Chargin' Targe",
    "Splendid Screen",
    "Tide Turner"
]
dem_weapon_list_melee = [
    "Bottle",
    "Scottish Handshake",
    "Eyelander",
    "Horseless Headless Horsemann's Headtaker",
    "Ullapool Caber",
    "Claidheamh Mòr",
    "Persian Persuader"
]

# Heavy
hea_weapon_list_primary = [
    "Minigun",
    "Natascha",
    "Brass Beast",
    "Tomislav",
    "Huo-Long Heater"
]
hea_weapon_list_secondary = [
    "Shotgun",
    "Family Business",
    "Sandvich",
    "Dalokohs Bar",
    "Buffalo Steak Sandvich",
    "Second Banana"
]
hea_weapon_list_melee = [
    "Fists",
    "Killing Gloves of Boxing",
    "Gloves of Running Urgently",
    "Holiday Punch",
    "Eviction Notice"
]

# Engineer
eng_weapon_list_primary = [
    "Shotgun",
    "Frontier Justice",
    "Widowmaker",
    "Pomson 6000",
    "Rescue Ranger"
]
eng_weapon_list_secondary = [
    "Pistol",
    "Lugermorph",
    "Wrangler",
    "Short Circuit"
]
eng_weapon_list_melee = [
    "Wrench",
    "Golden Wrench",
    "Southern Hospitality",
    "Jag",
    "Eureka Effect"
]

# Medic
me_weapon_list_primary = [
    "Syringe Gun",
    "Blutsauger",
    "Crusader's Crossbow",
    "Overdose"
]
me_weapon_list_secondary = [
    "Medigun",
    "Kritzkrieg",
    "Quick-Fix",
    "Vaccinator"
]
med_weapon_list_melee = [
    "Bonesaw",
    "Ubersaw",
    "Vita-Saw",
    "Amputator",
    "Solemn Vow"
]

# Sniper
sni_weapon_list_primary = [
    "Sniper Rifle",
    "Huntsman",
    "Sydney Sleeper",
    "Bazaar Bargain",
    "Machina",
    "Hitman's Heatmaker",
    "Classic"
]
sni_weapon_list_secondary = [
    "SMG",
    "Cleaner's Carbine"
]
sni_weapon_list_melee = [
    "Kukri",
    "Tribalman's Shiv",
    "Shahanshah",
    "Bushwacka"
]

# Spy
spy_weapon_list_primary = [
    "Revolver",
    "Ambassador",
    "L'Etranger",
    "Enforcer"
]
spy_weapon_list_melee = [
    "Knife",
    "Your Eternal Reward",
    "Conniver's Kunai",
    "Big Earner",
    "Spy-cicle",
    "Dead Ringer",
    "Cloak and Dagger",
    "Invis Watch"
]


