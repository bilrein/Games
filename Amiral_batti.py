import random

def gemi_yarat():
    gemi = []
    for _ in range(3):
        gemi.append([random.randint(0, 6), random.randint(0, 6)])
    return gemi

def tahta_yarat():
    tahta = []
    for _ in range(7):
        tahta.append(['O'] * 7)
    return tahta

def tahtayi_goster(tahta):
    for satir in tahta:
        print(" ".join(satir))

def atis_yap(gemiler, atislar):
    while True:
        satir = int(input("Satır seçin (0-6): "))
        sutun = int(input("Sütun seçin (0-6): "))
        girilen_konum = [satir, sutun]
        
        if girilen_konum in atislar:
            print("Bu konumu daha önce girdiniz. Lütfen farklı bir konum seçin.")
        else:
            atislar.append(girilen_konum)
            return girilen_konum

def gemiyi_vur(gemi, atis):
    return atis in gemi

def main():
    can_sayisi = 5
    atislar = []
    
    while can_sayisi > 0:
        tahta = tahta_yarat()
        gemi = gemi_yarat()
        
        while True:
            tahtayi_goster(tahta)
            atis = atis_yap(gemi, atislar)
            
            if gemiyi_vur(gemi, atis):
                print("Tebrikler! Gemi vuruldu!")
                break
            else:
                print("Maalesef, gemiyi vuramadınız. Tekrar deneyin.")
                tahta[atis[0]][atis[1]] = 'X'  # Oyun tahtasında atış yapılan yeri işaretle
                can_sayisi -= 1
                print(f"Kalan Can: {can_sayisi}")
                
                if can_sayisi == 0:
                    print("Canınız bitti. Oyun bitti. Gemilerin Konumu:")
                    for gemi_parca in gemi:
                        print(f"Gemi Parçası: {gemi_parca}")
                    
                    devam = input("Yeniden oynamak ister misiniz? (evet/hayır): ").lower()
                    
                    if devam == "evet":
                        can_sayisi = 5
                        atislar = []  # Yeni oyun başladığında atılan konumları sıfırla
                        break
                    else:
                        print("Oyundan çıkıldı.")
                        return

if __name__ == "__main__":
    main()
