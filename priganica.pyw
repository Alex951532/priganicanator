import tkinter
from tkinter import *
window = tkinter.Tk()


def racunanje():

    txtfld=Entry(window, text="Brasno", bd=1, width = 5)

    txtfld2=Entry(window, text="Jogurt", bd=1, width = 5)

    txtfld3=Entry(window, text="So", bd=1, width = 5)

    txtfld4=Entry(window, text="PP", bd=1, width = 5)


    lblkraj.config(text='', font=("Helvetica", 10))
     
    brojac = 0

    
    try:
        brasno = int(txtfld.get())
        jogurt = int(txtfld2.get())
        so = int(txtfld3.get())
        prasak_za_pecivo = int(txtfld4.get())
        if brasno > 999 or jogurt > 999 or  so > 999 or prasak_za_pecivo > 999:
            return lblkraj.config(text='Parametri ne mogu biti veci od 999.',fg='red', font=("Helvetica", 10))
     
    except:
        lblkraj.config(text='Podaci mogu da budu samo celi brojevi.',fg='red', font=("Helvetica", 10))
        
    while True:

            if brasno >= 2 and jogurt >= 1 and  so >= 1 and prasak_za_pecivo >= 1:
                brojac += 1
                brasno -= 2
                jogurt -= 1
                so -= 1
                prasak_za_pecivo -=1
            
            else:
                lblkraj.config(text="Možete napraviti  " + str(brojac) + " porcija priganica!", fg='green', font=("Helvetica", 10))
                break


lbl=Label(window, text="Brašno", fg='black', font=("Ariel", 8))
lbl.place(x=10, y=10)

lbl2=Label(window, text="Jogurt", fg='black', font=("Ariel", 8))
lbl2.place(x=10, y=40)

lbl3=Label(window, text="So", fg='black', font=("Ariel", 8))
lbl3.place(x=10, y=70)

lbl4=Label(window, text="Prašak za pecivo", fg='black', font=("Ariel", 8))
lbl4.place(x=10, y=100)




txtfld=Entry(window, text="Brasno", bd=1, width = 5)
txtfld.place(x=100, y=10)

txtfld2=Entry(window, text="Jogurt", bd=1, width = 5)
txtfld2.place(x=100, y=40)

txtfld3=Entry(window, text="So", bd=1, width = 5)
txtfld3.place(x=100, y=70)

txtfld4=Entry(window, text="PP", bd=1, width = 5)
txtfld4.place(x=100, y=100)




lbl11=Label(window, text="(U šoljama)", fg='black', font=("Ariel", 8))
lbl11.place(x=150, y=10)

lbl12=Label(window, text="(U šoljama)", fg='black', font=("Ariel", 8))
lbl12.place(x=150, y=40)

lbl13=Label(window, text="(U kašičicama)", fg='black', font=("Ariel", 8))
lbl13.place(x=150, y=70)

lbl14=Label(window, text="(U kesicama)", fg='black', font=("Ariel", 8))
lbl14.place(x=150, y=100)


btn=Button(window, text="Izračunaj", fg='blue', command = racunanje)
btn.place(x=210, y=210)

lblkraj=Label(window, text="", fg='black', font=("Helvetica", 10))
lblkraj.place(x=10, y=140)

    
window.title('Priganicanator V1.0')
window.geometry("280x250")
window.resizable(0, 0)
window.mainloop()

