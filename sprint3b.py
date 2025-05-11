# 1
def salam():
    print("Salam, Dünya!")
print("-------------------------------")
# 2
def kub_hesabla(n):
    return n ** 3
print("-------------------------------")

# 3
def birlesdir(soz1, soz2):
    return soz1 + " " + soz2
print("-------------------------------")

# 4
def cap_et(lst):
    for item in lst:
        print(item)
print("-------------------------------")

# 5
def toplam(*args):
    return sum(args)
print("-------------------------------")

# 6
def ortalama(*args):
    if len(args) == 0:
        return "Rəqəm yoxdur"
    return sum(args) / len(args)

# 7
def adlar_rəqəmlər(**kwargs):
    for ad, rəqəm in kwargs.items():
        print(f"ad: {ad}, rəqəm: {rəqəm}")

# 8
def tip_yoxla(dəyər):
    if isinstance(dəyər, str):
        print("mətn")
    elif isinstance(dəyər, (int, float)):
        print("rəqəm")
    else:
        print("başqa")

# 9
def yas_kateqoriya():
    yas = int(input("Yaşınızı daxil edin: "))
    if yas < 18:
        print("Gənc")
    else:
        print("Yetkin")

# 10
def soz_uzunluq():
    soz = input("Söz daxil edin: ")
    print(len(soz))

salam()
print(kub_hesabla(3))
print(birlesdir("Salam", "Dünya"))
cap_et(["alma", "armud", "banan"])
print(toplam(1, 2, 3))
print(ortalama(4, 8, 12))
print(ortalama())
adlar_rəqəmlər(Ayşə=1, Murad=2)
tip_yoxla("söz")
tip_yoxla(100)
tip_yoxla([1, 2, 3])
