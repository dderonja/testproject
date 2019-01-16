from tkinter import *
from classes.text_blob_de import TextBlobClass
from classes.checkForAds import AdCheck


def callback():
    entered_text = textentry.get("1.0", 'end-1c')
    a = AdCheck
    if a.check_for_ad(entered_text) != 'Valide':
        textDisplay['text'] = a.check_for_ad(entered_text)
    else:
        d = TextBlobClass
        textDisplay['text'] = d.get_sentiment(entered_text)


window = Tk()
window.title("Facebook Comment Sentiment Analysis")

toolbar = PhotoImage(file="img/toolbar.gif")
Label(window, image=toolbar).pack(anchor='center')

logo = PhotoImage(file="img/logo-rewe.gif")
Label(window, image=logo).pack(anchor='center')
headline = Label(window, text="Sag uns Deine Meinung!", font=("Neue Helvetica", 24))
headline.pack(anchor='center')
textentry = Text(window, width=40, height=10, font=("Neue Helvetica", 16), wrap=WORD, pady=10)
textentry.pack(anchor='center')

Label(window, text=" ").pack()
postButton = Button(window, text="Posten", command=callback, background='#4167B2', foreground='white', font=("Neue Helvetica", 16), cursor='hand2')
postButton.pack(anchor='center')
textDisplay = Label(window, width=40, height=10, font=("Neue Helvetica", 16), pady=10)
textDisplay.pack(anchor='center')

window.mainloop()
