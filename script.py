import math

# Vypočítání objemu krychle

str_krychle = 2 # veličina strany
objem_krychle = pow(str_krychle, 3) # výpočet pro objem: a na 3

print("Objem krychle je: " + str(objem_krychle)) # vepsání do konzole


# Vypočítání obsahu kruhu

prumer_kruhu = 5 # průměr kruhu
zaok_kruhu = 2 # zaokrouhleni na kolik desetinych míst
obsah_kruhu = round(pow((prumer_kruhu / 2), 2) * math.pi, zaok_kruhu)# výpočet kruhu pomocí: S = pi * r² , a je zde i napsáno na kolik desetinnych mist je to zaokrouhlené

print("Obvod kruhu je: " + str(obsah_kruhu) + " a je zaokrouhlený na " + str(zaok_kruhu) + " desetinná místa")
# print obvodu kruhu kde jsem pouzil predesle cisla a zaokrouhleno


# Vypočítání obvodu kruhu se stejnými veličinami jako minule

obvod_kruhu = round(math.pi * prumer_kruhu, zaok_kruhu)
print("Obvod kruhu je: " + str(obvod_kruhu) + " a je zaokrouhlený na " + str(zaok_kruhu) + " desetinná místa")


# Výpočet povrchu kvádru

v_kvadr = 3 # vyska strany
s_kvadr = 1 # šířka strany
d_kvadr = 7 # delky strany
povrch_kvadr = 2 * (v_kvadr * s_kvadr + s_kvadr * d_kvadr + d_kvadr * v_kvadr) # vypocet pomocí: 2 * (v * s + s * d + d * v)

print("Povrch kvádru je: " + str(povrch_kvadr)) # a zase výpis do konzole


# Výpočet 3 strany v trojúhelníku

a_troju = 6 # strana a
b_troju = 7 # strana b
zaok_troju = 4 # zaokrouhlení na kolik desetiných míst
c_troju = round(math.sqrt(pow(a_troju, 2) + pow(b_troju, 2)), zaok_troju) # vypocitani pomoci: odmocniny a na 2 + b na 2 a zaokrouhleni celeho vypoctu

print("Strana c v trojúhelníku je: " + str(c_troju) + " a je zaokrouhlená na " + str(zaok_troju) + " desetinná místa") # zas print


# objem valec pomoci kruhu s vyskou kvadr

objem_valec = obsah_kruhu * v_kvadr
print("Objem valce je: " + str(objem_valec))