import tkinter

def plakasorgu():
    plaka = entry.get()
    labelplaka["text"] = plaka
window = tkinter.Tk()
window.title("plaka sorgu")
window.geometry("400x200")
window.wm_iconbitmap("C:\\Users\\oğuz\\Downloads\\favicon.ico")
window.configure(background = "gold")
#-----------------------------------------------------------------------------------------------------------
label = tkinter.Label(window,text = "Lütfen plakanızı yazın",bg = "gold")
label.pack()
#-----------------------------------------------------------------------------------------------------------
entry = tkinter.Entry(window,bg = "gainsboro")
entry.pack()
#-----------------------------------------------------------------------------------------------------------
tus = tkinter.Button(window,text = "Sorgula",bg = "dark slate grey",fg = "turquoise",command = plakasorgu)
tus.pack()
#-----------------------------------------------------------------------------------------------------------
labelplaka = tkinter.Label(window,text = "",bg = ("gold"))
labelplaka.pack()

window.mainloop()
print(plaka)



