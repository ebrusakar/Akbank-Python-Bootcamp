import tkinter as tk

form = tk.Tk()
form.geometry('800x500+400+100')
form.title('Pizza Sipariş Programı')

###################### Label  ########################
baslik = tk.Label(form, text='Pizza Sipariş Programına Hoşgeldin', fg='black', bg='pink', font='Times 15 bold')
baslik.pack()

menu_label = tk.Label(form, text='Menu', fg='black', bg='pink', font='Times 15 bold underline')
menu_label.place(x=10, y=30)
pizza_label = tk.Label(form, text='Pizzalar:', fg='black', bg='pink', font='Times 15 bold')
pizza_label.place(x=10, y=60)
margarita_label = tk.Label(form, text='- Margarita: 25TL', fg='black', bg='pink', font='Times 15 bold')
margarita_label.place(x=10, y=90)
klasik_pizza_label = tk.Label(form, text='- Klasik Pizza: 20TL', fg='black', bg='pink', font='Times 15 bold')
klasik_pizza_label.place(x=10, y=120)
sade_pizza_label = tk.Label(form, text='- Sade Pizza: 15TL', fg='black', bg='pink', font='Times 15 bold')
sade_pizza_label.place(x=10, y=150)
icindekiler1_label = tk.Label(form, text='Soslar:', fg='black', bg='pink', font='Times 15 bold')
icindekiler1_label.place(x=10, y=180)
sucuk_label = tk.Label(form, text='- Sucuk: 5TL', fg='black', bg='pink', font='Times 15 bold')
sucuk_label.place(x=10, y=210)
mantar_label = tk.Label(form, text='- Mantar: 7TL', fg='black', bg='pink', font='Times 15 bold')
mantar_label.place(x=10, y=240)
keci_peyniri_label = tk.Label(form, text='- Keçi Peyniri: 10TL', fg='black', bg='pink', font='Times 15 bold')
keci_peyniri_label.place(x=10, y=270)


llb_ad = tk.Label(text='Ad-Soyad:', bg='pink', font='times 15 bold')
llb_ad.place(x=200, y=40)
llb_boyut = tk.Label(text='Pizza Boyutu:', bg='pink', font='times 15 bold')
llb_boyut.place(x=200, y=80)
llb_pizza = tk.Label(text='Pizza Seçiniz:', bg='pink', font='times 15 bold')
llb_pizza.place(x=200, y=125)
llb_icindekiler = tk.Label(text='Sos Seçiniz:', bg='pink', font='times 15 bold')
llb_icindekiler.place(x=200, y=220)
llb_adres = tk.Label(text='Adres:', bg='pink', font='times 15 bold')
llb_adres.place(x=200, y=320)

###################### Radiobutton  #########################
boyut = tk.StringVar()
boyut.set('Küçük')

rb_buyuk = tk.Radiobutton(form, text='Büyük', value='Büyük', variable=boyut, font='Times 12 bold', bg='pink')
rb_buyuk.place(x=350, y=80)
rb_orta = tk.Radiobutton(form, text='Orta', value='Orta', variable=boyut, font='Times 12 bold', bg='pink')
rb_orta.place(x=450, y=80)
rb_kucuk = tk.Radiobutton(form, text='Küçük', value='Küçük', variable=boyut, font='Times 12 bold', bg='pink')
rb_kucuk.place(x=550, y=80)

###################### Checkbutton - Pizza #########################
pizza = tk.StringVar()
pizza.set('')

cb_margarita = tk.Checkbutton(form, text='Margarita', variable=pizza, onvalue='Margarita 25 TL', offvalue='', font='Times 12 bold', bg='pink')
cb_margarita.place(x=350, y=125)
cb_klasik_pizza = tk.Checkbutton(form, text='Klasik Pizza', variable=pizza, onvalue='Klasik Pizza 20 TL', offvalue='', font='Times 12 bold', bg='pink')
cb_klasik_pizza.place(x=350, y=150)
cb_sade_pizza = tk.Checkbutton(form, text='Sade Pizza', variable=pizza, onvalue='Sade Pizza 15 TL', offvalue='', font='Times 12 bold', bg='pink')
cb_sade_pizza.place(x=350, y=175)

###################### Checkbutton - icindekiler #########################
icindekiler = tk.StringVar()
icindekiler.set('')

cb_sucuk = tk.Checkbutton(form, text='Sucuk', variable=icindekiler, onvalue='Sucuk 5 TL', offvalue='', font='Times 12 bold', bg='pink')
cb_sucuk.place(x=350, y=220)
cb_mantar = tk.Checkbutton(form, text='Mantar', variable=icindekiler, onvalue='Mantar 7 TL', offvalue='', font='Times 12 bold', bg='pink')
cb_mantar.place(x=350, y=245)
cb_keci_peyniri = tk.Checkbutton(form, text='Keçi Peyniri', variable=icindekiler, onvalue='Keçi Peyniri 10 TL', offvalue='', font='Times 12 bold', bg='pink')
cb_keci_peyniri.place(x=350, y=270)

###################### Entry ########################

entry_ad = tk.Entry(form)
entry_ad.place(x=350, y=45)

entry_adres = tk.Entry(form)
entry_adres.place(x=350, y=320)

######################  Function ####################
def hesapla():
    pizza_fiyat = 0
    icindekiler_fiyat = 0
    boyut_fiyat = 0

    # Calculate pizza price
    if pizza.get() == "Margarita 25 TL":
        pizza_fiyat += 25
    elif pizza.get() == "Klasik Pizza 20 TL":
        pizza_fiyat += 20
    elif pizza.get() == "Sade Pizza 15 TL":
        pizza_fiyat += 15

    # Calculate sauce price
    if icindekiler.get() == "Sucuk 5 TL":
        icindekiler_fiyat += 5
    elif icindekiler.get() == "Mantar 7 TL":
        icindekiler_fiyat += 7
    elif icindekiler.get() == "Keçi Peyniri 10 TL":
        icindekiler_fiyat += 10

    # Calculate size price
    if boyut.get() == "Büyük":
        boyut_fiyat += 10
    elif boyut.get() == "Orta":
        boyut_fiyat += 5
    elif boyut.get() == "Küçük":
        boyut_fiyat += 0

    toplam_fiyat = pizza_fiyat + icindekiler_fiyat + boyut_fiyat

    ##### sipariş bilgi  ######
    label_bilgi = tk.Label(form, text='Sipariş Bilgileri', bg='pink', font='times 15 bold').place(x=200, y=450)
    llb_ad = tk.Label(text='Ad-Soyad', bg='pink', font='times 15 bold').place(x=200, y=500)
    llb_adres = tk.Label(text='Adres', bg='pink', font='times 15 bold').place(x=200, y=550)
    llb_fiyat = tk.Label(text='Toplam Fiyat', bg='pink', font='Times 15 bold').place(x=200, y=600)
    llb_ad1 = tk.Label(text=entry_ad.get(), bg='pink', font='times 15 italic').place(x=350, y=500)
    llb_adres1 = tk.Label(text=entry_adres.get(), bg='pink', font='times 15 italic').place(x=350, y=550)
    llb_fiyat1 = tk.Label(text=str(toplam_fiyat) + " TL", bg='pink', font='times 15 italic').place(x=350, y=600)

def iptalet():
    form.quit()


btn_hesapla = tk.Button(form, text='Sipariş Ver', font='Times 12 bold', bg='green', command=hesapla).place(x=420,y=370)
iptal=tk.Button(form,text='İptal Et', font='Times 12 bold', bg='red',command=iptalet).place(x=550,y=370)


form.mainloop()