import speech_recognition as sr

import webbrowser 

import os

import pyttsx3

from tkinter import *

from time import *

from tkinter import messagebox

from datetime import datetime

from threading import Timer

from plyer import notification

from PIL import Image,ImageTk

import requests

import subprocess

import pyautogui

import screen_brightness_control as sbc



engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def speakout(audio):
    engine.say(audio)
    engine.runAndWait()


def open_notepad():
    subprocess.Popen(['notepad.exe'])

r = sr.Recognizer()
def takeCommand():
    with sr.Microphone() as source:
        print("Say something in English only")
        r.pause_threshold = 0.5
        audio = r.listen(source)


    try:
        query = r.recognize_google(audio, language="en-in")
        return query.lower()
    
    except: 
        print("Translation failed")



if __name__ == '__main__':
    speakout("Hello I am Friday A.I")
    query = "hello"
    while(query!="over") :
        query = takeCommand()
        print(query)
        if "over" in query:
            break

        elif "friday open google" in query:
            webbrowser.open("https://www.google.com")
            speakout("opening google")


        elif "friday how are you" in query:
            print("I am fine! Thank you for asking; please tell me how can I assist you...")
            speakout("I am fine thankyou for asking; please tell how can I assist you")


        elif "friday open youtube" in query:
            webbrowser.open("https://www.youtube.com")
            speakout("opening youtube")


        elif "friday open wikipedia" in query:
            webbrowser.open("https://www.wikipedia.com")
            speakout("opening wikipedia")


        elif "friday play any song" in query:
            speakout("enjoy music")
            MusicPath = r"C:/Users/chhay/Downloads/theme-timeless-vlog-no-copyright-music-195165.mp3"
            os.system(f"start {MusicPath}")



        elif "friday play any english song" in query:
            speakout("playing music for you")
            MusicPath1 = r"C:\Users\chhay\Downloads\Ride_It_5.mp3"
            os.system(f"start {MusicPath1}") 


        elif "friday play any hindi song" in query:
            speakout("playing music for you")
            MusicPath2 = r"C:/Users/chhay/Downloads/hindiSong_Kuch_dino_se.mp3"
            os.system(f"start {MusicPath2}")


        elif "friday play any punjabi song" in query:
            speakout("playing music for you")
            MusicPath3 = r"C:/Users/chhay/Downloads/Hass_Hass_Diljit_Dosanjh_Sia.mp3"
            os.system(f"start {MusicPath3}")


        elif "friday open chat gpt" in query:
            url = "https://chat.openai.com/"
            webbrowser.open_new_tab(url)
            speakout("opening chatgpt")


        elif "friday tell me today's headlines" in query:
            url = "https://www.hindustantimes.com/"
            webbrowser.open_new_tab(url)
            speakout("here's the today's news headlines")


        elif "friday open notepad" in query:
            open_notepad()
            speakout("opening notepad")


        elif "friday close notepad" in query:
            os.system("taskkill /f /im  notepad.exe")
            speakout("notepad has been closed")


        elif "friday close google chrome" in query:
            os.system("taskkill /f /im  chrome.exe")
            speakout("chrome has been closed")

        elif "friday open camera" in query:
            os.system("start microsoft.windows.camera:")
            speakout("opening camera")


        elif "friday take a screenshot" in query:
            print("Taking screenshot... and saving it on desktop..\n")
            i=1
            speakout("taking screenshot")
            image = pyautogui.screenshot()
            image.save("C:/Users/chhay/Desktop/my_screenshot%d.png"%i)
            i=i+1
            speakout("screenshot has been saved on desktop")


        elif "friday increase brightness" in query:
            speakout("increasing brightness")
            sbc.set_brightness(75)
            print(sbc.get_brightness)


        elif "friday decrease brightness " in query:
            speakout("decreasing brightness")
            sbc.set_brightness(30)
            print(sbc.get_brightness)


        elif "friday tell me current date time" in query:
            def update():
                time_string = strftime("%I:%M:%S %p")
                time_label.config(text=time_string)

                day_string = strftime("%A")
                day_label.config(text=day_string)

                date_string = strftime("%B %d,%Y")
                date_label.config(text=date_string)

                time_label.after(1000, update)

            window = Tk()
            window.configure(bg="black")
            time_label = Label(window, font=("Arial", 50), fg="yellow", bg="black")
            time_label.pack()

            day_label = Label(window, font=("Ink free", 50), fg="pink", bg="black")
            day_label.pack()

            date_label = Label(window, font=("Ink free", 50), fg="pink", bg="black")
            date_label.pack()

            update()
            day = strftime("%A")
            speakout("The current day is %s"%day)
            dates = strftime("%B %d,%Y")
            speakout("and today's date is %s"%dates)
            times=strftime("%I:%M")
            speakout("and current time is %s"%times)


            window.mainloop()


        elif "friday open calendar reminder" in query:
            speakout("set your reminder")
            class EventSchedulerApp:
                def __init__(self, master):
                    self.master = master

                    master.title("Event Scheduler")
                    self.events = {}

                    self.background_image = PhotoImage(file="C:/Users/chhay/OneDrive/Documents/perfectlady.png")
                    self.background_label = Label(master, image=self.background_image)
                    self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

                    self.label = Label(master, text="Enter Event Name and Time(dd-mm-yyyy HH:MM)", font=("Joanna Eve", 15))
                    self.label.pack()


                    self.event_name_entry = Entry(master, width=25)
                    self.event_name_entry.pack(pady=5)


                    self.event_time_entry = Entry(master, width=25)
                    self.event_time_entry.pack(pady=5)


                    self.add_button = Button(master, text="Add Events", font=("Arial", 13), command=self.add_event)
                    self.add_button.pack()


                    self.quit_button = Button(master, text="Quit", font=("Arial", 13), command=master.quit)
                    self.quit_button.pack()

            
                def add_event(self):
                    event_name = self.event_name_entry.get()
                    event_time_str = self.event_time_entry.get()


                    try:
                        event_time = datetime.strptime(event_time_str, "%d-%m-%Y %H:%M")
                

                    except ValueError:
                        messagebox.showerror("Error", "Invalid date/time format. Please use DD-MM-YYYY HH:MM.")
                        return

                    self.events[event_name] = event_time
                    messagebox.showinfo("Success", f"Event '{event_name}' scheduled successfully!")

                    self.event_name_entry.delete(0, END)
                    self.event_time_entry.delete(0, END)

                    self.schedule_event(event_name, event_time)

                def schedule_event(self, event_name, event_time):
                    current_time = datetime.now()

                    time_difference = event_time - current_time

                    if time_difference.total_seconds() <= 0:
                        return 

                    delay_seconds = time_difference.total_seconds()
                    t = Timer(delay_seconds, self.show_notification, args=[event_name])
                    t.start()


                def show_notification(self, event_name):

                    notification.notify(title="Event Reminder",
                                    message=f"It's time for {event_name}!",
                                    timeout=20)
                    
            def main():
                root = Tk()
                root.geometry("600x400")
                app = EventSchedulerApp(root)
                root.mainloop()


            if __name__ == "__main__":
                main()


        elif "friday open weather app" in query:
            speakout("opening weather app")
            w = 0
            def get_weather_icon(icon_code):

                icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"
                icon_response = requests.get(icon_url)
                icon_data = icon_response.content


                with open("weather_icon.png", "wb") as icon_file:
                    icon_file.write(icon_data)

            def getweather(window):

                city = text1.get()  
                api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=6856dd2337b92aec9b18d0f019b3b66e"
                

                json_data = requests.get(api).json()

                condition = json_data["weather"][0]["main"]

                temp = int(json_data["main"]["temp"] - 273.15)

                pressure = json_data["main"]["pressure"]

                icon_code = json_data["weather"][0]["icon"]

                final_info = condition + "\n" + "Temp:" + str(temp) + "°C"

                final_data = "Pressure:" + str(pressure) +"Pa"

                text2.config(text=final_info)

                text3.config(text=final_data)

                get_weather_icon(icon_code)

                icon_image = Image.open("weather_icon.png")

                icon_photo = ImageTk.PhotoImage(icon_image)

                weather_icon_label.config(image=icon_photo)

                weather_icon_label.image = icon_photo 

            window = Tk()

            window.configure(bg="sky blue")

            window.geometry("500x500")

            window.title("WEATHER APP")

            font1 = ("Arial", 25, "bold")

            font2 = ("Ink free", 25, "bold")

            font3 = ("Ink free", 25, "bold")
            
            text1_label = Label(window, font=font3, text="Enter the city:", fg="black", bg="sky blue")

            text1 = Entry(window, font= font1)
            text1_label.pack(pady=5)

            text1.pack(pady=20) 
             
            text1.bind('<Return>', getweather)

            btn = Button(window, text="SEARCH", command=lambda: getweather(""))
            btn.pack(pady=5)

            text2 = Label(window, font=font2, fg="dark green", bg="sky blue")
            text2.pack(pady=5)

            text3 = Label(window, font=font2, fg="dark green", bg="sky blue")
            text3.pack(pady=5)

            weather_icon_label = Label(window)
            weather_icon_label.pack()

            window.mainloop()
            
        

        
    print("Thanks for using  Chhaya and Tanvi's voice assistant")
