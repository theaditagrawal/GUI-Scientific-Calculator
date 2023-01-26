"""
Python Miniproject
GUI Scientific Calculator
A simple scientific calculator with a GUI front end that supports arithmatic, trigonometric, hyperbolic and logarithmic operations.
@authors: Adit Agarwal (PES1202202067), Aditya Jain (PES1202202033), Akilan Elango (PES1202202220) 

"""


from tkinter import *
import math

#Function to handle button clicks
def click(value):
    ex = entryField.get()  #gets input into the entry field
    answer = ''
    input_string = ex
    try:
        if value == 'C':  #handles backspace
            ex = ex[0:len(ex) - 1]  #removes last character
            entryField.delete(0, END)  #clears entry field
            entryField.insert(0, ex)  #inserts modified input
            return

        elif value == 'CE':  #handles clear entry
            entryField.delete(0, END)

        elif value == '√': #handles square root
            answer = math.sqrt(eval(ex))

        elif value == 'π': #inputs pi
            answer = math.pi

        elif value == 'cosθ': #handles cosine
            answer = math.cos(math.radians(eval(ex)))

        elif value == 'tanθ':  #handles tangent
            answer = math.tan(math.radians(eval(ex)))

        elif value == 'sinθ':  #handles sine
            answer = math.sin(math.radians(eval(ex)))

        elif value == '2π': #inputs 2*pi
            answer = 2 * math.pi

        elif value == 'cosh': #handles hyperbolic cosine
            answer = math.cosh(eval(ex))

        elif value == 'tanh': #handles hyperbolic tangent
            answer = math.tanh(eval(ex))

        elif value == 'sinh': #handles hyperbolic sine
            answer = math.sinh(eval(ex))

        elif value == chr(8731): #handles cube root
            answer = eval(ex) ** (1 / 3)

        elif value == 'x\u02b8': #handles x^n
            entryField.insert(END, '**')
            return

        elif value == 'x\u00B3': #handles x^3
            answer = eval(ex) ** 3

        elif value == 'x\u00B2': #handles x^2
            answer = eval(ex) ** 2

        elif value == 'ln': #handles natural log
            answer = math.log(eval(ex))

        elif value == 'deg': #converts radian to degree measure
            answer = math.degrees(eval(ex))

        elif value == "rad": #converts degree to radian measure
            answer = math.radians(eval(ex))

        elif value == 'e': #inputs Euler's number
            answer = math.e

        elif value == 'log₁₀': #handles log base 10.
            answer = math.log10(eval(ex))

        elif value == 'x!': #handles factorial of a number
            answer = math.factorial(eval(ex))

        elif value == chr(247): #handles division
            entryField.insert(END, "/")
            return

        elif value == '=': #handles equations
            answer = eval(ex)

        else:  #handles inputs of numbers and operators.
            entryField.insert(END, value)
            return

        output_field.delete(0, END)
        output_field.insert(0, answer)

#Error handling for SyntaxError, ZeroDivisionError, ValueError and OverflowError.

    except (SyntaxError, ZeroDivisionError, ValueError, OverflowError) as error:
        print("ERROR")

#Function to implement Keyboard shortcuts for operations.    
def keyStroke(event):
  value=event.char
  if event.keysym=="BackSpace": #Maps backspace key to "C" operation.
    value="C"
  elif event.keysym=="Return": #Maps Enter key to "=" operation.
    value="="  
  elif event.keysym=="E": #Maps "E" key to "CE" function
    value="CE"  
  elif event.keysym=="q": #Maps "q" key to "√" operation.
    value="√"
  elif event.keysym=="p": #Maps "p" key to "π" operation.
    value="π"
  elif event.keysym=="P": #Maps "P" key to "2π" operation.
    value="2π"
  elif event.keysym=="Q": #Maps "Q" key to division operartion
    value=chr(8731)
  elif event.keysym=="l": #Maps "l" key to natural log operation.
    value="ln"
  elif event.keysym=="L": #Maps "L" key  to log base 10 operation.
    value="log₁₀"        
  elif event.keysym=="c": #Maps "c" key to cosine operation.
    value="cosθ"
  elif event.keysym=="t": #Maps "t" key to tangent operation.
    value="tanθ"
  elif event.keysym=="s": #Maps "s" key to sine operation.
    value="sinθ"
  elif event.keysym=="C": #Maps "C" key to hyperbolic cosine operation.
    value="cosh"
  elif event.keysym=="T": #Maps "T" key to hyperbolic tangent operation.
    value="tanh"
  elif event.keysym=="S": #Maps "S" key to hyperbolic sine operation.
    value="sinh"
  elif event.keysym=="d": #Maps "d" key to radians to degrees conversion.
    value="deg"
  elif event.keysym=="r": #Maps "r" key to degrees to radians conversion.
    value="rad"
  elif event.keysym=="f": #Maps "f" key to factorial operation.
    value="x!"
  elif event.keysym=="F": #Maps "F" key to x^n operation.
    value="x\u02b8"
  elif event.keysym=="i": #Maps "i" key to x^2 operation.
    value="x\u00B2"
  elif event.keysym=="I": #Maps "I" key to x^3 operation.
    value="x\u00B3"                                    
  click(value)     #Calls click(value) function and nests it within keyStroke(event). 

def add(a,b): #Function to handle addition.
    return a+b
def sub(a,b): #Function to handle subtraction.
    return a-b
def mul(a, b): #Function to handle multiplication.
    return a * b
def div(a, b): #Function to handle division.
    return a / b
def mod(a, b): #Function to handle modulus operation.
    return a % b
def lcm(a,b): #Function to return LCM of two numbers. Future Usecase
    return (math.lcm(a,b))
def hcf(a,b): #Function to return HCF of two numbers. Future Usecase
    return(math.gcd(a,b))

operations={'ADD':add,'ADDITION':add,'SUM':add,'PLUS':add,
            'SUBTRACTION':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
            'PRODUCT': mul, 'MULTIPLICATION': mul,'MULTIPLY': mul,
            'DIVISION': div, 'DIV': div, 'DIVIDE': div,
            'LCM':lcm , 'HCF':hcf,
            'MOD':mod ,'REMAINDER':mod , 'MODULUS':mod }
#Function to filter out non-integers. Future usecase
def findNumbers(t):
    l=[]
    for num in t:
        try:
            l.append(int(num))
        except ValueError:
            pass
    return l
#GUI Implementation
root=Tk()  #Creating the GUI Window
root.title("Scientific Calculator") #Title
root.config(bg='aqua') #Background Colour
root.geometry('700x625+100+100') #Window dimensions
root.bind_all("<Key>", keyStroke) #Connects keyboard mapping to GUI buttons.

input_label = Label(root, text="Input", font=('arial',20,'bold'), bg='aqua', fg='black') #Title for Input Label
input_label.grid(row=0, column=0, padx=5, pady=5, columnspan=10)

entryField=Entry(root,font=('arial',20,'bold'),bg='aqua',fg='black',bd=10,relief=SUNKEN,width=45) #Input label, Expression is stored and displayed
entryField.grid(row=1,column=0,padx=5,pady=5, columnspan=10)

output_label = Label(root, text="Output", font=('arial',20,'bold'), bg='aqua', fg='black') #Title for Output Label
output_label.grid(row=2, column=0, padx=5, pady=5, columnspan=10)

output_field = Entry(root, font=('arial',20,'bold'),bg='aqua',fg='black',bd=10,relief=SUNKEN,width=45) #Output label, Answer is displayed.
output_field.grid(row=3, column=0, padx=5, pady=5, columnspan=10)

button_list= ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",        
                    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                    "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]                      #List of buttons.

'''
Implementing and displaying the buttons on the GUI window.
Defining and storing parameters for the button:
1. dimensions and relief.
2. Colour and font.
Establishing dimensions within a row in which the buttons can be stacked to maintain a clean look.

'''
rowval=4
columnval=0
for i in button_list:
 button=Button(root,font=('arial',18,'bold'),bg='aqua',fg='black',bd=2,relief=SUNKEN,width=5,height=2,text=i,command= lambda button=i: click(button))
 button.grid(row=rowval,column=columnval)
 columnval=columnval+1
 if columnval>7:
  rowval=rowval+1
  columnval=0
root.mainloop() #Running the GUI window.