import chat as ai
from tkinter import *
from tkinter import messagebox as msb
#stworzenie okna
root = Tk()
# Funkcja for
# Meniu
def meniu(event):
    meniu = Menu(root)

    filemeniu = Menu(meniu)
    meniu.add_cascade(label = 'Aplikacje',menu=filemeniu)

    option = Menu(meniu, tearoff = 0)
    filemeniu.add_command(label='Youtube',command=lambda:ai.youtoube(root))
    filemeniu.add_cascade(label="Pobierz MP3 z tekstu", menu=option)
    filemeniu.add_command(label="QR Code",command=lambda:ai.qr(root,))
    option.add_radiobutton(label="Odtwórz",command=lambda:ai.sluch())
    option.add_radiobutton(label="Pobierz MP3 z tekstu",command=lambda:ai.mp3(chatbot.get("1.0", "end-1c")))
    
    root.config(menu=meniu)
    
root.title("Twój chat bot")
foto = PhotoImage(file = 'robot.png')
optionpng = PhotoImage(file= 'option.png')
root.iconphoto(False,foto)

#rozmiar okna
root.geometry("1000x500")

def input():
    INPUT1 = you.get("1.0", "end-1c")
    chatbot.insert(END,ai.chatbot(INPUT1))

you = Text(root, height=10,width=500,bg="#E4F6D4",fg='Black')

frameyou = Label(root,height=1,bg="green",width=10000000,text="Napisz co chcesz wiedzieć",justify='center')
framechat = Label(root,height=1,bg="red",width=10000000,text="Odpowiadam",justify='center')
root.configure(bg="#ECECEC")
ramka= Frame(root,height=2,width=500)
ramkaoption= Frame(root,height=2,width=5000)
option = Button(ramka, height = 35,
                 width = 40,
                 text ="O",
                 image=optionpng,
                 command = lambda:ai.new_window(root,you,chatbot,odpowiedz,save,audio,option)
                )
#przycik obsugujący Odpowiedzi 
odpowiedz = Button(ramka, height = 2,
                 width = 20,
                 text ="Odpowiedz",
                 command = lambda:input())
#pole tekstowe odpowiedzi bota
chatbot = Text(root, height = 10,
              width = 500,
              bg="#FF3927",
              fg='Black')

#przycik obsugujący zapis do pliku dane.txt
save = Button(ramka, height = 2,
                 width = 20,
                 text ="Zapisz",
                 command = lambda:ai.save(chatbot.get("1.0", "end-1c"))
                 )

#przycik obsugujący audio
audio = Button(ramka, height = 2,
                 width = 20,
                 text= "Mów mi",
                 command = lambda:ai.audio(chatbot.get("1.0", "end-1c"))
                 )

#wczatanie zasobów
ramkaoption.pack()
frameyou.pack()
you.pack()
ramka.pack()
framechat.pack()
chatbot.pack()
option.pack(side=RIGHT)
odpowiedz.pack(side=LEFT)
save.pack(side=LEFT)
audio.pack(side=LEFT)

root.bind('<Control-Button-1>', meniu)

mainloop()
