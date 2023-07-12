import speech_recognition as sr
import pyttsx3
import smtplib
from email.message import EmailMessage


listener = sr.Recognizer
engine = pyttsx3.init()
def get_info():
    try:
        with sr.Microphone() as source:
            print("listening.....")
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def send_mail(receiver,subject,message):
    server = smtplib.SMTP('sender mail@gmail.com',587)
    server.starttls()
    server.login('sender mail.com','Password')
    email = EmailMessage()
    email['from'] ="sender mail@gmail.com"
    email['to'] = receiver
    email['subject'] = subject
    email.set_content(message)
email_list = {
     'asmanjas':  xyz@gmail.com'

    }
def get_email_info():
    speak('to whom you want to send email ...')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    speak('what is the subject of your email ')
    subject = get_info()
    speak('tell me the text of your email')
    message = get_info()
    send_mail(receiver,subject,message)
    speak('your email has been seended !')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()
    get_email_info()