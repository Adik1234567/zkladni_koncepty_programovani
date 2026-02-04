import math

# Vypočítání objemu krychle

str_krychle = 2 # veličina strany
def objem_krychle(str_krychle): # výpočet pro objem: a na 3
    return pow(str_krychle, 3)

print("Objem krychle je: " + str(objem_krychle(str_krychle))) # vepsání do konzole


# Vypočítání obsahu kruhu

prumer_kruhu = 6 # průměr kruhu
zaok_kruhu = 2 # zaokrouhleni na kolik desetinych míst
def obsah_kruhu(prumer_kruhu, zaok_kruhu): # výpočet kruhu pomocí: S = pi * r² , a je zde i napsáno na kolik desetinnych mist je to zaokrouhlené
    return round(pow((prumer_kruhu / 2), 2) * math.pi, zaok_kruhu)

print("Obvod kruhu je: " + str(obsah_kruhu(prumer_kruhu, zaok_kruhu)) + " a je zaokrouhlený na " + str(zaok_kruhu) + " desetinná místa")
# print obvodu kruhu kde jsem pouzil predesle cisla a zaokrouhleno


# Vypočítání obvodu kruhu se stejnými veličinami jako minule

def obvod_kruhu(prumer_kruhu, zaok_kruhu):
    return round(math.pi * prumer_kruhu, zaok_kruhu)
print("Obvod kruhu je: " + str(obvod_kruhu(prumer_kruhu, zaok_kruhu)) + " a je zaokrouhlený na " + str(zaok_kruhu) + " desetinná místa")


# Výpočet povrchu kvádru

v_kvadr = 3 # vyska strany
s_kvadr = 1 # šířka strany
d_kvadr = 7 # delky strany
def povrch_kvadr(v_kvadr, s_kvadr, d_kvadr): # vypocet pomocí: 2 * (v * s + s * d + d * v)
    return 2 * (v_kvadr * s_kvadr + s_kvadr * d_kvadr + d_kvadr * v_kvadr)

print("Povrch kvádru je: " + str(povrch_kvadr(v_kvadr, s_kvadr, d_kvadr))) # a zase výpis do konzole


# Výpočet 3 strany v trojúhelníku

a_troju = 6 # strana a
b_troju = 7 # strana b
zaok_troju = 4 # zaokrouhlení na kolik desetiných míst
def c_troju(a_troju, b_troju, zaok_troju): # vypocitani pomoci: odmocniny a na 2 + b na 2 a zaokrouhleni celeho vypoctu
    return round(math.sqrt(pow(a_troju, 2) + pow(b_troju, 2)), zaok_troju)

print("Strana c v trojúhelníku je: " + str(c_troju(a_troju, b_troju, zaok_troju)) + " a je zaokrouhlená na " + str(zaok_troju) + " desetinná místa") # zas print


# objem valec pomoci kruhu s vyskou kvadr

def objem_valec(obsah_kruhu, zaok_kruhu, v_kvadr):
    return obsah_kruhu(prumer_kruhu, zaok_kruhu) * v_kvadr
print("Objem valce je: " + str(objem_valec(obsah_kruhu, zaok_kruhu, v_kvadr)))