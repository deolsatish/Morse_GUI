from tkinter import *
import RPi.GPIO as GPIO
from time import sleep

Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
Morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)


win=Tk()
win.title("Gui Morse Code")
label = Label(win, text = "Enter String here:")
#label.grid(row = 0, column= 0)
label.pack()
 
text = Entry(win, width = 18);
#text.grid(row = 1,column = 0)
text.pack()


def dot():
    GPIO.output(40, GPIO.HIGH) # Turn on
    sleep(0.25)
    GPIO.output(40, GPIO.LOW) # Turn off
    sleep(0.25) # Sleep for 1 second
    print(".")
    
    
def dash():
    GPIO.output(40, GPIO.HIGH) # Turn on
    sleep(0.75)
    GPIO.output(40, GPIO.LOW) # Turn off
    sleep(0.75) # Sleep for 1 second
    print("-")


    
def morsegenerator():
    inputtext=text.get()
    inputtext.upper()
    length=len(inputtext)
    
    if(length<=12):
        for i in range(length):
            num=Alphabet.index(inputtext[i].upper())
            print(num)
            print(inputtext[i])
            for char in Morse[num]:
                if(char=='-'):
                    dash()
                if(char=='.'):
                    dot()
                    
    if(length>12):
        print("Too Long")
        
        
        
startconversion=Button(text="Start Morse Conversion",height=2,width=20, command=morsegenerator)
#startconversion.grid(row=4,column=0)
startconversion.pack()

def close():
	GPIO.cleanup()
	win.destroy()


exitbutton=Button(win, text='Exit',command=close, bg='red')
#exitbutton.grid(row=5,column=1)
exitbutton.pack()

win.protocol("WM_DELETE_WINDOW", close) #exit cleanly

win.mainloop()