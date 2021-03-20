import pyttsx3  # support to cconvert text to speech
import datetime  # it will give current date and time
import speech_recognition as sr  # recognize the speech with microphone
import wikipedia  # give the information from the wikipedia
import webbrowser  # it will use to open any website
import os  # give acccess to the ssystem
import smtplib  # this module is use to send email
import random  # it will genrate the random number
import psutil  # use to fetch value from current battery
import screen_brightness_control as sbc  # use to increase the brightness or decrease
import requests
import time
import wolframalpha  # api which give certain question of answer
import pyjokes
from selenium import webdriver
import cv2
import subprocess  # use to call application
from PIL import ImageGrab
import file_search  # to search a file
import pyzbar.pyzbar as pyzbar  # this module is used to decode the barcode
import numpy as np

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from Second_UI import Ui_Frond_End_GUI  # This is file UI file class
import sys

# import mixer


# wolframe API
wol_app_id = "sd"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    # print("test first")
    engine.runAndWait()
    # print("test")


def wishme():
    hour = int(datetime.datetime.now().hour)
    # tt= time.strftime("%I:%M %p")
    print("2")
    if hour >= 0 and hour < 12:
        speak("good morning ")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon ")
    else:
        speak("Good Evening")

    speak("i am Jarvis Sir. please tell me how may i help you : ")


def SendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("sample@gmail.com", "pass@123")
    server.sendmail("sample@gamil.com", to, content)
    server.close()


def Increase_brightness():
    try:
        currrent_brightness = sbc.get_brightness()
        increased_brightness = currrent_brightness + 10
        sbc.set_brightness(increased_brightness)
    except Exception as e:
        speak("sir brightness is full")


def Decrease_brightness():
    try:
        currrent_brightness = sbc.get_brightness()
        decreased_brightness = currrent_brightness - 10
        sbc.set_brightness(decreased_brightness)
    except Exception as e:
        speak("sir brightness is low")


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.code()

    def takeCommandfromUser(self):
        """ Its take input from microphone and return in string type """
        r = sr.Recognizer()
        with sr.Microphone() as source:

            print("Listining...")
            r.energy_threshold = 800
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=0.3)
            # print("1")
            audio = r.listen(source, phrase_time_limit=5)  # pause time
            # print("2")
            try:
                print("Recognization...")
                query = r.recognize_google(audio, language='en-in')
                print(f"User said : {query}\n")
            except Exception as e:
                print("Say it again : ")
                return "None"

        return query

    def code(self):

        wishme()
        while 1:
            self.query = self.takeCommandfromUser().lower()
            # logic for executing based on query
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'  # path of chrome
            if 'wikipedia' in query:
                speak('Searching wikipedia')
                query = query.replace('wikipedia', "")
                results = wikipedia.summary(query, sentences=2)
                speak('According to wikipedia')
                print(results)
                speak(results)
            elif 'open youtube' in self.query:
                # webbrowser.open('youtube.com')
                webbrowser.get(chrome_path).open('youtube.com')

            elif 'open google' in self.query:
                webbrowser.get(chrome_path).open('google.com')


            elif 'open stackoverflow' in self.query:
                webbrowser.get(chrome_path).open('stackoverflow.com')

            elif 'open github' in self.query:
                webbrowser.get(chrome_path).open_new_tab(
                    'https://github.com/stifler68')

            # some talk function
            # elif 'how are you' in query:
            #     speak("I am fine, Thank you")
            #     speak("How are you, Sir")

            elif "what\'s up" in self.query or 'how are you' in self.query:
                n = random.randint(1, 4)
                stMsgs = ['Just doing my thing!', 'I am fine! and what about you sir!', 'Nice! ',
                          'I am nice and full of energy']
                speak(random.choice(stMsgs))


            elif 'fine' in self.query or "good" in self.query:

                speak("It's good to know that your fine")

            elif 'play music' in self.query or 'play' in self.query:
                speak("sir,which song should i play ")
                song_name = self.takeCommandfromUser()

                if "play random" in self.song_name or "random song" in self.song_name or "random music" in self.song_name:

                    n = random.randint(1, 11)
                    music = 'C:\\Music\\audios'
                    songs = os.listdir(music)
                    print(songs)
                    print(songs[n])
                    os.startfile(os.path.join(music, songs[n]))  # playing song


                elif song_name != None:
                    try:
                        song_name = song_name.replace("play", "")
                        print("helloooooooooo")
                        music_path = "C:\\Music\\audios"
                        file_search.set_root(music_path)
                        songs = file_search.searchFile(song_name)
                        # print(songs)
                        song_uri = songs[0]

                        song_in_str = ""
                        for ele in song_uri:
                            song_in_str += ele
                        print(song_in_str)
                        webbrowser.open(song_in_str)

                    except Exception as e:
                        speak('dont have this song')
                        print('dont have this song')

                else:
                    speak("sir please tell the song name ")
                    print("sir please tell the song name ")
                    song_name1 = self.takeCommandfromUser()

                    if (song_name1 != None):
                        song_name1 = song_name.replace("play", "")
                        print("helloooooooooo")
                        music_path = "C:\\Music\\audios"
                        file_search.set_root(music_path)
                        songs = file_search.searchFile(song_name1)
                        # print(songs)
                        song_uri = songs[0]

                        song_in_str = ""
                        for ele in song_uri:
                            song_in_str += ele
                        print(song_in_str)
                        webbrowser.open(song_in_str)

                    else:
                        speak("sir dont get any song suggestion should i play random song ")
                        song_name2 = self.takeCommandfromUser()
                        if (song_name2 == "yes"):
                            n = random.randint(1, 11)
                            music = 'C:\\Music\\audios'
                            songs = os.listdir(music)
                            print(songs)
                            print(songs[n])
                            os.startfile(os.path.join(music, songs[n]))  # playing song
                        else:
                            speak("okay sir please tell another work for me!")



            elif "stop music" in self.query or "close music" in self.query:
                print("stopping music")


            elif 'open notepad' in self.query:
                os.system("start notepad")
                # subprocess.Popen('notepad.exe')
                # subprocess.call(['C:\\Windows\\System32\\Notepad.exe', 'C:\\Python_folder\\File1.txt']) #use for open any .txt file in notepad

            elif 'open command prompt' in self.query:
                # subprocess.Popen('cmd.exe')
                os.system("start cmd")

            elif 'open file manager' in self.query:
                subprocess.Popen(r'explorer /select,"C:\path\of\folder\file"')  # 'r' represent as raw data

            elif 'open calculator' in self.query:
                os.system('start calc')

            elif 'github' in self.query:
                webbrowser.get('chrome').open_new_tab(
                    'https://github.com/gauravsingh9356')


            elif 'the time' in self.query:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir the time is : {strtime}")

            elif "email to parab" in self.query:
                try:
                    speak("What should i say ")
                    content = self.takeCommandfromUser()
                    to = "jayramparab19@gmail.com"
                    SendEmail(to, content)
                    speak("Email has sent ! ")
                except Exception as e:
                    speak("Sorry i cant sent email there is some technical error")
                    print(e)

            elif "email to ravi" in self.query:
                try:
                    speak("What should i say ")
                    content = self.takeCommandfromUser()
                    to = "ravisingh02@gmail.com"
                    SendEmail(to, content)
                    speak("Email has sent ! ")
                except Exception as e:
                    speak("Sorry i cant sent email there is some technical error")
                    print(e)


            elif "show battery status" in self.query:
                battery = psutil.sensors_battery()
                percent = str(battery.percent)
                plugged = battery.power_plugged
                # plugged = "Plugged In" if plugged else "Not Plugged In"
                if plugged:
                    plug = 'plugged'
                else:
                    plug = 'not plugged'
                per = int(percent)
                # plugged = "Plugged In" if plugged else "Not Plugged In"
                if plugged:
                    plug = "plugged"
                else:
                    plug = "not_plugged"

                if plug == 'not_plugged' and per <= 30:
                    speak("Sir your battery is ")
                    speak(percent)
                    speak("sir please pluggin your charger because your battery is low ")
                elif plug == 'plugged' and battery > 20:
                    speak("Sir your battery is ")
                    speak(percent)
                elif plug == 'not_plugged' and per > 20:
                    speak("Sir your battery is ")
                    speak(percent)
                elif plug == 'plugged' and battery <= 20:
                    speak("Sir your battery is ")
                    speak(percent)
                    speak("sir your battery is low dont remove your charger")
                elif plug == 'plugged' and battery == 100:
                    speak("Sir your battery is ")
                    speak(percent)
                    speak("sir your battery is full please remove charger ")
                else:
                    print(percent)

            elif "increase the brightness" in self.query or "yes increase the brightness" in self.query or "increase brightness" in self.query:
                Increase_brightness()
                speak("sir should i increase the brightness or its good")

            elif "decrease the brightness" in self.query or "yes decrease the brightness" in self.query or "decrease brightness" in self.query:
                Decrease_brightness()
                speak("sir should i decrease the brightness or its good")


            # Give weather status
            elif "show weather status" in self.query or "weather status" in self.query:
                speak("sir please wait for while")

                api_key = "0bf38c445cb8545f237f2d0ce54511ee"

                base_url = "http://api.openweathermap.org/data/2.5/weather?"

                city_name = "mumbai"

                complete_url = base_url + "appid=" + api_key + "&q=" + city_name

                response = requests.get(complete_url)

                x = response.json()

                if x["cod"] != "404":

                    y = x["main"]

                    current_temperature = y["temp"]
                    current_pressure = y["pressure"]

                    current_humidiy = y["humidity"]

                    z = x["weather"]

                    weather_description = z[0]["description"]

                    if str(current_temperature) == "288.15":
                        # print("Temperature", 15, "celcius")
                        temp = "15"
                    elif str(current_temperature) == "289.15":
                        temp = "16"
                    elif str(current_temperature) == "290.15":
                        temp = "17"
                    elif str(current_temperature) == "291.15":
                        temp = "18"
                    elif str(current_temperature) == "292.15":
                        temp = "19"
                    elif str(current_temperature) == "293.15":
                        temp = "20"
                    elif str(current_temperature) == "294.15":
                        temp = "21"
                    elif str(current_temperature) == "295.15":
                        temp = "22"
                    elif str(current_temperature) == "296.15":
                        temp = "23"
                    elif str(current_temperature) == "297.15":
                        temp = "24"
                    elif str(current_temperature) == "298.15":
                        temp = "25"
                    elif str(current_temperature) == "299.15":
                        temp = "26"
                    elif str(current_temperature) == "300.15":
                        temp = "27"
                    elif str(current_temperature) == "301.15":
                        temp = "28"
                    elif str(current_temperature) == "302.15":
                        temp = "29"
                    elif str(current_temperature) == "303.15":
                        temp = "30"
                    elif str(current_temperature) == "304.15":
                        temp = "31"
                    elif str(current_temperature) == "305.15":
                        temp = "32"
                    elif str(current_temperature) == "306.15":
                        temp = "33"
                    elif str(current_temperature) == "307.15":
                        temp = "34"
                    elif str(current_temperature) == "308.15":
                        temp = "35"
                    elif str(current_temperature) == "309.15":
                        temp = "36"
                    elif str(current_temperature) == "310.15":
                        temp = "37"
                    elif str(current_temperature) == "311.15":
                        temp = "38"
                    elif str(current_temperature) == "312.15":
                        temp = "39"
                    elif str(current_temperature) == "313.15":
                        temp = "40"
                    else:
                        temp = "41"

                    # print("\n atmospheric pressure (in hPa unit) = " +
                    #       str(current_pressure) +
                    #       "\n humidity (in percentage) = " +
                    #       str(current_humidiy) +
                    #       "\n weather = " +
                    #       str(weather_description))

                    speak("temprature is ")
                    speak(temp)
                    speak("celcius")

                    speak("Atmospheric pressure is ")
                    speak(str(current_pressure))
                    speak("Humidity ")
                    speak(str(current_humidiy))
                    speak("weather is " + weather_description)

                else:
                    print("error occure")

            elif "search in google" in self.query:
                try:
                    speak("What should i search sir ")
                    search_results = self.takeCommandfromUser()
                    speak("its take some time sir ")
                    driver = webdriver.Chrome(
                        executable_path='C:\\Users\\ravi singh\\Downloads\\chromedriver.exe')  # chrome drive path
                    driver.get("https://google.com/")
                    search = driver.find_element_by_name("q")  # name of div class in google inspect
                    search.send_keys(search_results)
                    time.sleep(4)
                    button = driver.find_element_by_name("btnK").click()
                except Exception as e:
                    speak("some error occure")


            elif "solve maths calculation" in self.query:

                speak("okay sir please tell your question")
                question = self.takeCommandfromUser()

                if "plus" in question:
                    question = question.replace("plus", "+")
                elif "minus" in question:
                    question = question.replace("minus", "-")
                elif "multiply" in question:
                    question = question.replace("minus", "-")
                elif "divide" in question:
                    question = question.replace("divide", "/")
                elif "modules" in question:
                    question = question.replace("modules", "%")

                try:
                    print(question)

                    client = wolframalpha.Client(wol_app_id)
                    res = client.query(question)
                    speak("sir it's ")
                    speak(next(res.results).text)
                    print(next(res.results).text)
                except Exception as e:
                    print("wrong input")

            elif 'who is ' in self.query or 'what is ' in self.query:

                client = wolframalpha.Client(wol_app_id)
                res = client.query(query)
                try:
                    print(next(res.results).text)
                    speak(next(res.results).text)
                except Exception as e:
                    print('not found result')
                    speak('result not found sir ')


            elif "jokes" in self.query or "joke" in self.query:
                speak(pyjokes.get_joke())



            elif "camera" in self.query or "take a photo" in self.query:

                speak("Note : sir if you want to capture the image the press on spacebar")
                # 1.creating a video object
                video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

                # 2. Variable
                a = 0
                # 3. While loop
                while True:
                    a = a + 1
                    # 4.Create a frame object
                    check, frame = video.read()
                    # 5.show the frame!
                    cv2.imshow("Capturing", frame)
                    # 6.for playing
                    key = cv2.waitKey(1)

                    if key % 256 == 32:  # 32 ascii value of sapcebar
                        break
                # 7. image saving
                for i in range(100):
                    drive_letter = "C:\\Users\\ravi singh\\PycharmProjects\\Camera_Img\\"
                    folder_name = r'downloaded-files'
                    folder_time = datetime.datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
                    extention = '.jpg'
                    folder_to_save_files = drive_letter + folder_name + folder_time + extention

                    showPic = cv2.imwrite(folder_to_save_files, frame)
                    print(folder_to_save_files)
                    print(showPic)
                    break
                # 8. shutdown the camera
                video.release()
                cv2.destroyAllWindows()



            elif "take a screenshot" in self.query or "take screenshot" in self.query:
                snapshot = ImageGrab.grab()
                drive_letter = "C:\\Users\\ravi singh\\PycharmProjects\\Screenshot\\"
                folder_name = r'downloaded-files'
                folder_time = datetime.datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
                extention = '.jpg'
                folder_to_save_files = drive_letter + folder_name + folder_time + extention
                snapshot.save(folder_to_save_files)
                speak("done sir")
            #
            # elif 'location' in query:
            #     speak('What is the location?')
            #     location = takeCommandfromUser()
            #     url = 'https://google.nl/maps/place/' + location + '/&amp;'
            #     webbrowser.get('chrome').open_new_tab(url)
            #     speak('Here is the location ' + location)

            elif "scan qr code" in self.query:
                cap = cv2.VideoCapture(0)
                cap.set(3, 640)
                cap.set(4, 480)

                while True:
                    success, img = cap.read()
                    for barcode in pyzbar.decode(img):
                        myData = barcode.data.decode('utf-8')
                        print(myData)

                        pts = np.array([barcode.polygon], np.int32)
                        pts = pts.reshape((-1, 1, 2))
                        cv2.polylines(img, [pts], True, (255, 0, 255), 5)

                        pts2 = barcode.rect
                        cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

                    cv2.imshow('Result', img)
                    key = cv2.waitKey(1)
                    if key % 256 == 32:  # 32 ascii value of spacebar
                        break

                cv2.destroyAllWindows()

            elif 'shutdown' in self.query:
                os.system('shutdown /p /f')

            elif "quit" in self.query:
                speak("quitting sir... ")
                quit()


startExecution = MainThread()


class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frond_End_GUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("Resources/TIM.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        startExecution.start()


app = QtWidgets.QApplication(sys.argv)
tim = main()
tim.show()
exit(app.exec_())

