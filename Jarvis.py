from tkinter import *
from PIL import ImageTk,Image
import pyttsx3 ##used for speak engine
import speech_recognition as sr # used for voice to text conversion
import datetime # used to extract the current date and time
import webbrowser ## used for opening web sites
import os # to open any app
import wikipedia # to search something in wikipedia
import threading
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
    # print(voices[1].id)
engine.setProperty('voice', voices[0].id)
    
class ActivateJarvis:
    def __init__(self):

        self.__speak("Intializing..")
        print("Intializing ..")
        self.__speak("Welcome back sir ")
    

    def __speak(self,audio):
        engine.say(audio)
        engine.runAndWait()
    def wishme(self):
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            self.__speak("Good Morning!")

        elif hour>=12 and hour<18:
            self.__speak("Good Afternoon!")   

        else:
            self.__speak("Good Evening!")  

        self.__speak("I am Jarvis Sir. Please tell me how may I help you")
        #request=self.__takecommand()
        self.__run()
        
    
    def __takecommand(self):
        self.r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            self.r.pause_threshold=0.5
            self.audio=self.r.listen(source)
        try:
            print("Recognizing...")
            self.query=self.r.recognize_google(self.audio,language='en-in')
            print("{}".format(self.query))
        except Exception as e:
            print("Please say again..")
            return "None"
        return self.query
    def __run(self):
        chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        while True:
            self.requestQuery=self.__takecommand().lower()
            if 'open youtube' in self.requestQuery:
                webbrowser.get('chrome').open_new_tab('youtube.com')
            elif 'what languages you know' in self.requestQuery:
                self.__speak("I am currently learning language")
            elif 'you are fool' in self.requestQuery:
                self.__speak("Apologize sir, I'll try to improve")
            elif 'who are you' in self.requestQuery:
                self.__speak("I am jarvis Artificial intelligence , created for domestic Automation purpose")
            elif 'open prime video' in self.requestQuery:
                webbrowser.get('chrome').open_new_tab('https://www.primevideo.com')
            elif 'open spotify' in self.requestQuery:
                path="C:\\Users\\ACER\\AppData\\Roaming\\Spotify\\Spotify.exe"
                os.startfile(path)
            elif 'hi jarvis' in self.requestQuery:
                self.__speak("Hello sir")
            elif "how is going" in self.requestQuery:
                self.__speak("Everything fine sir")
            elif "who is your owner" in self.requestQuery or "who created you" in self.requestQuery:
                self.__speak("Mr.sai kiran created me and he is my owner")
            elif 'thank you jarvis' in self.requestQuery or 'thank you so much jarvis' in self.requestQuery:
                self.__speak("Most welcome sir!")
            elif 'jarvis open what i like the most' in self.requestQuery:
                webbrowser.get('chrome').open_new_tab('https://www.youtube.com/watch?v=pR7kMQPZV2U')
            elif 'open prasad tech in telugu' in self.requestQuery:
                webbrowser.get('chrome').open_new_tab('https://www.youtube.com/channel/UCb-xXZ7ltTvrh9C6DgB9H-Q')
            elif 'open my channel' in self.requestQuery or 'open my youtube channel' in self.requestQuery:
                webbrowser.get('chrome').open_new_tab('https://www.youtube.com/channel/UCPv9XuCE1Cho5QDYBcqWphA?view_as=subscriber')
            elif 'open the dashboard of my channel' in self.requestQuery:
                webbrowser.get('chrome').open_new_tab('https://studio.youtube.com/channel/UCPv9XuCE1Cho5QDYBcqWphA')
            elif 'open instagram' in self.requestQuery:
                webbrowser.get('chrome').open_new_tab('https://www.instagram.com/')
            elif 'open google classroom' in self.requestQuery or 'open my class room' in self.requestQuery:
                webbrowser.get('chrome').open_new_tab('https://classroom.google.com/u/2/h')
            elif 'open chrome' in self.requestQuery:
                path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(path)
            elif 'google assistant' in self.requestQuery:
                self.__speak('Google assistant is great!')
            elif 'siri' in self.requestQuery:
                self.__speak('siri is awesome')
            elif 'open study files' in self.requestQuery:
                path="D:\\STUDY FILES"
                os.startfile(path)
            elif 'programming' in self.requestQuery:
                path="D:\\STUDY FILES\\PROGRAMMING"
                os.startfile(path)
            elif 'open udemy' in self.requestQuery:
                webbrowser.get('chrome').open_new_tab('https://www.udemy.com/home/my-courses/learning/')
            elif 'open google meet' in self.requestQuery:
                webbrowser.get('chrome').open_new_tab('https://meet.google.com/')
            
            elif 'the time' in self.requestQuery:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                self.__speak(f"Sir, the time is {strTime}")
            elif 'open genius tech' in self.requestQuery:
                webbrowser.get('chrome').open_new_tab('https://saikiran-patro.github.io/Genius-Tech.github.io/index.html')
            elif 'open code with harry' in self.requestQuery:
                webbrowser.get('chrome').open_new_tab('https://www.codewithharry.com/')
            elif 'wikipedia' in self.requestQuery:
                self.__speak("Search wikipedia...")
                self.requestQuery=self.requestQuery.replace("wikipedia","")
                try:
                    
                    result=wikipedia.Summary(self.requestQuery,sentences=3)
                    print(result)
                    self.__speak(result)
                except:
                    self.__speak("sorry sir not found could you please ask again")
            elif 'what can you do for me' in self.requestQuery:
                self.__speak("You can order me anything sir, I am here to help you")
            
                
 
            
            elif 'exit' in self.requestQuery or 'bye jarvis' in self.requestQuery:
                self.__speak("Good Bye sir , will meet you again!")
                exit()
            elif "time table today" in self.requestQuery:
                day=datetime.datetime.now().strftime("%A").lower()
                if day=="sunday":
                    self.__speak("You have no work today sir, you can do whatever you like")
                    
                elif day=="monday":
                    self.__speak("Sir, On monday you have CSE , AWP ,  CAO and MPA LAB")
                elif day=="tuesday":
                    self.__speak("sir, on tuesday you have 2 periods ICA and 2 periods QA")
                elif day=="wednesday":
                    self.__speak("sir, on wednesday you have CSE , AWP , CAO and MPA")
                elif day=="thursday":
                    self.__speak("sir, on thursday  you have CSE , MPA and 2  VA periods also ICA 1 period")
                elif day=="friday":
                    self.__speak("sir, on friday you  have MPA , AWP CAO and ICA lab")
                elif day=="saturday":
                    self.__speak("you have only 2 python classes")
            elif 'do you like' in self.requestQuery:
                self.__speak("I like Technology! because i am created using tech")

                
                
            
                
            
    
        
        
        
        

##gui
root =Tk()
root.geometry("600x630")
root.title("JARVIS")
root.configure(bg="black")
root.iconbitmap('Jarvis31.ico')
file = 'Jarvis3.gif'
info=Image.open(file)
#print(info)
frames=info.n_frames
#print(frames)
im=[PhotoImage(file=file, format=f'gif -index {i}') for i in range(frames)]
count=0
def animation(count):
    b.destroy()
    im2=im[count]
    gif.configure(image=im2)
    count+=1
    if count==frames:
        count=0
    root.after(50,lambda:animation(count))        


if __name__=="__main__":
    

    gif=Label(image="")
    gif.pack()
    b=Button(root,text="start",command=lambda:animation(count))
    b.pack()
    AJ=ActivateJarvis()
    j=Button(root,text="",fg="white",bg="black",padx=500,command=threading.Thread(target=lambda:AJ.wishme()).start())
    j.pack()
    
    
########################################
