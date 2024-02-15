import pyttsx3 #----------------package used for audio------------------<pip install pyttsx3>
import platform as p#----------------it is used to get details of pc---------------
import socket as s#---------------------------it is used get ip addresses of our system and its network systems-----------------
from phonenumbers import geocoder# ----------------------------it is used  to get geolocation of phonenumber----------------------------<pip install phonenumbers>
from phonenumbers import carrier#-------------------------------it is used to show service provider--------------------------------------
import phonenumbers as ph
import cv2 # ----------------------------------------used  to access the camera---------------------<pip install opencv-contrib-python>
import numpy as np


a=pyttsx3.init("sapi5")
voice=a.getProperty("voices")
audio="hello sir ,welcome , I AM MARK YOUR ASSISTANT\n choose option to perform\n 1. DETAILS OF YOUR PC \n 2. IP ADDRESS OF YOUR DEVICE \n 3. DETAILS OF  A PHONE NUMBER \n 4. open camera \n 5. openning the camera in black and white mode\n 6. send a whatsapp message\n7. see the clock for time\n8. open the website "
a.setProperty("voices",voice[1].id)
print(audio)
a.say(audio)
for i in range(1,9):
    a.say("enter choice")
    a.runAndWait()
    # Python program to translate
    # speech to text and text to speech
    import speech_recognition as sr
    # Initialize the recognizer
    r = sr.Recognizer()
    # Function to convert text to
    # speech
    def SpeakText(command):
        # Initialize the engine
        engine = pyttsx3.init()
        engine.say(command)
	engine.runAndWait()
    # Loop infinitely for user to
    # speak
    while(1):
        # Exception handling to handle
        # exceptions at the runtime
        try:
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                # wait for a second to let the recognizer
		# adjust the energy threshold based on
		# the surrounding noise level
		r.adjust_for_ambient_noise(source2, duration=0.2)
			
		#listens for the user's input
		audio2 = r.listen(source2)
			
		# Using google to recognize audio
		MyText = r.recognize_google(audio2)
		MyText = MyText.lower()

		print("Did you say ",MyText)
			SpeakText(MyText)
			
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:
		print("unknown error occurred")

    
    if MyText=="one"or MyText=="One" or MyText=="1":
        def details(): 
            info={}
            # platform details
            p1=p.platform()
            info["platform details"] = p1
            system_name = p.system()
            info["system name"] = system_name
            processor_name = p.processor()
            info["processor name"] = processor_name
            architecture_details = p.architecture()
            info["architectural detail"] = architecture_details
            h=s.getfqdn()
            info["device name"]=h
            ip=s.gethostbyname(h)
            info["ip-address"]=ip
            for i, j in info.items():
                print(i, " --> ", j)
                a.say(i)
                a.say(j)
                a.runAndWait()
        details()
    elif n==2:#for ip address
        def ip():
            a.say("enter device name:")
            a.runAndWait()
            host=input("enter device name:")
            print("your ip address is :",s.gethostbyname(host))
            a.say("your ip address is :")
            a.say(s.gethostbyname(host))
            a.runAndWait()
        ip()
    elif n==3:#phone number details
        def phone():
            a.say("enter phonenumber with country code:")
            a.runAndWait()
            s=input("enter phonenumber with country code:")
            q=ph.parse(s)
            print(geocoder.description_for_number(q,'en'))
            a.say("your are in")
            a.say(geocoder.description_for_number(q,'en'))
            print("your service provider:",carrier.name_for_number(q,'en'))
            a.say("your service provider")
            a.say(carrier.name_for_number(q,'en'))
            a.runAndWait()
        phone()
    elif n==4:
        print("openning the camera")
        a.say("openning the camera")
        a.runAndWait()
        import numpy as np
        import cv2
        cap=cv2.VideoCapture(0)
        cap.set(3,640)#set width
        cap.set(4,480)
        while True:
            ret,frame=cap.read()
            frame=cv2.flip(frame,1)#flip camera verically
            #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            cv2.imshow("frame",frame)
            #cv2.imshow("gray",gray)
            k=cv2.waitKey(1)&0xff
            if k==7:
                break
        cap.release()
        cv2.destroyAllwindows()
        
    elif n==5:
        print("openning the camera in black and white mode")
        a.say("openning the camera in black and white mode")
        a.runAndWait()

        import numpy as np
        import cv2
        cap=cv2.VideoCapture(0)
        cap.set(3,640)#set width
        cap.set(4,480)
        while True:
            ret,frame=cap.read()
            #frame=cv2.flip(frame,1)#flip camera verically
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            cv2.imshow("frame",frame)
            cv2.imshow("gray",gray)
            k=cv2.waitKey(30)&0xff
            if k==7:
                break
        cap.release()
        cv2.destroyAllwindows()
    elif n==6:
        def wh():
            import pywhatkit
            a.say("link your phone with whatsapp web ,then type yes to proceed further")
            print("link your phone with whatsapp web ,then type yes to proceed further")
            a.runAndWait()
            y=input()
            if y=="yes" or y=="YES" or y=="Yes":
                a.say("enter the message to send:")
                a.runAndWait()
                msg=input("enter the message to send:")
                a.say("enter the mobile number of the person that you want to send this message")
                a.runAndWait()
                number=input("enter the mobile number of the person that you want to send this message")
                a.say("enter hours in 24 hours format:")
                a.runAndWait()
                h=int(input("enter hours in 24 hours format:"))
                a.say("enter at what minute to send this message:")
                a.runAndWait()
                m=int(input("enter at what minute to send this message:"))
                try:
                    pywhatkit.sendwhatmsg("+91"+number,msg, h,m)
                    a.say("message sended sir")
                    a.runAndWait()
                    print("message sended sir")
                except:
                    print("sorry for disturbence , check once  your phone is connected to whatsapp web or not")
        wh()
    elif n==7:
        a.say("CLOCK opened SIR")
        a.runAndWait()
        import tkinter as t
        from tkinter import *
        import time
        w=t.Tk()
        def clock():
            hour=time.strftime("%I")
            minute=time.strftime("%M")
            second=time.strftime("%S")
            zone=time.strftime("%p")
            tt=hour+":"+minute+":"+second+""+zone
            c.config(text=tt)
            c.after(1000,clock)
        w.geometry("400x400")
        w.title("clock")
        c=t.Label(w, text="00:00:00" ,height=400 ,width=400,font="algerian 72 bold",background="Dodgerblue",foreground="yellow")
        c.pack()
        clock()
        w.mainloop()
        a.say("CLOCK closed SIR")
        a.runAndWait()
    elif n==8:
        import webbrowser 
        c=input("do want to enter url or  a word:")
        if c=="word"or c=="WORD" or c=="Word":
                from googlesearch import search
                query = input("enter the word to search:")
                import wikipedia
                print(wikipedia.summary(query, sentences=1))  

                my_results_list = []
                for i in search(query,        # The query you want to run
                                tld = 'com',  # The top level domain
                                lang = 'en',  # The language
                                num = 1,     # Number of results per page
                                start = 0,    # First result to retrieve
                                stop = 5,  # Last result to retrieve
                                pause = 2.0,  # Lapse between HTTP requests
                                ):
                    my_results_list.append(i)
                    print(i)
                    webbrowser.open(i)
                    a.say("browser opened, searching completed sir")
                    a.runAndWait()
        else:
            c=input("enter url:")
            webbrowser.open(c)
            a.say("browser opened, searching completed sir")
            a.runAndWait()
            
