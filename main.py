import smtplib
from tkinter import *
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()
email = EmailMessage()


def talk(text): #reads input text
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  #smtpfunct

    server.login('implementationcip@gmail.com', 'Emailbot365')
    email['From'] = 'implementationcip@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email) #smtpfunction


def get_email_info():

    email_list = {
        'black': 'hariharakrishna1@gmail.com',
        'blue': 'aravinthashwa@gmail.com'
    }
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Hey Your email is sent')


if __name__ == "__main__":

    win = Tk()
    lbl1 = Label(win, text='Welcome to the voice controlled email bot', fg='blue', font=('HP Simplified Hans', 20))
    lbl2 = Label(win, text='INSTRUCTIONS', fg='red', font=('HP Simplified Hans', 16))
    lbl3 = Label(win, text='1.Press the button in order to send email', font=('HP Simplified Hans', 12))
    lbl4 = Label(win, text='2.Use microphones, as it is voice controlled', font=('HP Simplified Hans', 12))
    lbl5 = Label(win, text='3.Do not panic if mail not sent', font=('HP Simplified Hans', 12))
    lbl6 = Label(win, text='4.Close and restart if required', font=('HP Simplified Hans', 12))
    lbl7 = Label(win, text='Mail ID options', fg='red', font=('HP Simplified Hans', 16))
    lbl8 = Label(win, text='black = hariharakrishna1@gmail.com', font=('HP Simplified Hans', 12))
    lbl9 = Label(win, text='red = aravinthashwa@gmail.com', fg='red', font=('HP Simplified Hans', 12))
    lbl1.place(x=4,y=0)
    lbl2.place(x=179,y=50)
    lbl3.place(x=109,y=90)
    lbl4.place(x=109, y=110)
    lbl5.place(x=109, y=130)
    lbl6.place(x=109, y=150)
    lbl7.place(x=179, y=180)
    lbl8.place(x=109,y=220)
    lbl9.place(x=109,y=240)
    b1 = Button(win, text="Send email?", command=get_email_info)
    b1.place(x=209, y=280)
    win.title('PYMAILER')
    win.geometry("510x330")

win.mainloop()


