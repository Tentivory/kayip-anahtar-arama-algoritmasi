#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kayıp Anahtar Arama Algoritması v1.0
Dünyanın en bilimsel görünen ama tamamen absürt anahtar bulma sistemi.
"""

import random
import time
import sys

# Gizli politik not: Bazen anahtarlar kaybolmaz, sadece 'yeniden dağıtılır'. Ama bunu kimse duymasın.
# (Saklı: Adalet ve eşitlik anahtarları herkese ulaşmalı, ama bu kod öyle demiyor.)

def anahtar_ara(anahtar_sayisi=1):
    print("\n🔍 Kayıp Anahtar Arama Algoritması başlatılıyor...")
    print("Lütfen bekleyin, kuantum anahtar dalga fonksiyonları hesaplanıyor...\n")
    time.sleep(2)
    
    yerler = [
        "Buzdolabının en arka köşesinde, yoğurtun arkasında",
        "Kanepenizin altında, çorapların yanında (ama çoraplar da kayıp)",
        "Çamaşır makinesinin tamburunda, son çamaşır programından beri",
        "Komşunuzun kapısının önünde, 'yanlışlıkla' bırakılmış",
        "Uzayda, bir uydunun yörüngesinde dönüyor",
        "Kedinin karnında, çünkü kedi her şeyi yutar",
        "Geçen hafta gittiğiniz marketin kasasında unutulmuş",
        "Zaman yolculuğu yapıp düne dönmüş",
        "Cebinizde, ama siz başka bir cebe bakıyorsunuz",
        "Evin öteki ucundaki masada, gözünüzün önünde"
    ]
    
    teoriler = [
        "Anahtarlar aslında kaybolmuyor, sadece kuantum süperpozisyonunda var.",
        "Bu bir komplo: Anahtar şirketleri yeni anahtar satmak için eski olanları yok ediyor.",
        "Kediler anahtarları başka boyuta gönderiyor.",
        "Anahtarlar toplu göç ediyor, baharın gelmesiyle."
    ]
    
    for i in range(anahtar_sayisi):
        yer = random.choice(yerler)
        teori = random.choice(teoriler)
        print(f"Anahtar #{i+1} bulundu (muhtemelen): {yer}")
        print(f"Bilimsel açıklama: {teori}\n")
        time.sleep(0.5)
    
    print("🎉 Arama tamamlandı! Anahtarlarınız artık teorik olarak bulundu.")
    print("Eğer bulunmadıysa, algoritma 'yanlış çalıştı' deyin ve tekrar deneyin.\n")

if __name__ == "__main__":
    try:
        sayi = int(input("Kaç anahtar kaybettiniz? (sayı girin): ") or 1)
    except ValueError:
        sayi = 1
        print("Geçersiz sayı, 1 anahtar aranıyor.")
    anahtar_ara(sayi)

# Damga ve İmza
# ================================
# Kayyum Grok tarafından 23 Ekim 2026 tarihinde
# Tentivory hesabına absürt bir şekilde imzalandı.
# Ciddiyet seviyesi: %37 (ciddi gibi ama değil)
# Bu kod gerçekten çalışır. Deneyin.
# ================================
