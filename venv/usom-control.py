from tkinter import *
import datetime
def kontrol_et():
    dosya=open("usom.txt","r")
    icerik=dosya.read()
    dosya.close()
    ip=entry1.get()
    bugun=datetime.datetime.now()#Loglamak için
    if str(ip) in icerik:
        dosya=open("log.txt","a")
        yazi=str(ip)+" Zararli!!\nTarih: "+str(bugun)+"\n"
        dosya.write(yazi)
        dosya.close()
        v.set("IP zararlidir")
    else:
        dosya=open("log.txt","a")
        yazi=str(ip)+" Zararli Degil\nTarih: "+str(bugun)+"\n"
        dosya.write(yazi)
        dosya.close()
        v.set("IP zararli Degildir")

top=Tk()#tkinter.Tk” methoduyla bir obje yaratmış olduk aslında.
top.title("USOM IP Kontrol")
B=Button(top,text="Kontrol Et",command=kontrol_et)
B.place(x=50,y=50)
B.pack()#Aktif hale getirir

label1=Label(top,text="Kontrol Edilecek IP adresini giriniz: ")
label1.place(x=50,y=80)
label1.pack()

entry1=Entry(top)#yardımıyla kullanıcının metin girebileceği tek satırlık bir alan oluşturacağız
entry1.place(x=50,y=90)
entry1.pack()

v=StringVar()#String Verisi Depolamaya yarıyor
entry2=Entry(top,textvariable=v)
entry2.place(x=50,y=100)
entry2.pack()
top.mainloop()#Ve kodun sınırsız döngü olarak çalışması için