import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import webbrowser
import smtplib
from email.message import EmailMessage
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from tkinter import messagebox

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


class login:
    def __init__(self, root):
        self.root = root
        self.root.title("Embot")
        self.root.geometry("1080x615+100+50")
        self.root.resizable(False, False)

        # background image.
        self.bg = ImageTk.PhotoImage(
            file="C:\\Users\HP\\OneDrive\\Desktop\\Email-bot\\login.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(
            x=0, y=0, relwidth=1, relheight=1)

        # login frame
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=50, y=120, width=500, height=400)

        #title and subtitle

        title = Label(Frame_login, text="Email - Bot", font=(
            "Century", 35, "bold"), fg="coral", bg="ghost white").place(x=110, y=40)
        subtitle = Label(Frame_login, text="Login With G-mail Account", font=(
            "Goudy old style", 13), fg="black", bg="ghost white").place(x=140, y=115)

        # Username
        lbl_user = Label(Frame_login, text="Username", font=(
            "Century", 13), fg="black", bg="ghost white").place(x=50, y=170)
        self.username = Entry(Frame_login, font=(
            "Century", 13), bg="#E7E6E6")
        self.username.place(x=50, y=200, width=320, height=35)

        # Password
        lbl_password = Label(Frame_login, text="Password", font=(
            "Century", 13), fg="black", bg="ghost white").place(x=50, y=250)
        self.password = Entry(Frame_login, font=(
            "Century", 13), bg="#E7E6E6", show="*")
        self.password.place(x=50, y=280, width=320, height=35)

        Submit = Button(Frame_login, command=self.check_func, cursor="hand2", text="Login?", bd=0.5, font=(
            "Century", 13), fg="black", bg="white smoke").place(x=160, y=340, width=150, height=35)

    def check_func(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "Please Enter Username & Password", parent=self.root)
        elif self.username.get() or self.password.get():
            messagebox.showinfo("Welcome", f"Welcome - {self.username.get()}")

        def home(self):
            self.root = root
            self.root.title("Embot-Home")
            self.root.geometry("1080x615+100+50")
            self.root.resizable(False, False)
            self.bg = ImageTk.PhotoImage(
                file=r"C:\Users\HP\OneDrive\Desktop\Email-bot\talk_embot.gif")
            self.bg_image = Label(self.root, image=self.bg).place(
                x=0, y=0, relwidth=1, relheight=1)
            Button(cursor="hand2", text="Start", bd=0.5, font=(
                "Century", 13,), fg="black", bg="white smoke", command=self.run).place(x=460, y=520, width=150, height=35)
        home(self)


    def run(self):

        def speak(audio):
            engine.say(audio)
            engine.runAndWait()

        def wishMe():
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                speak("Good Morning!")

            elif hour >= 12 and hour < 18:
                speak("Good Afternoon!")

            else:
                speak("Good Evening!")

            speak("I am Email Bot's Sir. Please tell me how may I help you")

        def takeCommand():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 1
                r.energy_threshold = 200
                audio = r.listen(source)

            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language='en-in')
                # print(f"User said: {query}\n")
                print(query)

            except Exception as e:
             # print(e)
                print("Say that again please...")
                return "None"
            return query.lower()

        def send_email(receiver, subject, message):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            # Make sure to give app access in your Google account
            # server.login('yashvasundhariya.1@gmail.com', '2000June17@yash')
            server.login(self.username.get(), self.password.get())
            email = EmailMessage()
            email['From'] = 'Sender_Email'
            email['To'] = receiver
            email['Subject'] = subject
            email.set_content(message)
            server.send_message(email)

        email_list = {
            'yash': 'yashvasundhariya.1@gmail.com',
            'sahil': 'sahilshaikh3010@gmail.com',
            'harshita': 'harshita123ugde@gmail.com',
            'harsh': 'ugdeharshita@gmail.com'
        }

        def get_email_info():
            speak('To Whom you want to send email')
            name = takeCommand()
            receiver = email_list[name]
            print(receiver)
            speak('What is the subject of your email?')
            subject = takeCommand()
            speak('Tell me the text in your email')
            message = takeCommand()
            send_email(receiver, subject, message)
            speak('Hey lazy . Your email is sent')
            messagebox.showinfo("Successfully", f"Mail Sent Successfully..!")


        wishMe()
        while(True):
            query = takeCommand().lower()
            # Logic for executing tasks based on query
            if 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'send mail' in query:
                get_email_info()

            elif 'exit' in query:
                exit()


root = Tk()
obj = login(root)
root.mainloop()
