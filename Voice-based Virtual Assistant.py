import pyttsx3 #pip install pyttsx3 using cmd (PyPi website to find all modules/libraries)
import speech_recognition as sr #pip install SpeechRecognition
import datetime
import os
import webbrowser
import wikipedia
import random
import pyjokes
import time
import pyautogui
import imdb
engine = pyttsx3.init('sapi5')

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
def takeCommand():
    r = sr.Recognizer() #setting up a recognizer to recognize speech
    with sr.Microphone() as source: #input is through microphone
        print ("Listening......") 
        r.pause_threshold = 1 #waits 1 second before generating a response
        audio = r.listen(source , timeout = 10 , phrase_time_limit = 10)
        try:
            print("Recognizing......")#there are multiple recognizers but we chose Google and chose english(in) as the language which is all stored in the variable query
            query = r.recognize_google(audio, language = 'en-in')
            print("User said:",query)
        except Exception as e:
            speak("Unable to recognize your voice......")
            return "None"
        return query
    
def username(): #introduction
    speak("What should I call you?")
    uname=takeCommand()
    speak("Nice to meet you " + uname)
    speak("How can I help you ma'am?")
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning ma'am!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon ma'am!")
    else:
        speak("Good Evening ma'am!")
    speak("I am your virtual assistant Titan.")

def movie():
    moviesdb = imdb.IMDb()
    speak("Please tell me the movie name Srinidhi")
    text = takeCommand()
    movies = moviesdb.search_movie(text)
    speak("Searching for " + text)
    if len(movies) == 0:
        speak("No results found")
    else:
        speak("I found these: ")
        for movie in movies:
            title = movie["title"]
            year = movie["year"]
            speak(f'{title}-{year}')
            info = movie.getID()
            movie = moviesdb.get_movie(info)
            rate = movie["rating"]
            plot = movie["plot outline"]
            if year<int(datetime.datetime.now().strftime("%Y")):
                speak(f'{title} was released in {year} has IMDB ratings of {rate}. The plot summary of the movie is {plot}')
                break
            else:
                speak(f'{title} will release in {year} has IMDB ratings of {rate}. The plot summary of the movie is {plot}')

def rock():
    user = int(input("Please enter your choice:- \n 1-Rock \2-Paper \3-Scissors"))
    shapes = {1:'rock', 2:'paper', 3:'scissors'}
    if user not in shapes:
        print("Please enter a valid choice")
        exit()
    comp = random.randint(1,3) #lets the computer choose a random choice of num between between 1,2 & 3
    print("you choose", user)
    print("Computer choose", comp)
    if(user == 1) and (comp == 3) or (user == 2) and (comp == 1) or (user == 3) and (comp == 2):
        speak("Congratulations {uname}, you won!")
    elif (user == comp):
        speak("Whoops, Match tied!")
    else:
        speak("Sorry, you lost!")

if __name__ == '__main__':
    wishMe()
    username()
    while True:
        order=takeCommand().lower()

        if 'how are you' in order:
            speak("I am Fine, Thank you.")
            speak ("How are you, ma'am?")

        elif 'fine' in order or 'good' in order:
            speak("I'm glad you're doing well")

        elif 'test' in order or 'ready' in order:
            speak("Oh I am ready! Ask me questions and I will do my best to answer them!")

        elif 'what am i' in order:
            speak("Well, surely you are human as you have created me ma'am.")

        elif 'who are you' in order:
            speak("I’m your virtual assistant Titan, designed to help you with a variety of tasks and provide information. I can answer questions and assist with your daily activities.")

        elif 'tell the audience some cool fun facts about yourself' in order:
            speak("Ooh sure! I am always here to help you day or night and I can provide vast information on any topic")

        elif 'open word' in order:
            npath="C:\\Program Files\\Microsoft Office\\root\\Office16\\winword.exe"
            os.startfile(npath)
            speak("Opening word!")

        elif 'play music' in order:
            npath="C:\\Users\\itsme\\Music\\kuttanandanpunjayile.mp3"
            os.startfile(npath)
            speak("Playing music!")

        elif 'wikipedia' in order:
            speak("Searching......")
            order = order.replace("wikipedia","")
            results = wikipedia.summary(order , sentences=2)#stores the first two sentences of the summary
            speak("According to wikipedia")
            speak(results)

        elif 'open google' in order:
            webbrowser.open("google.com")
            speak("Sure, here is google")
            
        elif 'open amazon' in order:
            webbrowser.open("amazon.in")
            speak("Opening amazon, Happy shopping!")     

        elif 'open youtube' in order:
            webbrowser.open("youtube.com")
            speak("Here is youtube, where you can find millions of videos!")

        elif 'open gmail' in order:
            webbrowser.open("gmail.com")
            speak("Here is your gmail!")
            
        elif 'open stackoverflow' in order:
            webbrowser.open("stackoverflow.com")
            speak("Here it is. Happy Coding!")

        elif "where is" in order: #locates the area on google maps
            order = order.replace("where is","")
            location = order
            speak("Locating......")
            speak(location)
            webbrowser.open("https://www.google.co.in/maps/place/"+location+"")

        elif 'joke' in order:
            speak(pyjokes.get_joke(language="en",category="neutral"))
            speak("Ha ha ha, I hope that made you laugh!")

        elif "write a note" in order:
            speak("What should I write Srinidhi")
            note = takeCommand() #whatever the user says will be stored in this variable called note
            file = open('titan.txt' , 'w') #creates a file named titan.txt and opens it in write mode
            speak("Ma'am, should I include date and time?")
            sn = takeCommand() #whatever the user says will be stored in this variable called sn
            if 'include' in sn:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime) #writes current time which is stored in strTime variable
                file.write(note)
                speak("Done writing a note!")
            else:
                file.write(note)
                speak("Done writing a note!")

        elif 'show note' in order:
            speak("Showing notes")
            file = open('titan.txt' , 'r')#opens the file named titan.txt in read mode
            print(file.read())
            speak(file.read(6))

        elif 'the time' in order:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'take a screenshot' in order:
            speak("Ma'am, please tell me the name for this file.")
            name = takeCommand().lower()
            speak("please hold the screen")
            time.sleep(3)
            img = pyautogui.screenshot() #screenshot function
            img.save(f"{name}.png") #saves screenshot as a png in the given file name
            speak("Screenshot captured successfully!")

        elif 'bmi' in order:
            speak("Please tell me you height in centimeters")
            height = takeCommand()
            speak("Please tell me your weight in kilograms")
            weight = takeCommand()
            height = float(height)/100
            BMI = float(weight)/(height**2)
            speak("Your body mass index is " + str (BMI))
            if (BMI>0):
                if (BMI<=16):
                    speak("You are severly underweight")
                elif (BMI<=18.5):
                    speak("You are underweight")
                elif (BMI <=25):
                    speak("You are healthy")
                elif (BMI <=30):
                    speak("You are overweight")
                else:
                    speak("You are severly overweight")
            else:
                speak("Enter valid details.")

        elif 'movie' in order:
            movie()

        elif 'game' in order:
            speak("Sure! Let's play rock, paper, scissors!")
            rock()

        elif 'exit' in order or 'quit' in order:
            speak("Thank you for using me ma'am. Have a good day!")
    

        

        


            
            

        

        
    
            
            
            
            
            
            

        

            
            
            

        
            
        

        
            
    
