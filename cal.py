# cal = Calorie
# kj = Kilojoule
# hp = Horse power


def Cal_To_Kj(Calories):
    return Calories * 4.184

def Kj_To_Cal(Kj):
    return Kj / 4.184

def Cal_To_KWH(Cal):
    kj = Cal_To_Kj(Cal)
    wh = kj / 3.6
    kwh = wh / 1000
    return kwh

def Kj_To_KWH(kj):
    wh = kj / 3.6
    kwh = wh / 1000
    return kwh

def kwh_To_hp(kwh):
    return kwh * 1.341
