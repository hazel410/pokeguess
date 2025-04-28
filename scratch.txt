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
fuckstringsiguess = 0
rowt.reverse()

# DRAAAWWWWIIIIINNG
for browt in rowt:
    loopt = browt
    if even:
        loopy = posy - (offset / 2) - (offset * fuckstringsiguess)
    else:
        loopy = posy - (offset * (fuckstringsiguess + 1))
    looprend = font.render(loopt, True, colt)
    looprect = looprend.get_rect(center=[posx, loopy])
    S.blit(looprend, looprect)
    fuckstringsiguess += 1
fuckstringsiguess = 0
for erowb in rowb:
    loopt = erowb
    if even:
        loopy = posy + (offset / 2) + (offset * fuckstringsiguess)
    else:
        loopy = posy + (offset * (fuckstringsiguess + 1))
    looprend = font.render(loopt, True, colt)
    looprect = looprend.get_rect(center=[posx, loopy])
    S.blit(looprend, looprect)
    fuckstringsiguess += 1

    # draaaawing
    for rows in outrow:
        sizy.append(font.size(rows)[1])
    even = divmod(len(outrow), 2)[1] == 0
    offset = max(sizy) + pady
    if even:
        index = int(len(outrow) / 2)
        rowt = outrow[:index]
        rowb = outrow[index:]
        rowt.reverse()
        fuckstringsiguess = 0
        for erowt in rowt:
            loopt = erowt
            loopy = posy - (offset / 2) - (offset * fuckstringsiguess)
            looprend = font.render(loopt, True, colt)
            looprect = looprend.get_rect(center=[posx, loopy])
            S.blit(looprend, looprect)
            fuckstringsiguess += 1
        fuckstringsiguess = 0
        for erowb in rowb:
            loopt = erowb
            loopy = posy + (offset / 2) + (offset * fuckstringsiguess)
            looprend = font.render(loopt, True, colt)
            looprect = looprend.get_rect(center=[posx, loopy])
            S.blit(looprend, looprect)
            fuckstringsiguess += 1
    else:
        index = int((len(outrow) - 1) / 2)
        rowt = outrow[:index]
        rowm = outrow[index]
        rowb = outrow[(index + 1):]
        rowt.reverse()
        rend = font.render(rowm, True, colt)
        rect = rend.get_rect(center=[posx, posy])
        S.blit(rend, rect)
        fuckstringsiguess = 0
        for orowt in rowt:
            loopt = orowt
            loopy = posy - (offset * (fuckstringsiguess + 1))
            looprend = font.render(loopt, True, colt)
            looprect = looprend.get_rect(center=[posx, loopy])
            S.blit(looprend, looprect)
            fuckstringsiguess += 1
        fuckstringsiguess = 0
        for orowb in rowb:
            loopt = orowb
            loopy = posy + (offset * (fuckstringsiguess + 1))
            looprend = font.render(loopt, True, colt)
            looprect = looprend.get_rect(center=[posx, loopy])
            S.blit(looprend, looprect)
            fuckstringsiguess += 1