# imports
from PIL import Image
import pandas as pd
import numpy as np
import random
import pygame
import time
import math

# pygame initializaitons
pygame.mixer.init()
pygame.init()

# General initializations
rootdir = 'pokeguess/'
gamemode = 1
running = True
cvs = rootdir + 'files/sheet_smart.csv'
smarttyp = "SSP-T"
smartgen = "SSP-G"
gifcount = 649
giflist = ['abomasnow', 'abra', 'absol', 'accelgor', 'aerodactyl', 'aggron', 'aipom', 'alakazam', 'alomomola',
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

"""
Notes on CSV requirements:

- Must store generation columns in interrupted ascending order from left to right
- Must store type information interrupted starting with normal from left to right
- The first row of the sheet must consist of questions to be asked for the corresponding column
- the second row of the sheet must consist of category names, which do not repeat
    - the category label for the names of the pokemon must be "Category"
    - the category label for mons in gen 1 must be "G1"
"""

# window
Wi = 720
Hi = 480
S = pygame.display.set_mode((Wi, Hi), flags=pygame.SCALED, vsync=1)
pygame.display.set_caption('PokéGuess V4')
clock = pygame.time.Clock()

# fonts and colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
green = (40, 120, 40)
neon = (120, 245, 66)
light_cornflower_blue_2 = (152, 196, 236)
light_cornflower_blue_1 = (100, 166, 225)
light_purple_1 = (148, 115, 200)
dark_magenta_2 = (126, 0, 70)
color_background = dark_magenta_2
font_32 = pygame.font.Font('freesansbold.ttf', 32)
font_24 = pygame.font.Font('freesansbold.ttf', 24)
font_40 = pygame.font.Font('freesansbold.ttf', 40)
font_18 = pygame.font.Font('freesansbold.ttf', 18)

# sounds!!
pygame.mixer.music.load(rootdir + 'files/mps/HGSS - Pewter City.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(loops=-1)
sfx_pop = pygame.mixer.Sound(rootdir + 'files/mps/pop.mp3')
sfx_yip = pygame.mixer.Sound(rootdir + 'files/mps/yippee.mp3')
sfx_bye = pygame.mixer.Sound(rootdir + 'files/mps/roblox-bye.mp3')
sfx_che = pygame.mixer.Sound(rootdir + 'files/mps/children-cheering.mp3')
sfx_cor = pygame.mixer.Sound(rootdir + 'files/mps/correct.mp3')
sfx_pip = pygame.mixer.Sound(rootdir + 'files/mps/metal-pipe-clang.mp3')
sfx_pop.set_volume(.1)
sfx_yip.set_volume(.1)
sfx_bye.set_volume(.1)
sfx_che.set_volume(.1)
sfx_cor.set_volume(.1)
sfx_pip.set_volume(.05)
mute = False

# silly easter egg
sillit = []
silmag = 10
gravity = 0
bouncey = -1
anglerange = (0, 359)
colislimrange = (7, 10)
sillyistbh = True
drawbounds = False
scrollhell = False


# text wrap function
def twrap(text, font, colt, posx, posy, lenx):
    """
    A function I made that horizontally wraps text

    :param text: string; the text you want wrapped
    :param font: pygame.font.Font; the font you want the text in
    :param colt: tuple, RGB format; the color you want the text to be
    :param posx: int; the x position you want the text to center
    :param posy: int; the y position you want the text to center
    :param lenx: int; the horizontal boundary length of the text
    """

    # initial assignments
    words = text.split()
    wordtot = len(words)
    padx = 10
    pady = .5
    wordnum = 0
    outrow = []
    stri = ""
    widt = lenx - (2 * padx)
    sizy = []

    # seperating into distinct lines
    while wordtot > wordnum:
        strb = stri
        stri = stri + words[wordnum]
        leni = font.size(stri)[0]
        if leni > widt:
            if font.size(words[wordnum])[0] > widt:
                print('ERROR: twrap seperation; text bigger than bounds')
                exit(3)
            else:
                strb = strb[:-1]
                outrow.append(strb)
                stri = ""
        else:
            if wordnum == wordtot - 1:
                outrow.append(stri)
            else:
                stri = stri + " "
            wordnum += 1

    # does some math
    for rows in outrow:
        sizy.append(font.size(rows)[1])
    even = divmod(len(outrow), 2)[1] == 0
    offset = max(sizy) + pady
    if even:
        index = int(len(outrow) / 2)
        rowt = outrow[:index]
        rowb = outrow[index:]
    else:
        index = int((len(outrow) - 1) / 2)
        rowt = outrow[:index]
        rowm = outrow[index]
        rowb = outrow[(index + 1):]
        rend = font.render(rowm, True, colt)
        rect = rend.get_rect(center=[posx, posy])
        S.blit(rend, rect)
    rowt.reverse()

    # DRAAAWWWWIIIIINNG
    weirdindex = 0
    for browt in rowt:
        loopt = browt
        if even:
            loopy = posy - (offset / 2) - (offset * weirdindex)
        else:
            loopy = posy - (offset * (weirdindex + 1))
        looprend = font.render(loopt, True, colt)
        looprect = looprend.get_rect(center=[posx, loopy])
        S.blit(looprend, looprect)
        weirdindex += 1
    weirdindex = 0
    for erowb in rowb:
        loopt = erowb
        if even:
            loopy = posy + (offset / 2) + (offset * weirdindex)
        else:
            loopy = posy + (offset * (weirdindex + 1))
        looprend = font.render(loopt, True, colt)
        looprect = looprend.get_rect(center=[posx, loopy])
        S.blit(looprend, looprect)
        weirdindex += 1


# subset sum function, for subset of len three
def ssp3(numbers, target):
    """
    A function I made that brute forces a specific subset sum problem

    Tries to grab 3 points of data that are closest to the target

    :returns a tuple of [sum of items, index of items]

    :param numbers: tuple/list; the set of numbers to be input. must contain at least four items
    :param target: int; the goal to achieve
    """

    arr = numbers
    tar = target
    smm = sum(numbers) * 2
    ind = []
    for i in range(len(arr)):
        if arr[i] > 0:
            for j in range(i + 1, len(arr)):
                if arr[j] > 0:
                    for k in range(j + 1, len(arr)):
                        if arr[k] > 0:
                            if abs(tar - smm) > abs(tar - (arr[i] + arr[j] + arr[k])):
                                smm = arr[i] + arr[j] + arr[k]
                                ind = [i, j, k]
    if len(ind) != 3:
        ind = [0, 0, 0]
        smm = 0
    return smm, ind


# export function -- god wish me luck
def export():
    """
    a function that solves every pokemon and exports that data

    :return: nothing
    """
    global running
    
    staticgame = Gameplay()
    numberomon = len(staticgame.mdfr)
    csvinterme = {}
    t0 = time.perf_counter()
    for pokemon in range(numberomon):
        csvinterme[staticgame.mdfr.iloc[pokemon]['Category']] = monsolver(pokemon)
        percent = round((pokemon / numberomon) * 100, 2)
        t1 = time.perf_counter()
        te = t1 - t0
        pygame.draw.rect(S, color_background, (W * (2 / 5), H / 4, 1000, 1000))
        pygame.draw.rect(S, gray, ((W / 2) - 50, (H / 2), 200, 50))
        pygame.draw.rect(S, white, ((W / 2) - 50, (H / 2), round(percent * 2), 50))
        perrend = font_24.render(str(percent) + "%", True, white)
        monrend = font_24.render('mons left: ' + str(numberomon - pokemon), True, white)
        timrend = font_24.render('time spent: ' + str(round(te)) + ' secs', True, white)
        perrect = perrend.get_rect(topleft=[(W / 2) + 175, (H / 2) + 12])
        monrect = monrend.get_rect(topleft=[(W / 2) - 45, (H / 2) - 40])
        timrect = timrend.get_rect(topleft=[(W / 2) - 45, (H / 2) + 75])
        S.blit(perrend, perrect)
        S.blit(monrend, monrect)
        S.blit(timrend, timrect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
        pygame.display.flip()
    file = pd.DataFrame(dict([(key, pd.Series(value)) for key, value in csvinterme.items()]))
    filetrans = file.transpose()
    filetrans.to_csv(rootdir + 'out.csv')
    pygame.mixer.find_channel(True).play(sfx_cor)


def monsolver(pokemon_number):
    """
    solves a given pokemon and returns data

    :param pokemon_number: int; the number of the pokemon being solved for
    :return: list; data yk
    """

    main = Gameplay()
    monu = pokemon_number
    info = main.mdfr.iloc[monu]
    val = 0
    if main.stal:
        val = 1 if info['Category'] == main.mdic[main.clit[0]][0] else 0
    elif main.bcat == smarttyp:
        val = info[main.ssct[0]] + info[main.ssct[1]] + info[main.ssct[2]]
    elif main.bcat == smartgen:
        val = info[main.sscg[0]] + info[main.sscg[1]] + info[main.sscg[2]]
    elif main.bcat in main.clit[0:(len(main.clit) - 2)]:
        val = info[main.bcat]
    ans = 'Yes' if val > 0 else 'No'
    output = ['Question ' + str(main.qnum), main.pnum, main.bcat, ans, main.sums]
    while main.pnum > 1:
        if main.stal:
            val = 1 if info['Category'] == main.mdic[main.clit[0]][0] else 0
        elif main.bcat == smarttyp:
            val = info[main.ssct[0]] + info[main.ssct[1]] + info[main.ssct[2]]
        elif main.bcat == smartgen:
            val = info[main.sscg[0]] + info[main.sscg[1]] + info[main.sscg[2]]
        elif main.bcat in main.clit[0:(len(main.clit) - 2)]:
            val = info[main.bcat]
        ans = 'Yes' if val > 0 else 'No'
        main.input(ans)
        main.upkeep()
        if main.stal and main.pnum > 1:
            output.append('Question ' + str(main.qnum))
            output.append(main.pnum)
            output.append('Stalemate')
            output.append(ans)
            output.append(main.sums)
        elif main.bcat == smarttyp:
            output.append('Question ' + str(main.qnum))
            output.append(main.pnum)
            output.append(main.ssct)
            output.append(ans)
            output.append(main.sums)
        elif main.bcat == smartgen:
            output.append('Question ' + str(main.qnum))
            output.append(main.pnum)
            output.append(main.sscg)
            output.append(ans)
            output.append(main.sums)
        elif main.bcat != 'Category':
            output.append('Question ' + str(main.qnum))
            output.append(main.pnum)
            output.append(main.bcat)
            output.append(ans)
            output.append(main.sums)
        else:
            pass

    return output


# gif worker thing
class Gif:
    def __init__(self, filepath, scale=3):
        self.gifi = Image.open(filepath)
        self.frms = 1
        self.indx = 0
        self.libr = []
        self.disp = []
        while True:
            try:
                self.gifi.seek(self.frms)
                self.frms += 1
            except EOFError:
                break
        for frames in range(self.frms):
            self.gifi.seek(frames)
            frame_rgba = self.gifi.convert("RGBA")
            image = pygame.image.fromstring(frame_rgba.tobytes(), frame_rgba.size, "RGBA")
            image = pygame.transform.scale_by(image, scale)
            self.libr.append(image)
        self.size = self.libr[0].get_size()

    def display(self, position, flipx=False, speed=1, orient='center'):
        global S
        self.disp = self.libr[math.floor(self.indx)]
        if orient == 'center':
            S.blit(pygame.transform.flip(self.disp, flipx, False),
                   [position[0] - (self.size[0] / 2), position[1] - (self.size[1] / 2)])
        elif orient == 'topleft':
            S.blit(pygame.transform.flip(self.disp, flipx, False), position)
        if self.indx == len(self.libr) - 1:
            self.indx = 0
        else:
            self.indx += .25 * speed


# button class omg yay
class Button:
    # attributes = [text, font, posx, posy, lenx, leny, mode, hide, back]
    def __init__(self, text, draw, mode, hide=False, back=True, font=font_32,
                 colt=white, colb=light_cornflower_blue_2, colh=light_cornflower_blue_1, wrap=False):
        """
        Initializes a Button for use in my game.

        :param text: string; the text present on the button
        :param draw: tuple; [center x position to brnd, center y position to brnd, width of button, height of button]
        :param mode: int; for handling mode changes from workingbuttons, see Button.click for more
        :param hide: boolean; if true, button is hidden until hovered
        :param back: boolean; if false, button is pure text. you can still click it
        :param font: pygame.font.Font; for specifying a font for the button outside from the preset
        :param colt: tuple; for specifying a text color outside from the preset
        :param colb: tuple; for specifying a button color outside from the preset
        :param colh: tuple; for specifying a button hover color outside from the preset
        :param wrap: boolean; if true, horizontally wraps the text to the width of the button
        """

        self.text = text
        self.posx = draw[0]
        self.posy = draw[1]
        self.lenx = draw[2]
        self.leny = draw[3]
        self.mode = mode
        self.hide = hide
        self.back = back
        self.font = font
        self.colt = colt
        self.colb = colb
        self.colh = colh
        self.wrap = wrap
        self.rend = self.font.render(self.text, True, self.colt)
        self.size = self.font.size(self.text)
        self.sizx = self.size[0]
        self.sizy = self.size[1]
        self.rect = self.rend.get_rect(center=[self.posx, self.posy])
        self.draw = [round(self.posx - (self.lenx / 2)), round(self.posy - (self.leny / 2)), self.lenx, self.leny]
        self.xlimL = self.draw[0]
        self.xlimU = self.draw[0] + self.draw[2]
        self.ylimL = self.draw[1]
        self.ylimU = self.draw[1] + self.draw[3]

    def draw(self):
        if not self.hide:
            if self.back:
                pygame.draw.rect(S, self.colb, self.draw)
            if self.wrap:
                twrap(self.text, self.font, self.colt, self.posx, self.posy, self.lenx)
            else:
                S.blit(self.rend, self.rect)

    def hover(self):
        if self.back:
            if self.xlimL <= M[0] <= self.xlimU and self.ylimL <= M[1] <= self.ylimU:
                pygame.draw.rect(S, self.colh, self.draw)
                if self.wrap:
                    twrap(self.text, self.font, self.colt, self.posx, self.posy, self.lenx)
                else:
                    S.blit(self.rend, self.rect)

    def click(self):
        global gamemode
        global running
        global sillit
        global sillyistbh
        global gaming
        global W
        global H
        global creature
        global mute
        global scrollhell
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.xlimL <= M[0] <= self.xlimU and self.ylimL <= M[1] <= self.ylimU:
                if self.mode != 0:  # if button is supposed to do something
                    if pygame.mouse.get_pressed()[0]:  # handles left click inputs
                        if self.mode > 0:
                            gamemode = self.mode
                            creature = Gif(rootdir + 'files/sprites/' + giflist[random.randrange(0, gifcount - 1)] + '.gif')
                            if self.mode != 5:
                                pygame.mixer.pause()
                        elif self.mode == -1:
                            running = False
                        elif self.mode == -3:
                            sillit.append(TBH())
                        elif self.mode == -7:
                            if not mute:
                                sfx_pop.set_volume(0)
                                sfx_yip.set_volume(0)
                                sfx_bye.set_volume(0)
                                sfx_che.set_volume(0)
                                sfx_cor.set_volume(0)
                                sfx_pip.set_volume(0)
                                mute = True
                            else:
                                sfx_pop.set_volume(.1)
                                sfx_yip.set_volume(.1)
                                sfx_bye.set_volume(.1)
                                sfx_che.set_volume(.1)
                                sfx_cor.set_volume(.1)
                                sfx_pip.set_volume(.05)
                                mute = False
                        elif self.mode == -8:
                            scrollhell = not scrollhell
                        elif self.mode == -9:
                            export()
                        elif self.mode == -10:
                            sillyistbh = not sillyistbh
                        elif self.mode == -11:
                            W = Wi
                            H = Hi
                        elif self.mode == -13:
                            gaming.main('Yes')
                        elif self.mode == -14:
                            gaming.main('No')
                        elif self.mode == -15:
                            gaming.main('Undo')
                        else:
                            print("ERROR: Button.click; no match found")
                            exit(4)
                    elif pygame.mouse.get_pressed()[2]:  # handles right click inputs
                        if self.mode == -3:
                            sillit = []
                            pygame.mixer.pause()
                    elif scrollhell and self.mode == -3:  # if scroll hell, lets you scroll on easter egg
                        sillit.append(TBH())


# creature classing
class TBH:
    def __init__(self):
        pygame.mixer.find_channel(True).play(sfx_yip)
        angle = random.randrange(1, 360) * (np.pi / 180)
        self.type = sillyistbh
        self.image = pygame.image.load(rootdir + 'files/tbh.png') if self.type else Gif(rootdir + 'files/blahaj.gif', scale=1)
        self.size = self.image.get_size() if self.type else self.image.size
        self.xpos = random.randrange(0, round(W - (self.size[0] / 2)))
        self.ypos = random.randrange(0, round(H - (self.size[1] / 2)))
        self.xvel = silmag * np.cos(angle)
        self.yvel = silmag * np.sin(angle)
        self.colislim = random.randrange(colislimrange[0], colislimrange[1])
        self.coli = 0
        self.dele = False

    def posupdate(self):
        self.yvel = self.yvel + gravity
        self.xpos = self.xpos + self.xvel
        self.ypos = self.ypos + self.yvel
        if self.coli <= self.colislim:
            if self.xpos > W - self.size[0] or self.xpos < 0:
                self.xpos = min([0, W - self.size[0]], key=lambda z: abs(z - self.xpos))
                self.xvel = self.xvel * bouncey
                self.coli += 1
                pygame.mixer.find_channel(True).play(sfx_pip)
            if self.ypos > H - self.size[1] or self.ypos < 0:
                self.ypos = min([0, H - self.size[1]], key=lambda z: abs(z - self.ypos))
                self.yvel = self.yvel * bouncey
                self.coli += 1
                pygame.mixer.find_channel(True).play(sfx_pip)
        elif self.xpos > W or self.xpos < 0 - self.size[0] or self.ypos > H:
            self.dele = True
            pygame.mixer.find_channel(True).play(sfx_bye)


# gameplay classing
class Gameplay:

    def __init__(self):
        # Initializations
        self.shrt = False
        self.qnum = 1
        self.mdfr = pd.read_csv(cvs, skiprows=1)
        self.mdic = pd.DataFrame.to_dict(self.mdfr, orient='list')
        self.clit = list(self.mdic.keys())
        self.qdic = pd.DataFrame.to_dict(pd.read_csv(cvs, nrows=0), orient='list')
        self.qlit = list(self.qdic.keys())
        self.pnum = len(self.mdfr)
        self.dfvc = []
        self.stvc = []
        self.sgvc = []
        self.cnum = len(self.qlit)
        # Sums
        self.sums = [0]
        loopvar = 1
        while loopvar < self.cnum:
            self.sums.append(sum(self.mdic[self.clit[loopvar]]))
            loopvar += 1
        # Smart Stuff
        self.indt = self.clit.index('Normal')
        self.indg = self.clit.index('G1')
        self.outt = [1] * 18
        self.outg = [1] * 9
        self.sumt = self.sums[self.indt:(self.indt + 17)]
        self.sumg = self.sums[self.indg:(self.indg + 8)]
        self.ssit = list(map(lambda x, y: x * y, self.outt, self.sumt))
        self.ssig = list(map(lambda x, y: x * y, self.outg, self.sumg))
        self.ssvt = ssp3(self.ssit, self.pnum / 2)
        self.ssvg = ssp3(self.ssig, self.pnum / 2)
        self.ssct = (self.clit[self.ssvt[1][0] + self.indt], self.clit[self.ssvt[1][1] + self.indt],
                     self.clit[self.ssvt[1][2] + self.indt])
        self.sscg = (self.clit[self.ssvg[1][0] + self.indg], self.clit[self.ssvg[1][1] + self.indg],
                     self.clit[self.ssvg[1][2] + self.indg])
        self.ssqt = "Is your pokemon " + self.ssct[0] + " " + self.ssct[1] + " or " + self.ssct[2] + " type?"
        self.ssqg = ("Was your pokemon introduced in  gens " + str(self.ssvg[1][0] + 1) + " " +
                     str(self.ssvg[1][1] + 1) + " or " + str(self.ssvg[1][2] + 1)) + "?"
        self.sums.append(self.ssvt[0])
        self.sums.append(self.ssvg[0])
        self.clit.append(smarttyp)
        self.clit.append(smartgen)
        # Best Values and booleans
        self.bval = min(self.sums, key=lambda x: abs(x - self.pnum / 2))
        self.bcat = self.clit[self.sums.index(self.bval)]
        self.stal = self.bval == 0 or self.bval == self.pnum
        self.undo = len(self.dfvc) >= 2
        self.wins = True
        # Questions
        if self.bcat == smarttyp:
            self.bque = self.ssqt
            self.outt[self.ssvt[1][0]] = 0
            self.outt[self.ssvt[1][1]] = 0
            self.outt[self.ssvt[1][2]] = 0
        elif self.bcat == smartgen:
            self.bque = self.ssqg
            self.outg[self.ssvg[1][0]] = 0
            self.outg[self.ssvg[1][1]] = 0
            self.outg[self.ssvg[1][2]] = 0
        elif self.bcat in self.clit[0:(len(self.clit) - 2)]:
            self.bque = self.qlit[self.sums.index(self.bval)]

    def input(self, ans):
        global gamemode
        global creature
        if ans == 'Undo':
            if self.undo:
                offset = 2 if self.pnum > 1 else 1
                self.mdfr = self.dfvc[self.qnum - offset]
                self.outt = self.stvc[self.qnum - offset]
                self.outg = self.sgvc[self.qnum - offset]
                del self.dfvc[self.qnum - offset]
                del self.stvc[self.qnum - offset]
                del self.sgvc[self.qnum - offset]
                self.qnum += (1 - offset)
                self.shrt = False
        elif ans == 'Yes':
            self.dfvc.append(self.mdfr)
            self.stvc.append(list(self.outt))
            self.sgvc.append(list(self.outg))
            self.qnum += 1
            if self.pnum == 1:
                gamemode = 5
                creature = Gif(rootdir + 'files/sprites/' + giflist[random.randrange(0, gifcount - 1)] + '.gif')
            elif self.stal:
                self.shrt = True
                self.mdfr = (self.mdfr.drop(self.mdfr[self.mdfr['Category'] !=
                                                      self.mdfr['Category'][self.mdfr.first_valid_index()]].index))
            elif self.bcat == smarttyp:
                self.outt[self.ssvt[1][0]] = 0
                self.outt[self.ssvt[1][1]] = 0
                self.outt[self.ssvt[1][2]] = 0
                msk = (self.mdfr[self.ssct[0]].eq(0) &
                       self.mdfr[self.ssct[1]].eq(0) &
                       self.mdfr[self.ssct[2]].eq(0))
                self.mdfr = self.mdfr.drop(self.mdfr.index[msk])
            elif self.bcat == smartgen:
                self.outg[self.ssvg[1][0]] = 0
                self.outg[self.ssvg[1][1]] = 0
                self.outg[self.ssvg[1][2]] = 0
                msk = (self.mdfr[self.sscg[0]].eq(0) &
                       self.mdfr[self.sscg[1]].eq(0) &
                       self.mdfr[self.sscg[2]].eq(0))
                self.mdfr = self.mdfr.drop(self.mdfr.index[msk])
            elif self.bcat in self.clit[0:(len(self.clit) - 2)]:
                self.mdfr = self.mdfr.drop(self.mdfr[self.mdfr[self.bcat] == 0].index)
        elif ans == 'No':
            self.dfvc.append(self.mdfr)
            self.stvc.append(list(self.outt))
            self.sgvc.append(list(self.outg))
            self.qnum += 1
            if self.pnum == 1:
                gamemode = 1
                creature = Gif(rootdir + 'files/sprites/' + giflist[random.randrange(0, gifcount - 1)] + '.gif')
            elif self.stal:
                self.mdfr = (self.mdfr.drop(self.mdfr[self.mdfr['Category'] ==
                                                      self.mdfr['Category'][self.mdfr.first_valid_index()]].index))
            elif self.bcat == smarttyp:
                self.outt[self.ssvt[1][0]] = 0
                self.outt[self.ssvt[1][1]] = 0
                self.outt[self.ssvt[1][2]] = 0
                self.mdfr = self.mdfr.drop(self.mdfr[self.mdfr[self.ssct[0]] == 1].index)
                self.mdfr = self.mdfr.drop(self.mdfr[self.mdfr[self.ssct[1]] == 1].index)
                self.mdfr = self.mdfr.drop(self.mdfr[self.mdfr[self.ssct[2]] == 1].index)
            elif self.bcat == smartgen:
                self.outg[self.ssvg[1][0]] = 0
                self.outg[self.ssvg[1][1]] = 0
                self.outg[self.ssvg[1][2]] = 0
                self.mdfr = self.mdfr.drop(self.mdfr[self.mdfr[self.sscg[0]] == 1].index)
                self.mdfr = self.mdfr.drop(self.mdfr[self.mdfr[self.sscg[1]] == 1].index)
                self.mdfr = self.mdfr.drop(self.mdfr[self.mdfr[self.sscg[2]] == 1].index)
            elif self.bcat in self.clit[0:(len(self.clit) - 2)]:
                self.mdfr = self.mdfr.drop(self.mdfr[self.mdfr[self.bcat] == 1].index)
        else:
            print('ERROR: Input ANS invalid')
            exit(8)

    def upkeep(self):
        # basic items
        self.mdic = pd.DataFrame.to_dict(self.mdfr, orient='list')
        self.pnum = len(self.mdfr)
        # ending fix
        if self.pnum == 1:
            self.qnum -= 1
        # ending sfx
        if self.pnum == 1 and self.wins and gamemode == 4:
            pygame.mixer.find_channel(True).play(sfx_che)
            self.wins = False
        # resums qvalues
        self.sums = [0]
        loopvar = 1
        while loopvar < self.cnum:
            self.sums.append(sum(self.mdic[self.clit[loopvar]]))
            loopvar += 1
        # calculates subset sum vals, cats, ques, and appends sums
        self.sumt = self.sums[self.indt:(self.indt + 17)]
        self.ssit = list(map(lambda x, y: x * y, self.outt, self.sumt))
        self.ssvt = ssp3(self.ssit, self.pnum / 2)
        self.ssct = (self.clit[self.ssvt[1][0] + self.indt], self.clit[self.ssvt[1][1] + self.indt],
                     self.clit[self.ssvt[1][2] + self.indt])
        self.ssqt = "Is your pokemon " + self.ssct[0] + " " + self.ssct[1] + " or " + self.ssct[2] + " type?"
        self.sums.append(self.ssvt[0])
        self.sumg = self.sums[self.indg:(self.indg + 17)]
        self.ssig = list(map(lambda x, y: x * y, self.outg, self.sumg))
        self.ssvg = ssp3(self.ssig, self.pnum / 2)
        self.sscg = (self.clit[self.ssvg[1][0] + self.indg], self.clit[self.ssvg[1][1] + self.indg],
                     self.clit[self.ssvg[1][2] + self.indg])
        self.ssqg = ("Was your pokemon introduced in  gens " + str(self.ssvg[1][0] + 1) + " " +
                     str(self.ssvg[1][1] + 1) + " or " + str(self.ssvg[1][2] + 1)) + "?"
        self.sums.append(self.ssvg[0])
        # Refreshes best val, cat, and stale / undo
        self.bval = min(self.sums, key=lambda x: abs(x - self.pnum / 2))
        self.bcat = self.clit[self.sums.index(self.bval)]
        self.stal = self.bval <= 1 or self.bval >= self.pnum - 1
        self.undo = len(self.dfvc) >= 1

    def question(self):
        if self.pnum == 1 & self.shrt:
            self.bque = "Yippee!! Do you want to play again?"
        elif self.pnum == 1:
            self.bque = 'Your pokemon is ' + self.mdic[self.clit[0]][0] + "!! Do you want to play again?"
        elif self.stal:
            self.bque = "Is your pokemon " + self.mdic[self.clit[0]][0] + "?"
        elif self.bcat == smarttyp:
            self.bque = self.ssqt
        elif self.bcat == smartgen:
            self.bque = self.ssqg
        elif self.bcat in self.clit[0:(len(self.clit) - 2)]:
            self.bque = self.qlit[self.sums.index(self.bval)]
        else:
            print('Error: Gaming.question could not find match')
            exit(5)

    @staticmethod
    def main(ans):
        global gamemode
        Gameplay.input(gaming, ans)
        Gameplay.upkeep(gaming)
        Gameplay.question(gaming)


# gameplay initializations
resetgm = False
gaming = Gameplay()
quenumb = "Question: " + str(gaming.qnum)
monnumb = "Pokémon Left: " + str(gaming.pnum)
quetext = gaming.bque
creature = Gif(rootdir + 'files/sprites/' + giflist[random.randrange(0, gifcount - 1)] + '.gif')

# Gameplay Loop
while running:

    # General Maintenance
    pygame.display.flip()
    clock.tick(60)
    M = pygame.mouse.get_pos()
    W = S.get_size()[0]
    H = S.get_size()[1]
    buttons = []
    S.fill(color_background)
    FPS = clock.get_fps()

    # Buttons
    if gamemode == 1:  # Home
        creature.display([W * .7, H / 2])
        buttons = [Button("PokéGuess V4", (W / 2, 32, -1, -1), 0, back=False, font=font_40),
                   Button("Play", (W / 5, H * (1 / 5) + 16, 160, 70), 4),
                   Button("Settings", (W / 5, H * (2 / 5) + 16, 160, 70), 2),
                   Button("Credits", (W / 5, H * (3 / 5) + 16, 160, 70), 3),
                   Button("Exit", (W / 5, H * (4 / 5) + 16, 160, 70), -1)]
    elif gamemode == 2:  # Settings
        creature.display([W * .7, H / 2])
        muted = "Unmute SFX" if mute else "Mute SFX"
        silbut = "Blåhaj" if sillyistbh else "TBH"
        scroll = "chill" if scrollhell else "hell"
        buttons = [Button("Settings", (W / 2, 32, -1, -1), 0, font=font_40),
                   Button(muted, (W / 5, H * (1 / 5) + 16, 160, 70), -7, font=font_24),
                   Button("DEV: exp", (W / 5, H * (2 / 5) + 16, 160, 70), -9),
                   Button("Home", (W - 36 - 5, 20 + 5, 72, 40), 1, font=font_24),
                   Button(silbut, (W / 5, H * (3 / 5) + 16, 160, 70), -10),
                   Button(scroll, (W / 5, H * (4 / 5) + 16, 160, 70), -8)]
    elif gamemode == 3:  # Credits
        gartext = "thanks for helping me design the ux of this game! :]"
        jaxtext = "thanks for helping me learn python! :D"
        garmage = pygame.image.load(rootdir + 'files/garrett.png')
        jaxmage = pygame.image.load(rootdir + 'files/jax.png')
        S.blit(garmage, (50, 50))
        S.blit(jaxmage, (50, 150))
        buttons = [Button("Credits", (W / 2, 32, -1, -1), 0, font=font_40),
                   Button("Home", (W - 36 - 5, 20 + 5, 72, 40), 1, font=font_24),
                   Button(gartext, (W / 2, 120, 350, 10), 0, font=font_24, wrap=True, back=False),
                   Button(jaxtext, (W / 2, 240, 350, 10), 0, font=font_24, wrap=True, back=False)]
    elif gamemode == 4:  # Gameplay
        # creature.display([W * .3, H / 2], flipx=True)
        colundo = light_cornflower_blue_1 if gaming.undo else gray
        quenumb = "Question: " + str(gaming.qnum)
        monnumb = "Pokémon Left: " + str(gaming.pnum)
        quetext = gaming.bque
        resetgm = True
        buttons = [Button("Home", (W - 36 - 5, 20 + 5, 72, 40), 1, font=font_24),
                   Button('', (W * (23 / 32), H * .17, 250, 2), 0, colb=white, colh=white),
                   Button("No", (W * (13 / 16), H * .75, 120, 75), -14, font=font_40),
                   Button("Yes", (W * (10 / 16), H * .75, 120, 75), -13, font=font_40),
                   Button("Undo", (W * (23 / 32), H * .9, 252, 50), -15, colh=colundo),
                   Button(quenumb, (W * (23 / 32), H * .08, -1, -1), 0),
                   Button(monnumb, (W * (23 / 32), H * .14, -1, -1), 0, font=font_24),
                   Button(quetext, (W * (23 / 32), H * (2 / 5), 252, 200), 0,
                          font=font_24, wrap=True, colb=gray, colh=gray)]
    elif gamemode == 5:  # Retry
        # preserving gameplay so theres not that flash of blank screen
        # creature.display([W * .3, H / 2], flipx=True)
        colundo = light_cornflower_blue_1 if gaming.undo else gray
        quenumb = "Question: " + str(gaming.qnum)
        monnumb = "Pokémon Left: " + str(gaming.pnum)
        quetext = gaming.bque
        buttons = [Button("Home", (W - 36 - 5, 20 + 5, 72, 40), 1, font=font_24),
                   Button('', (W * (23 / 32), H * .17, 250, 2), 0, colb=white, colh=white),
                   Button("No", (W * (13 / 16), H * .75, 120, 75), -14, font=font_40),
                   Button("Yes", (W * (10 / 16), H * .75, 120, 75), -13, font=font_40),
                   Button("Undo", (W * (23 / 32), H * .9, 252, 50), -15, colh=colundo),
                   Button(quenumb, (W * (23 / 32), H * .08, -1, -1), 0),
                   Button(monnumb, (W * (23 / 32), H * .14, -1, -1), 0, font=font_24),
                   Button(quetext, (W * (23 / 32), H * (2 / 5), 252, 200), 0,
                          font=font_24, wrap=True, colb=gray, colh=gray)]
        # actually flipping the gamemode
        gamemode = 4
        gaming = Gameplay()

    # Resets game mode if we leave the play screen
    if resetgm and gamemode != 4:
        gaming = Gameplay()
        resetgm = False

    # persistent buttons
    buttons.append(Button("FPS: " + str(round(FPS)), (50, 25, 72, 40), 0, font=font_24, back=False))
    buttons.append(Button('Silly', (30, H - 25, 50, 30), -3, font=font_18, hide=True))

    # Button Draw Loop
    for bd in buttons[:]:
        Button.draw(bd)

    # Hovering Loop
    for bh in buttons[:]:
        Button.hover(bh)

    # Input Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for bi in buttons[:]:
            Button.click(bi)

    # sillies
    for obj in sillit[:]:

        # updates physics
        obj.posupdate()

        # draws debug bounds if set
        if drawbounds:
            pygame.draw.circle(S, neon, [obj.xpos, obj.ypos], 7)
            pygame.draw.circle(S, neon, [obj.xpos + obj.size[0], obj.ypos], 7)
            pygame.draw.circle(S, neon, [obj.xpos + obj.size[0], obj.ypos + obj.size[1]], 7)
            pygame.draw.circle(S, neon, [obj.xpos, obj.ypos + obj.size[1]], 7)

        # draws the silly
        if obj.type:
            S.blit(obj.image, [obj.xpos, obj.ypos])
        else:
            obj.image.display([obj.xpos, obj.ypos], speed=4, orient='topleft')

        # deletes the sillies
        if obj.dele:
            sillit.remove(obj)

# If Program Stops Running
pygame.quit()
quit(0)
