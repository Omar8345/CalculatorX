import tkinter #import tkinter
import tkinter.font as font


window = tkinter.Tk() # create tkinter master window
window.geometry('900x900') # set window size
window.title('My Calculator') # set window title to my calculator
myFont = font.Font(size=15) # buttons font size number


# we need to create these functions before making buttons or we are not able to use them
# then we cannot indentify which button was pressed to calculate properly

def checkbutton1():
    global buttonClicked1
    buttonClicked1 = not buttonClicked1
    print('button 1 clicked')

buttonClicked1 = False # set it false before clicking the button

def checkbutton2():
    global buttonClicked2
    buttonClicked2 = not buttonClicked2
    print('button 2 clicked')

buttonClicked2 = False # set it false before clicking the button
def checkbutton3():
    global buttonClicked3
    buttonClicked3 = not buttonClicked3
    print('button 3 clicked')

buttonClicked3 = False # set it false before clicking the button
def checkbutton4():
    global buttonClicked4
    buttonClicked4 = not buttonClicked4
    print('button 4 clicked')

buttonClicked4 = False # set it false before clicking the button
def checkbutton5():
    global buttonClicked5
    buttonClicked5 = not buttonClicked5
    print('button 5 clicked')

buttonClicked5 = False # set it false before clicking the button
def checkbutton6():
    global buttonClicked6
    buttonClicked6 = not buttonClicked6
    print('button 6 clicked')

buttonClicked6 = False # set it false before clicking the button
def checkbutton7():
    global buttonClicked7
    buttonClicked7 = not buttonClicked7
    print('button 7 clicked')

buttonClicked7 = False # set it false before clicking the button
def checkbutton8():
    global buttonClicked8
    buttonClicked8 = not buttonClicked8
    print('button 8 clicked')

buttonClicked8 = False # set it false before clicking the button

def checkbutton9():
    global buttonClicked9
    buttonClicked9 = not buttonClicked9
    print('button 9 clicked')

buttonClicked9 = False # set it false before clicking the button

# create buttons for the calculator tkinter gui

button1=tkinter.Button(window, text="1", width=10, height=10, command=checkbutton1) # create button 1
button1.grid(row=3,column=1) # arrange button 1 place

button2=tkinter.Button(window, text="2", width=10, height=10, command=checkbutton2) # create button 2
button2.grid(row=3,column=2) # arrange button 2 place

button3=tkinter.Button(window, text="3", width=10, height=10, command=checkbutton3) # create button 3
button3.grid(row=3,column=3) # arrange button 3 place

button4=tkinter.Button(window, text="4", width=10, height=10, command=checkbutton4) # create button 4
button4.grid(row=2,column=1) # arrange button 4 place

button5=tkinter.Button(window, text="5", width=10, height=10, command=checkbutton5) # create button 5
button5.grid(row=2,column=2) # arrange button 5 place

button6=tkinter.Button(window, text="6", width=10, height=10, command=checkbutton6) # create button 6
button6.grid(row=2,column=3) # arrange button 6 place

button7=tkinter.Button(window, text="7", width=10, height=10, command=checkbutton7) # create button 7
button7.grid(row=1,column=1) # arrange button 7 place

button8=tkinter.Button(window, text="8", width=10, height=10, command=checkbutton8) # create button 8
button8.grid(row=1,column=2) # arrange button 8 place

button9=tkinter.Button(window, text="9", width=10, height=10, command=checkbutton9) # create button 9
button9.grid(row=1,column=3) # arrange button 9 place

# set buttons font
button1['font'] = myFont # set button 1 size
button2['font'] = myFont # set button 2 size
button3['font'] = myFont # set button 3 size
button4['font'] = myFont # set button 4 size
button5['font'] = myFont # set button 5 size
button6['font'] = myFont # set button 6 size
button7['font'] = myFont # set button 7 size
button8['font'] = myFont # set button 8 size
button9['font'] = myFont # set button 9 size




print("Welcome to the CalculateX Application...")
window.mainloop()
