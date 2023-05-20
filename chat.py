import openai,os,time
from gtts import gTTS
from tkinter import *
import ctypes as ct
from pytube import YouTube
import pyttsx3 as tts

openai.api_key = "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" # Your code api >>> Openai API

# Motyw ciemny
def dark_title_bar(window,you,chat,x,z,c,v):
    window.update()
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    value = 5
    value = ct.c_int(value)
    set_window_attribute(hwnd, 20, ct.byref(value),4)
    window['bg'] = "#3C3C3C"
    chat.configure(bg="#2D2D2D",fg='White')
    you.configure(bg="#1E1E1E",fg='White')
    x.configure(bg="#3C3C3C",fg='White')
    z.configure(bg="#3C3C3C",fg='White')
    c.configure(bg="#3C3C3C",fg='White')
    v.configure(bg="#3C3C3C",fg='White')

# Motyw jasny
def Light_title_bar(window,you,chat,x,z,c,v):
    window.update()
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    value = 0
    value = ct.c_int(value)
    set_window_attribute(hwnd, 20, ct.byref(value),4)
    window.configure(bg = "#F0F0F0")
    chat.configure(bg="#FF3927",fg='Black')
    you.configure(bg="#E4F6D4",fg='Black')
    x.configure(bg="#F0F0F0",fg='Black')
    z.configure(bg="#F0F0F0",fg='Black')
    c.configure(bg="#F0F0F0",fg='Black')
    v.configure(bg="#F0F0F0",fg='Black')

#tworzenie okna configuracji mods
def new_window(root,you,chatbot,odpowiedz,save,audio,option):
    dialog = Toplevel(root)
    bialy = Button(dialog,text="White",command=lambda:Light_title_bar(root,you,chatbot,odpowiedz,save,audio,option))
    czarny = Button(dialog,text="Black",command=lambda:dark_title_bar(root,you,chatbot,odpowiedz,save,audio,option))
    bialy.pack(side=LEFT)
    czarny.pack(side=LEFT)
    dialog.grab_set()

# funkcja youtube
def youtoube(root):
    def play(odbierz):
       yt = YouTube(str(odbierz))
       video = yt.streams.first()
       lokalizacja = '.'
       pobierz = video.download(output_path=lokalizacja)
       base,ext = os.path.splitext(pobierz)
       new_file = base + '.mp4'
       os.rename(pobierz,new_file)

    okno = Toplevel(root)
    start = Label(okno,text="Youtube downloader",bg="red",fg="White")
    start.pack()
    link = Entry(okno,width=100)
    link.pack()
    odbierz = Button(okno,text="Pobierz",command=lambda:play(link.get()))
    odbierz.pack()
   
    okno.grab_set()

#Funkcja która zpisuje i odtwarza dziwięk v1

def mp3(plikaudio):
    tts = gTTS(text=plikaudio,lang='pl')
    tts.save('plik.mp3')
    time.sleep(2) # odczekanie na utworzenie sie pliku
def sluch():
    os.system("start plik.mp3") # Funkcja odtwarzająca plik

# Funkcja odtwarza dziwięk v2
def audio(plikaudio):
    engine= tts.init()
    engine.setProperty('rate',150)
    engine.say(plikaudio)
    engine.runAndWait()

# Tworzenie linku do wygeneroania obrazu
def OBRAZ(odpowidz):
    response = openai.Image.create(prompt=odpowidz,
                                   n=1,
                                   size= "1024x1024")
    image_url = response['data'][0]['url']
    print(image_url)

# Zapis do pliku 
def save(x):
        filepath = "dane.txt"
        f = open(filepath,"w", encoding="UTF-8")
        time.sleep(2)
        f.write(x)

# funkcja chatbota
def chatbot(wiadomosc):       
    
    comp = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                        messages=[{"role":"user","content":wiadomosc},
                                                  {"role":"assistant","content":wiadomosc},
                                                  {"role":"system","content":wiadomosc}],
                                                  temperature=0.2)
    odpowiedz = comp.choices[0].message.content
    #kontrole wyprintowanie
    print (odpowiedz + "\n")
    return odpowiedz + "\n"  

def qr(root):
    import qrcode
    
    okno = Toplevel(root)
    start = Label(okno,text="QR CODE",bg="Black",fg="White")
    start.pack()
    link = Entry(okno,width=100)
    link.pack()
    odbierz = Button(okno,text="Pobierz",command=lambda:qr())
    odbierz.pack()
    def qr():
        qr = link.get()
        img = qrcode.make(qr)
        img.save("qr.png")
    okno.grab_set()