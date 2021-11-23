def paranda_komavead(lause):
    lause = lause.replace(" sest ", ", sest ")
    lause = lause.replace(" et ", ", et ")
    lause = lause.replace(" kuid ", ", kuid ")
    lause = lause.replace(" siis ", ", siis ")
    lause = lause.replace(" mis ", ", mis " )
    lause = lause.replace(" aga ", ", aga ")
    return lause
# paranda_komavead("Ma olen sinine sest et ma olen punane siis kui ma ei ole roheline")
fail1 = open("vigane.txt", encoding  = "UTF-8")
fail2 = open("parandatud.txt", "w", encoding = "UTF-8")
for line in fail1:
    parandus = paranda_komavead(line)
    fail2.write(parandus)
fail1.close()
fail2.close()
