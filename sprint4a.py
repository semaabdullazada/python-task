# 1) Hesablama funksiyası
def hesablama():
    try:
        a = float(input("Birinci rəqəmi daxil edin: "))
        b = float(input("İkinci rəqəmi daxil edin: "))
        əməl = input("Əməliyyatı daxil edin (+, -, *, /): ")

        if əməl == "+":
            print("Nəticə:", a + b)
        elif əməl == "-":
            print("Nəticə:", a - b)
        elif əməl == "*":
            print("Nəticə:", a * b)
        elif əməl == "/":
            if b == 0:
                print("0-a bölmə yoxdur.")
            else:
                print("Nəticə:", a / b)
        else:
            print("Yanlış əməliyyat simvolu!")
    except ValueError:
        print("Xəta: Zəhmət olmasa rəqəm daxil edin.")
    except TypeError:
        print("Xəta: Uyğunsuz tip.")
    finally:
        print("Hesablama bitdi.")


# 2) 1-dən 50-yə qədər 11-ə bölünənlər
def bolunenler():
    return [i for i in range(1, 51) if i % 11 == 0]


# 3) Sözlərin ilk hərfləri
def ilk_herfler(siyahi):
    return [soz[0] for soz in siyahi]


# 4) Şəhər və kodları dictionary kimi
def seher_kod_dict(seherler, kodlar):
    return dict(zip(seherler, kodlar))


# 5) Kilometri milə çevirən lambda funksiyası
km_to_mil = lambda km: km * 0.621371
mil_neticeler = list(map(km_to_mil, [1, 5, 10, 15, 20]))


# 6) Qiymətlərə 18% vergi əlavə etmək
qiymetler = [100, 200, 300, 400]
vergi_qiymetler = list(map(lambda x: x * 1.18, qiymetler))


# 7) İki siyahını ikiqat artırıb cəmləmək
list1 = [3, 7, 12]
list2 = [2, 4, 6]
cemlendi = list(map(lambda x, y: x*2 + y*2, list1, list2))


# 8) Reduce ilə minimum dəyəri tapmaq
from functools import reduce
qiymet_siyahisi = [150, 80, 220, 45]
minimum = reduce(lambda x, y: x if x < y else y, qiymet_siyahisi)


print("--- Sprint 4a Nəticələr ---")
hesablama()

print("11-ə bölünənlər:", bolunenler())
print("İlk hərflər:", ilk_herfler(["kitab", "qələm", "defter", "silgi"]))
print("Şəhər kodları:", seher_kod_dict(["Bakı", "Gəncə", "Sumqayıt"], [12, 22, 18]))
print("Mil çevirmə nəticələri:", mil_neticeler)
print("18% vergi ilə qiymətlər:", vergi_qiymetler)
print("İkiqat artırılıb cəmlənmiş:", cemlendi)
print("Ən kiçik qiymət:", minimum)
