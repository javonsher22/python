'''
if elif else
'''
# yosh = int(input('Yoshingiz nechida? '))
# if yosh <= 4:
#     print('Sizga kirish bepul.')
# elif yosh <= 12:
#     print('Sizga kirish 5000 so\'m')
# else:
#     print('Sizga kirish 10000 so\'m')

# yosh = int(input('Yoshingiz nechida? '))
# if yosh <= 4:
#     price = 0
# elif yosh <= 12:
#     price = 5000
# else:
#     price = 10000
# print(f"Sizga kirish {price} so'm")

# kun = input("Bugun nima kun?>>>")
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print('Bugun dam olish kuni.')
# else:
#     print('Bugun ish kuni.')

# kun = input("Bugun nima kun? ")
# harorat = float(input("Havo harorati qanday? "))
# if kun.lower()=='yakshanba' and harorat >= 30:
#     print("Cho'milgani ketdik!")
# elif kun.lower() == 'yakshanba' and harorat < 30:
#     print("Uyda dam olamiz!")

# from random import randint
# a = randint(1, 500)
# b = randint(1, 500)
# c = int(input('{} + {} '.format(a, b)))
# if c == (a + b):
#     print("tugri")
# else:
#     print("xato!")

# karra = 9
# for son in range(1, 11):
#     natija = karra * son
#     print("{} * {} = {}".format(karra, son, natija))

# car = {'marka': 'ferrari', 'rangi': 'qizil'}
# print(car['marka'])

# talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
# print(f"{talaba_0['ism'].title()},\
#  {talaba_0['t_yil']}-yilda tu'gilgan,\
#  {talaba_0['yosh']} yoshda")

# talaba_0 = {'ism': 'Javoxirov Javonsher','yosh': 17, 't_yil': 2005}
# print(f"{talaba_0['ism'].title()}\
# ,{talaba_0['t_yil']}-yilda tugilgan,\
# {talaba_0['yosh']} yoshda")

# talaba_1['ism'] = 'qobil rasulov'
# talaba_1['kurs'] = 3
# talaba_1['yosh'] = 20
# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")\

            # yoshni hisoblovchi funksiya

# from datetime import datetime
# from tkinter import *
# oyna = Tk()
# oyna.title('Dasturcha :)')
# oyna.geometry('300x300')
# natija = Label(text='Natija', bg='white')
# natija.place(x=90, y=135, width=120, height=40)
# yil = Entry()
# yil.place(x=75, y=50, width=150, height=30)
# def farq():
#     bugun = datetime.today()
#     natija.config(text=bugun.year - int(yil.get()))
# tugma = Button(text='Hisoblash', command=farq)
# tugma.place(x=90, y=90, width=120, height=40)
# oyna.mainloop()

# funksiyalar

# def salom_ber(ism):
#     print(f"Assalomu aleykum, hurmatli {ism.title()}!")
# salom_ber('Hasan')
# salom_ber('Olim')

# def toliq_ism(ism, familiya):
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
# toliq_ism('Javonsher', 'Javokhirov')

# def yosh_hisobla(ism, tugilgan_yil):
#     print(f"{ism.title()} {2023-tugilgan_yil} yoshda")
# yosh_hisobla('Javonsher', 2005)

# def yosh_hisobla(tugilgan_yil, joriy_yil=2023):
#     print(f"Siz {joriy_yil - tugilgan_yil} yoshdasiz")
# yosh_hisobla(2005)
