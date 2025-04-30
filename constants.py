import pygame

# Configs
PHYSICS_DEBUG = False
RUNNING_LOCALLY = False

# Update when new pokemon
NUMBER_OF_POKEMON_GENS = 9
NUMBER_OF_POKEMON_TYPES = 18

# Physics Constants
PHYSICS_MAGNITUDE = 10
PHYSICS_GRAVITY = 0
PHYSICS_ELASTICITY = 1
PHYSICS_MAX_COLLISIONS = [7, 10]
PHYSICS_AIR_RESISTANCE = 0

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
GREEN = (40, 120, 40)
NEON = (120, 245, 66)
LIGHT_CORNFLOWER_BLUE_2 = (152, 196, 236)
LIGHT_CORNFLOWER_BLUE_1 = (100, 166, 225)
LIGHT_PURPLE_1 = (148, 115, 200)
DARK_MAGENTA_2 = (126, 0, 70)
BACKGROUND_COLOR = DARK_MAGENTA_2

# File Locations
ROOTDIR = ''
ASSETS_LOCATION = 'assets/'
ASYNC_PREFIX = 'async:'
CSV_LOCATION = ROOTDIR + ASSETS_LOCATION + 'sheet_smart.csv'
TBH_LOCATION = ROOTDIR + ASSETS_LOCATION + 'tbh.png'
BLAHAJ_LOCATION = ROOTDIR + ASSETS_LOCATION + 'blahaj.gif'
GIF_LOCATION = ROOTDIR + ASSETS_LOCATION + 'sprites/'
MP3_LOCATION = ROOTDIR + ASSETS_LOCATION + 'mps/'

# Dimensions
WINDOW_HEIGHT = 460
WINDOW_WIDTH = 690
WRAP_X_PADDING = 10
WRAP_Y_PADDING = .5

# Fonts
FONT_32 = pygame.font.Font('freesansbold.ttf', 32)
FONT_24 = pygame.font.Font('freesansbold.ttf', 24)
FONT_40 = pygame.font.Font('freesansbold.ttf', 40)
FONT_18 = pygame.font.Font('freesansbold.ttf', 18)
FONT_SIZE_TEST_STRING = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.?!\"\'"

# Other
SMART_TYPE_HEADER = "SSP-T"
SMART_GEN_HEADER = "SSP-G"
GIF_COUNT = 649
GIF_LIST = ['abomasnow', 'abra', 'absol', 'accelgor', 'aerodactyl', 'aggron', 'aipom', 'alakazam', 'alomomola',
           'altaria', 'ambipom', 'amoonguss', 'ampharos', 'anorith', 'arbok', 'arcanine', 'arceus', 'archen',
           'archeops', 'ariados', 'armaldo', 'aron', 'articuno', 'audino', 'axew', 'azelf', 'azumarill', 'azurill',
           'bagon', 'baltoy', 'banette', 'barboach', 'basculin-red-striped', 'bastiodon', 'bayleef', 'beartic',
           'beautifly', 'beedrill', 'beheeyem', 'beldum', 'bellossom', 'bellsprout', 'bibarel', 'bidoof', 'bisharp',
           'blastoise', 'blaziken', 'blissey', 'blitzle', 'boldore', 'bonsly', 'bouffalant', 'braviary', 'breloom',
           'bronzong', 'bronzor', 'budew', 'buizel', 'bulbasaur', 'buneary', 'burmy', 'butterfree', 'cacnea',
           'cacturne', 'camerupt', 'carnivine', 'carracosta', 'carvanha', 'cascoon', 'castform', 'caterpie', 'celebi',
           'chandelure', 'chansey', 'charizard', 'charmander', 'charmeleon', 'chatot', 'cherrim', 'cherubi',
           'chikorita', 'chimchar', 'chimecho', 'chinchou', 'chingling', 'cinccino', 'clamperl', 'claydol', 'clefable',
           'clefairy', 'cleffa', 'cloyster', 'cobalion', 'cofagrigus', 'combee', 'combusken', 'conkeldurr', 'corphish',
           'corsola', 'cottonee', 'cradily', 'cranidos', 'crawdaunt', 'cresselia', 'croagunk', 'crobat', 'croconaw',
           'crustle', 'cryogonal', 'cubchoo', 'cubone', 'cyndaquil', 'darkrai', 'darmanitan', 'darumaka', 'deerling',
           'deino', 'delcatty', 'delibird', 'deoxys', 'dewgong', 'dewott', 'dialga', 'diglett', 'ditto', 'dodrio',
           'doduo', 'donphan', 'dragonair', 'dragonite', 'drapion', 'dratini', 'drifblim', 'drifloon', 'drilbur',
           'drowzee', 'druddigon', 'ducklett', 'dugtrio', 'dunsparce', 'duosion', 'durant', 'dusclops', 'dusknoir',
           'duskull', 'dustox', 'dwebble', 'eelektrik', 'eelektross', 'eevee', 'ekans', 'electabuzz', 'electivire',
           'electrike', 'electrode', 'elekid', 'elgyem', 'emboar', 'emolga', 'empoleon', 'entei', 'escavalier',
           'espeon', 'excadrill', 'exeggcute', 'exeggutor', 'exploud', "farfetchd", 'fearow', 'feebas', 'feraligatr',
           'ferroseed', 'ferrothorn', 'finneon', 'flaaffy', 'flareon', 'floatzel', 'flygon', 'foongus', 'forretress',
           'fraxure', 'frillish', 'froslass', 'furret', 'gabite', 'gallade', 'galvantula', 'garbodor', 'garchomp',
           'gardevoir', 'gastly', 'gastrodon', 'genesect', 'gengar', 'geodude', 'gible', 'gigalith', 'girafarig',
           'giratina', 'glaceon', 'glalie', 'glameow', 'gligar', 'gliscor', 'gloom', 'golbat', 'goldeen', 'golduck',
           'golem', 'golett', 'golurk', 'gorebyss', 'gothita', 'gothitelle', 'gothorita', 'granbull', 'graveler',
           'grimer', 'grotle', 'groudon', 'grovyle', 'growlithe', 'grumpig', 'gulpin', 'gurdurr', 'gyarados', 'happiny',
           'hariyama', 'haunter', 'haxorus', 'heatmor', 'heatran', 'heracross', 'herdier', 'hippopotas', 'hippowdon',
           'hitmonchan', 'hitmonlee', 'hitmontop', 'ho-oh', 'honchkrow', 'hoothoot', 'hoppip', 'horsea', 'houndoom',
           'houndour', 'huntail', 'hydreigon', 'hypno', 'igglybuff', 'illumise', 'infernape', 'ivysaur', 'jellicent',
           'jigglypuff', 'jirachi', 'jolteon', 'joltik', 'jumpluff', 'jynx', 'kabuto', 'kabutops', 'kadabra', 'kakuna',
           'kangaskhan', 'karrablast', 'kecleon', 'keldeo', 'kingdra', 'kingler', 'kirlia', 'klang', 'klink',
           'klinklang', 'koffing', 'krabby', 'kricketot', 'kricketune', 'krokorok', 'krookodile', 'kyogre', 'kyurem',
           'lairon', 'lampent', 'landorus', 'lanturn', 'lapras', 'larvesta', 'larvitar', 'latias', 'latios', 'leafeon',
           'leavanny', 'ledian', 'ledyba', 'lickilicky', 'lickitung', 'liepard', 'lileep', 'lilligant', 'lillipup',
           'linoone', 'litwick', 'lombre', 'lopunny', 'lotad', 'loudred', 'lucario', 'ludicolo', 'lugia', 'lumineon',
           'lunatone', 'luvdisc', 'luxio', 'luxray', 'machamp', 'machoke', 'machop', 'magby', 'magcargo', 'magikarp',
           'magmar', 'magmortar', 'magnemite', 'magneton', 'magnezone', 'makuhita', 'mamoswine', 'manaphy', 'mandibuzz',
           'manectric', 'mankey', 'mantine', 'mantyke', 'maractus', 'mareep', 'marill', 'marowak', 'marshtomp',
           'masquerain', 'mawile', 'medicham', 'meditite', 'meganium', 'meloetta-aria', 'meowth', 'mesprit',
           'metagross', 'metang', 'metapod', 'mew', 'mewtwo', 'mienfoo', 'mienshao', 'mightyena', 'milotic', 'miltank',
           'mime-jr', 'minccino', 'minun', 'misdreavus', 'mismagius', 'moltres', 'monferno', 'mothim', 'mr-mime',
           'mudkip', 'muk', 'munchlax', 'munna', 'murkrow', 'musharna', 'natu', 'nidoking', 'nidoqueen', 'nidoran-f',
           'nidoran-m', 'nidorina', 'nidorino', 'nincada', 'ninetales', 'ninjask', 'noctowl', 'nosepass', 'numel',
           'nuzleaf', 'octillery', 'oddish', 'omanyte', 'omastar', 'onix', 'oshawott', 'pachirisu', 'palkia',
           'palpitoad', 'panpour', 'pansage', 'pansear', 'paras', 'parasect', 'patrat', 'pawniard', 'pelipper',
           'persian', 'petilil', 'phanpy', 'phione', 'pichu', 'pidgeot', 'pidgeotto', 'pidgey', 'pidove', 'pignite',
           'pikachu', 'piloswine', 'pineco', 'pinsir', 'piplup', 'plusle', 'politoed', 'poliwag', 'poliwhirl',
           'poliwrath', 'ponyta', 'poochyena', 'porygon-z', 'porygon', 'porygon2', 'primeape', 'prinplup', 'probopass',
           'psyduck', 'pupitar', 'purrloin', 'purugly', 'quagsire', 'quilava', 'qwilfish', 'raichu', 'raikou', 'ralts',
           'rampardos', 'rapidash', 'raticate', 'rattata', 'rayquaza', 'regice', 'regigigas', 'regirock', 'registeel',
           'relicanth', 'remoraid', 'reshiram', 'reuniclus', 'rhydon', 'rhyhorn', 'rhyperior', 'riolu', 'roggenrola',
           'roselia', 'roserade', 'rotom', 'rufflet', 'sableye', 'salamence', 'samurott', 'sandile', 'sandshrew',
           'sandslash', 'sawk', 'sawsbuck', 'sceptile', 'scizor', 'scolipede', 'scrafty', 'scraggy', 'scyther',
           'seadra', 'seaking', 'sealeo', 'seedot', 'seel', 'seismitoad', 'sentret', 'serperior', 'servine', 'seviper',
           'sewaddle', 'sharpedo', 'shaymin', 'shedinja', 'shelgon', 'shellder', 'shellos', 'shelmet', 'shieldon',
           'shiftry', 'shinx', 'shroomish', 'shuckle', 'shuppet', 'sigilyph', 'silcoon', 'simipour', 'simisage',
           'simisear', 'skarmory', 'skiploom', 'skitty', 'skorupi', 'skuntank', 'slaking', 'slakoth', 'slowbro',
           'slowking', 'slowpoke', 'slugma', 'smeargle', 'smoochum', 'sneasel', 'snivy', 'snorlax', 'snorunt', 'snover',
           'snubbull', 'solosis', 'solrock', 'spearow', 'spheal', 'spinarak', 'spinda', 'spiritomb', 'spoink',
           'squirtle', 'stantler', 'staraptor', 'staravia', 'starly', 'starmie', 'staryu', 'steelix', 'stoutland',
           'stunfisk', 'stunky', 'sudowoodo', 'suicune', 'sunflora', 'sunkern', 'surskit', 'swablu', 'swadloon',
           'swalot', 'swampert', 'swanna', 'swellow', 'swinub', 'swoobat', 'taillow', 'tangela', 'tangrowth', 'tauros',
           'teddiursa', 'tentacool', 'tentacruel', 'tepig', 'terrakion', 'throh', 'thundurus', 'timburr', 'tirtouga',
           'togekiss', 'togepi', 'togetic', 'torchic', 'torkoal', 'tornadus', 'torterra', 'totodile', 'toxicroak',
           'tranquill', 'trapinch', 'treecko', 'tropius', 'trubbish', 'turtwig', 'tympole', 'tynamo', 'typhlosion',
           'tyranitar', 'tyrogue', 'umbreon', 'unfezant', 'unown', 'ursaring', 'uxie', 'vanillish', 'vanillite',
           'vanilluxe', 'vaporeon', 'venipede', 'venomoth', 'venonat', 'venusaur', 'vespiquen', 'vibrava', 'victini',
           'victreebel', 'vigoroth', 'vileplume', 'virizion', 'volbeat', 'volcarona', 'voltorb', 'vullaby', 'vulpix',
           'wailmer', 'wailord', 'walrein', 'wartortle', 'watchog', 'weavile', 'weedle', 'weepinbell', 'weezing',
           'whimsicott', 'whirlipede', 'whiscash', 'whismur', 'wigglytuff', 'wingull', 'wobbuffet', 'woobat', 'wooper',
           'wormadam-plant', 'wurmple', 'wynaut', 'xatu', 'yamask', 'yanma', 'yanmega', 'zangoose', 'zapdos',
           'zebstrika', 'zekrom', 'zigzagoon', 'zoroark', 'zorua', 'zubat', 'zweilous']
