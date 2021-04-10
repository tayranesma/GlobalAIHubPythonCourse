# -*- coding: utf-8 -*-

"""
Knowledge competition
* Write a knowledge competition program
* It should consist of 10 questions in total
* Each question will have only one answer
* Adjust the answers of the questions according to case sensitivity
* Each question shoul be worth 10 points
* If user answers 5 or fewer questions, it will be considered unsuccessful
* If the user answers more than 5 questions correctly, it will be considered successful
"""

count = 0
questions = {"Moğol İmparatorluğu'nun kurucusu kimdir": "Cengizhan", 
             "Bir zarın kaç köşesi vardır?":"8", 
             "Olimpiyat bayrağı üzerinde bulunan iç içe geçmiş 5 renkli halka neyi temsil eder?": "Kıtaları", 
             "Tarihçilerin Kutbu olarak bilinen dünyaca ünlü tarihçimiz kimdir?": "Halil İnalcık", 
             "Kuyucaklı Yusuf adlı eser kime aittir?":"Sabahattin Ali",
             "Bir elektrik devresinde direnç hangi harfle gösterilir?":"R", 
             "Fas'ın başkenti hangi şehirdir?":"Kazablanka", 
             "İçine para atarak birikim yapılan kutunun adı nedir?":"Kumbara", 
             "Yirmi kişinin katıldığı bir yarışmada altıncı kişiyi geçen kişi kaçıncı oluştur?":"Altıncı", 
             "Türkiye'nin en yüksek dağı nedir?":"Ağrı Dağı"}

for key, value in questions.items():
    print(key)
    cevap = input("yanıtınız: ")
    if cevap == value:
        count += 1
        print("doğru cevap\n")
    else:
        print("yanlış cevap\n")

if count > 5:
    print("Tebrikler, %d soruya doğru cevap verdiniz, kazandınız!" % count)
else:
    print("Üzgünüz kazanamadınız :( tekrar deneyin.")
