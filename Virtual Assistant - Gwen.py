#VIRTUAL ASSISTANT - GWEN
#designed by Anurag Sen

import speech_recognition as sr
import datetime
import pyttsx3 as speak
import pywhatkit
import wikipedia
import pyjokes
import wolframalpha as mybrain
import sys
import smtplib as mail
import random
import COVID19Py as covidnews
from plyer import notification
import time as clock
import webbrowser


Gwen = speak.init()

voice = Gwen.getProperty("voices")
Gwen.setProperty('voice', voice[1].id)

rate = Gwen.getProperty("rate")
Gwen.setProperty("rate",170)

client = mybrain.Client('YOUR WOLFRAM ALPHA CLIENT KEY') #Get your Wolfram Alpha client key generated from https://www.wolframalpha.com/

A = datetime.datetime.now()

date = A.strftime("%d %m %Y")
time = A.strftime("%H:%M")
day = A.strftime("%A")


def speak(word):
    Gwen.say(word)
    Gwen.runAndWait()
    return word



def hear():
    p = sr.Recognizer()
    with sr.Microphone() as origin:
        audio = p.record(origin, duration=5)
    
        try:
            dial = p.recognize_google(audio,language='en IN') 
            return dial
    
    
        except sr.UnknownValueError:
            Gwen.say("Voice input unclear")
            Gwen.runAndWait()


print("Activation attempt: ")

dial = hear()

print("Recieved Voice Input:", dial)

try:
    dialogue = dial.lower()
    
    mt = ["Good Morning. I am Gwen, your virtual assistant","Heyy! It's me Gwen. Your Virtual assistant! Its Morning Already! ","Its Morning! Lets get back to work! This is me, Gwen! Your Virtual friend!","The sun is already out! Its Morning! I am Gwen. Your Virtual Assistant"]
    at = ["Good Afternoon. I am Gwen, your virtual assistant","Heyy! It's Gwen. Good Afternoon!","Good Afternoon amigo! I am Gwen! Lets get back to work!","Afternoon Already! Lets Get back to work! This is me.. Gwen!","Hope you had your lunch! Its Afternoon already. Lets get back to work! This is Gwen!"]
    et = ["Good Evening. I am Gwen, your virtual assistant","Done with the evening tea? This is Gwen. The virtual assistant!","Welcome back! Its the evening hour with your favorite assistant Gwen!","Heyy Good Evening! Its me Gwen! I'll do the work! You just get me a cup of tea. ","So You're back! Good Evening. I'm Gwen . It'll me night soon so let's finish the work quick!"]
    nt = ["Good Night. I am Gwen, your virtual assistant","Welcome back! This is the night hour! As of now, Alfred the butler is not here. I am Gwen. Your virtual butler!","Its already dark outside! Lets finish the work quick and get back to sleep! I am your favorite and personal assistant Gwen","Good Night! We're into the dark! This is Gwen, your assistant! Lets get back to work!"]
        
    if 'gwen' in dialogue:
        
        print("\n")
        print('Command Keywords-')
        print('1. time - to know the time')
        print('2. date - to know the date')
        print('3. day - to know the day')
        print('4. Hold on - to make Gwen wait')
        print('5. virus news - to get updates on covid19')
        print('6. tell me - to get answers of queries')
        print('7. remind me - to set a reminder')
        print('8. mail - to send a mail using gmail')
        print('9. open my google account - to open your gmail inbox')
        print('10. open a website - to open desired website')
        print('11. search - to speak a wikipedia search')
        print('12. look for - do a Google search')
        print('13. joke - hear a joke')
        print('14. play - play something on youtube')
    
        if time >= "05:00" and time < "12:00":
            speak(random.choice(mt))
            
        elif time >= "12:00" and time < "17:00":
            speak(random.choice(at))
            
        elif time >= "17:00" and time < "21:00":
            speak(random.choice(et))
            
        else:
            speak(random.choice(nt))
      
        
        Self = {"good morning gwen":"good morning!", "good evening": "good evening sir" , "ok" : "yes" , "oh":"hope i got it right!" , "good afternoon": "good afternoon sir" , "good morning": "good morning sir" ,"i woke up":"Wow! Now that's a miracle!","hello":"hii there","hi":"heyy","who are you":"my name is Gwen","what are you":"I am your computer brought to life.","who made you":"I am designed by Anurag Sen","what are you made on":"I am built using Python"}
        Greetings = {"bye":"Good Bye!","good night":"yeah! good bye! Its late already! you should sleep","goodbye":"hope you had a nice time!"}    
            
        while True:
            
    
                speak("How can I help you?")

                print("\n")
                print("How can I help you?")
                print("\n")
                
                
                comm = hear()
                
                command = comm.lower()
                
            
                if 'time' in command:
                    time12 = A.strftime("%I:%M %p")
                    speak("It is " + time12 + " now")
                    print("It is " + time12 + " now")
                
                        
                elif 'date' in command:
                    speak("The date today is " + date)
                    print("The date today is " + date)
                    
                    
                elif 'hold on' in command:
                    speak("Okay I'll wait!")
                    clock.sleep(20)
                
                    
                elif 'day' in command:
                    speak("Today is " + day)
                    print("Today is " + day)
                    
                    
                elif 'virus news' in command:
                    update = covidnews.COVID19(data_source='jhu')
                    latest = str(update.getLatest())
                    speak("The following is a Covid19 update and is based on the updates from The Johns Hopkins University, Maryland." + " World wide estimation " + latest)
                    print("The following is a Covid19 update and is based on the updates from The Johns Hopkins University, Maryland." + " World wide estimation " + latest)
                    
    
                elif 'tell me' in command:
                    try:
                        content = command.replace('tell me','')
                        res = client.query(content)
                        print(content.upper())
                        speak('Searching' + content)
                        output = next(res.results).text
                        speak(output)
                        print(output)
                    except:
                        speak("Sir. This entry is out of my reach. I apologize. Try the same entry with the search keyword or Try something else!")
                
                
                elif 'remind me' in command:
                   
                    speak("What should i remind you?")
                    reminder_title = hear()
                    speak("What should be the reminder message?")              
                    reminder_msg = hear()
                    speak("Please Enter the reminder duration in minutes.")
                    remind_time = float(input("Enter the reminder duration in minutes: "))
                                    
                    clock.sleep(60*remind_time)
                    notification.notify(title =  reminder_title ,message = reminder_msg ,app_icon = "path")
                    speak("Reminder Alert")
                    
                elif 'mail' in command:
                    myself = 'sender@email_address'
                    speak("Who should I mail?")
                    receiver_mail = input("Who should I mail? : ")
                    speak("What should I write?")
                    msg = hear()
                    server = mail.SMTP('smtp.gmail.com',587)
                    server.starttls()
                    server.login(myself, "password")
                    server.sendmail(myself, receiver_mail, msg)
                    speak("Mail Delivered!")
                    
                elif 'open my google account' in command:
                    speak("Opening your gmail account!")
                    webbrowser.open('link to your gmail inbox')

                
                elif 'open a website' in command:
                    speak("Which website should i open?")
                    websitelink = hear()
                    speak("Opening" + websitelink)
                    webbrowser.open(websitelink)
    
                elif 'search' in command:
                    content = command.replace('search','')
                    speak("Searching for " + content)
                    item = wikipedia.summary(content,2)
                    print(content.upper())
                    speak(item)
                    print(item)

                    
                elif 'look for' in command:
                    content = command.replace('look for','')       
                    speak("Looking for " + content)
                    item = pywhatkit.search(content)
                
                
                elif 'joke' in command:
                    speak("Okay! Let's have fun!")
                    joke = pyjokes.get_joke()
                    speak(joke)

                        
                elif 'play' in command:
                    video = command.replace('play','')
                    speak("Playing " + video)
                    print("playing...")
                    pywhatkit.playonyt(video)
                    speak("Enjoy!")
                    break
                
                for talk in Self:
                    if talk in command:
                        speak(Self[talk])
                    
                    
                for greet in Greetings:
                    if greet in command:
                        speak(Greetings[greet])
                        speak("Aborting the Assistance Process. See you next time!")
                        sys.exit()
                
    else:
        speak("Unauthorized Access attempt! Make sure we are familiar!")
                
except:
    pass        
                
        
        
        
            