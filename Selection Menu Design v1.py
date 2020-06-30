#Imports
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter.font as font

def Space():
    space =tk.Label(bg=bgSetting, text="\n")
    space.pack()

#Global Variables
fontSize = "Large"
buttonSize = "Small"
fontColour = "Black"
bgColour = "Grey"
errorColour = "OrangeRed3"
bgSetting = ""
fontSetting = ""
titleSize = 0
fontSet = 0
buttonFont = 0
height = 0
width = 0
buttonSetting = ""
#Temporary Values
check = 0
check2 = 0
check3 = 0
check4 = 0


fontColours=["Black", "White", "Light Blue", "Blue", "Dark Blue", "Red", "Purple", "Yellow", "Light Green", "Dark Green"]
bgColours=["Black", "White", "Grey", "Dark Grey", "Light Blue", "Blue", "Dark Blue", "Red", "Purple", "Yellow", "Light Green", "Dark Green", "Neutral"]
sizes=["Small", "Medium", "Large"]

###########################################################################################################################################################################
"""
Colour correspondance
Black = Black
White = White
Grey = Grey94
Dark Grey = Grey40
Light Blue = Cornflower Blue
Blue = Medium Blue
Dark Blue = Navy
Red = FireBrick2
Purple = Dark Orchid
Yellow = Yellow
Light Green = Lime Green
Dark Green = Dark Green
Neutral = Burlywood1
"""
###########################################################################################################################################################################
def BackgroundSet():
    global bgColour
    global bgSetting
    global errorColour
    global buttonSetting
        
    if bgColour == "Black":
        bgSetting = "Black"
        buttonSetting = "Grey30"
        errorColour = "Orange Red"
        
    elif bgColour == "White":
        bgSetting = "Snow"
        buttonSetting = "Grey80"
        errorColour = errorColour
        
    elif bgColour == "Grey":
        bgSetting = "Grey94"
        buttonSetting = "DarkGrey"
        errorColour = errorColour
        
    elif bgColour == "Dark Grey":
        bgSetting = "Grey40"
        buttonSetting = "Grey80"
        errorColour = "White"
        
    elif bgColour == "Light Blue":
        bgSetting = "Cornflower Blue"
        buttonSetting = "Navy"
        errorColour = errorColour
        
    elif bgColour == "Blue":
        bgSetting = "Medium Blue"
        buttonSetting = "Navy"
        errorColour = "Orange Red"
        
    elif bgColour == "Dark Blue":
        bgSetting = "Navy"
        buttonSetting = "Cornflower Blue"
        errorColour = errorColour
        
    elif bgColour == "Red":
        bgSetting = "FireBrick2"
        buttonSetting = "FireBrick4"
        errorColour = "Black"
        
    elif bgColour == "Purple":
        bgSetting = "Dark Orchid"
        buttonSetting = "MediumOrchid4"
        errorColour = "Grey99"
        
    elif bgColour == "Yellow":
        bgSetting = "Yellow"
        buttonSetting = "Goldenrod3"
        errorColour = errorColour
        
    elif bgColour == "Light Green":
        bgSetting = "Lime Green"
        buttonSetting = "Dark Green"
        errorColour = "OrangeRed4"
        
    elif bgColour == "Dark Green":
        bgSetting = "Dark Green"
        buttonSetting = "Lime Green"
        errorColour = "Orange Red"
        
    elif bgColour == "Neutral":
        bgSetting = "Burlywood1"
        buttonSetting = "Burlywood4"
        errorColour = "Black"
    else:
        bgColour = bgColour

def FontSet():
    global fontColour
    global fontSetting

    if fontColour == "Black":
        fontSetting = "Black"
        
    elif fontColour == "White":
        fontSetting = "Snow"
        
    elif fontColour == "Light Blue":
        fontSetting = "Cornflower Blue"
        
    elif fontColour == "Blue":
        fontSetting = "Medium Blue"
        
    elif fontColour == "Dark Blue":
        fontSetting = "Navy"
        
    elif fontColour == "Red":
        fontSetting = "FireBrick2"
        
    elif fontColour == "Purple":
        fontSetting = "Dark Orchid"
        
    elif fontColour == "Yellow":
        fontSetting = "Yellow"
        
    elif fontColour == "Light Green":
        fontSetting = "Lawn Green"
        
    elif fontColour == "Dark Green":
        fontSetting = "Dark Green"

    else:
        fontColour = fontColour


def FontSize():
    global fontSize
    global titleSize
    global fontSet
    global buttonFont
        
    if fontSize == "Small":
        titleSize = 24
        fontSet = 16
        buttonFont = 16
    elif fontSize == "Medium":
        titleSize = 36
        fontSet = 18
        buttonFont = 24
    elif fontSize == "Large":
        titleSize = 36
        fontSet = 26
        buttonFont = 36
    else:
        fontSize = fontSize


def ButtonSize():
    global buttonSize
    global fontSize
    global height
    
    if buttonSize == "Small":
        if fontSize == "Small":
            height = 2
        elif fontSize == "Medium":
            height = 1
        else:
            height = 1
            
    elif buttonSize == "Medium":
        if fontSize == "Small":
            height = 3
        elif fontSize == "Medium":
            height = 2
        else:
            height = 1
            
    elif buttonSize == "Large":
        if fontSize == "Small":
            height = 3
        elif fontSize == "Medium":
            height = 2
        else:
            height = 1
            
    else:
        buttonSize = buttonSize
    


def SelectionMenu():
    
    def MainMenu():
        global fontSize
        global buttonSize
        global fontColour
        global bgColour
        global bgSetting
        global fontSetting
        global errorColour
        global titleSize
        global fontSet
        global height
        global width
        global buttonSetting
        global buttonFont

        BackgroundSet()
        FontSet()
        FontSize()
        ButtonSize()
        

#Sorting Button Widths
        if buttonSize == "Small":
            width = 20     
        elif buttonSize == "Medium":
            width = 25       
        elif buttonSize == "Large":
            width = 30     
        else:
            buttonSize = buttonSize

        
        Menu = tk.Tk()
        Menu.configure()
        Menu.attributes("-fullscreen", True)
        Menu['bg']=bgSetting

        global screenWidth
        screenWidth = Menu.winfo_screenwidth()
        global screenHeight
        screenHeight = Menu.winfo_screenheight()

        xPos1 = screenWidth * 0.06
        xPos2 = screenWidth * 0.55
        yPos1 = screenHeight * 0.2
        yPos2 = screenHeight * 0.35
        yPos3 = screenHeight * 0.5
        yPos4 = screenHeight * 0.65
        yPos5 = screenHeight * 0.8

#Sorting Button Positions
        if fontSize == "Small":
            buttonY1=yPos1
            buttonY2=yPos2
            buttonY3=yPos3
            buttonY4=yPos4
            buttonY5=yPos5
            if buttonSize == "Small":
                buttonY1=buttonY1+60
                buttonY2=buttonY2+30
                buttonY3=buttonY3
                buttonY4=buttonY4-30
                buttonY5=buttonY5-60
            elif buttonSize == "Medium":
                buttonY1=buttonY1+20
                buttonY2=buttonY2+10
                buttonY3=buttonY3
                buttonY4=buttonY4-10
                buttonY5=buttonY5-20
            else:
                buttonY1=buttonY1-20
                buttonY2=buttonY2-15
                buttonY3=buttonY3-10
                buttonY4=buttonY4-5
                buttonY5=buttonY5
                
        elif fontSize == "Medium":
            buttonY1=yPos1+30
            buttonY2=yPos2+30
            buttonY3=yPos3+30
            buttonY4=yPos4+30
            buttonY5=yPos5+30
            if buttonSize == "Small":
                buttonY1=buttonY1+60
                buttonY2=buttonY2+30
                buttonY3=buttonY3
                buttonY4=buttonY4-30
                buttonY5=buttonY5-60
            elif buttonSize == "Medium":
                buttonY1=buttonY1
                buttonY2=buttonY2
                buttonY3=buttonY3
                buttonY4=buttonY4
                buttonY5=buttonY5
            else:
                buttonY1=buttonY1
                buttonY2=buttonY2
                buttonY3=buttonY3
                buttonY4=buttonY4
                buttonY5=buttonY5
                
        elif fontSize == "Large":
            buttonY1=yPos1+50
            buttonY2=yPos2+50
            buttonY3=yPos3+50
            buttonY4=yPos4+50
            buttonY5=yPos5+50
            if buttonSize == "Small":
                buttonY1=buttonY1+20
                buttonY2=buttonY2+10
                buttonY3=buttonY3
                buttonY4=buttonY4-10
                buttonY5=buttonY5-20
            elif buttonSize == "Medium":
                buttonY1=buttonY1+20
                buttonY2=buttonY2+10
                buttonY3=buttonY3
                buttonY4=buttonY4-10
                buttonY5=buttonY5-20
            else:
                buttonY1=buttonY1+20
                buttonY2=buttonY2+10
                buttonY3=buttonY3
                buttonY4=buttonY4-10
                buttonY5=buttonY5-20
                
        else:
            fontSize = fontSize

        Space()
        Title = tk.Label(Menu, text="Projectile Motion and Collision Simulator")
        Title['font'] = font.Font(family='Fixedsys', size=titleSize, weight='bold')
        Title['background'] = bgSetting
        Title['foreground'] = fontSetting
        Title.pack()
        Space()

        Heading = tk.Label(Menu, text="What would you like to do?")
        Heading['font'] = font.Font(family='Fixedsys', size=fontSet, weight='bold')
        Heading['background'] = bgSetting
        Heading['foreground'] = fontSetting
        Heading.pack()

        def MenuToVectors(event):
            Menu.destroy()
            print("VectorCalculations()")

        def MenuToProjectileMotion(event):
            Menu.destroy()
            print("ProjectileMotion()")

        def MenuToCollisions(event):
            Menu.destroy()
            print("Collisions()")

        def MenuToSettings(event):
            Menu.destroy()
            Settings()

        def LogOut(event):
            Menu.destroy()
            print("LoginSystem()")

        VectorClick = tk.Button(Menu, text="3-D Vectors", fg=fontSetting, bg=buttonSetting, height=height, width=width)
        VectorClick['font'] = font.Font(size=buttonFont)
        vectorWidth = VectorClick.winfo_reqwidth()
        VectorClick.place(x=((screenWidth/2)-(vectorWidth/2)), y=buttonY1)
        VectorClick.bind("<Button-1>",MenuToVectors)

        ProjectileMotionClick = tk.Button(Menu, text="Projectile Motion", fg=fontSetting, bg=buttonSetting, height=height, width=width)
        ProjectileMotionClick['font'] = font.Font(size=buttonFont)
        projectileWidth = ProjectileMotionClick.winfo_reqwidth()
        ProjectileMotionClick.place(x=((screenWidth/2)-(projectileWidth/2)), y=buttonY2)
        ProjectileMotionClick.bind("<Button-1>",MenuToProjectileMotion)

        CollisionClick = tk.Button(Menu, text="Collsions", fg=fontSetting, bg=buttonSetting, height=height, width=width)
        CollisionClick['font'] = font.Font(size=buttonFont)
        collisionWidth = CollisionClick.winfo_reqwidth()
        CollisionClick.place(x=((screenWidth/2)-(collisionWidth/2)), y=buttonY3)
        CollisionClick.bind("<Button-1>",MenuToCollisions)

        SettingsClick = tk.Button(Menu, text="Settings", fg=fontSetting, bg=buttonSetting, height=height, width=width)
        SettingsClick['font'] = font.Font(size=buttonFont)
        settingsWidth = SettingsClick.winfo_reqwidth()
        SettingsClick.place(x=((screenWidth/2)-(settingsWidth/2)), y=buttonY4)
        SettingsClick.bind("<Button-1>",MenuToSettings)

        LogOutClick = tk.Button(Menu, text="Log Out", fg=fontSetting, bg=buttonSetting, height=height, width=width)
        LogOutClick['font'] = font.Font(size=buttonFont)
        logoutWidth = LogOutClick.winfo_reqwidth()
        LogOutClick.place(x=((screenWidth/2)-(logoutWidth/2)), y=buttonY5)
        LogOutClick.bind("<Button-1>",LogOut)

    def Settings():

        global fontSize
        global buttonSize
        global fontColour
        global bgColour
        global bgSetting
        global errorColour
        global titleSize
        global fontSet
        global height
        global width
        global buttonSetting
        global buttonFont
        
        global sizes
        global fontColours
        global bgColours
        
        global check
        global check2
        global check3
        global check4

        check = 0
        check2 = 0
        check3 = 0
        check4 = 0

        if fontSize == "Small":
            add = 30
            boxWidth = 30
        elif fontSize == "Medium":
            add = 50
            boxWidth = 40
        elif fontSize == "Large":
            add = 60
            boxWidth = 50
        else:
            fontSize = fontSize

            

        Setting = tk.Tk()
        Setting.configure()
        Setting.attributes("-fullscreen", True)
        Setting['bg']=bgSetting

        Space()
        Title = tk.Label(Setting, text="Settings")
        Title['font'] = font.Font(family='Fixedsys', size=titleSize, weight='bold')
        Title['background'] = bgSetting
        Title['foreground'] = fontSetting
        Title.pack()
        Space()
        

        global screenWidth
        global screenHeight

        xPos1 = screenWidth * 0.17
        xPos2 = screenWidth * 0.55
        yPos1 = screenHeight * 0.2
        yPos2 = screenHeight * 0.35
        yPos3 = screenHeight * 0.5
        yPos4 = screenHeight * 0.65
        yPos5 = screenHeight * 0.8
        yPos3_5 = yPos3+((yPos4-yPos3)/2)

        def BackToMenu(event):
            Setting.destroy()
            MainMenu()

        backArrow = PhotoImage(file = r"E:\Computer Science Programming Project\Images\BackArrow.png")
        backArrowSized = backArrow.subsample(6,6)
        BackButton = tk.Button(Setting, bg=buttonSetting, image=backArrowSized, fg=fontSetting)
        BackButton.image=backArrowSized
        BackButton.place(x=screenHeight*0.06, y=screenHeight*0.06)
        BackButton.bind("<Button-1>",BackToMenu)

        FontSizeLabel = tk.Label(Setting, text="Font Size:", bg=bgSetting, fg=fontSetting)
        FontSizeLabel['font'] = font.Font(family='Fixedsys', size=fontSet)
        FontSizeLabel.place(x=xPos1, y=yPos2)

        w = -1
        count = 0
        for i in sizes:
            i = str(i)
            i = i.strip("('")
            i = i.strip("',)")
            if i == fontSize:
                w = count
                count = count + 1
            else:
                count = count + 1

        InitialFont = tk.StringVar(Setting)
        InitialFont.set(sizes[w])
        FontSize = ttk.Combobox(Setting, justify="center", width=boxWidth, textvariable=InitialFont, state="readonly")
        FontSize['values']=sizes
        FontSize.configure(foreground="Gray")
        FontSize.place(x=xPos1, y=yPos2+add, height=40)

        def ConfigFont(event):
            global check
            if check == 0:
                FontSize.config(foreground="black")
                check = 1
            else:
                check = check

        FontSize.bind("<Button-1>",ConfigFont)
        FontSize.bind("<FocusIn>",ConfigFont)



        ButtonSizeLabel = tk.Label(Setting, text="Button Size:", bg=bgSetting, fg=fontSetting)
        ButtonSizeLabel['font'] = font.Font(family='Fixedsys', size=fontSet)
        ButtonSizeLabel.place(x=xPos2, y=yPos2)

        x = -1
        count2 = 0
        for i in sizes:
            i = str(i)
            i = i.strip("('")
            i = i.strip("',)")
            if i == buttonSize:
                x = count2
                count2 = count2 + 1
            else:
                count2 = count2 + 1

        InitialButton = tk.StringVar(Setting)
        InitialButton.set(sizes[x])
        ButtonSize = ttk.Combobox(Setting, justify="center", width=boxWidth, textvariable=InitialButton, state="readonly")
        ButtonSize['values']=sizes
        ButtonSize.configure(foreground="Gray")
        ButtonSize.place(x=xPos2, y=yPos2+add, height=40)

        def ConfigButton(event):
            global check2
            if check2 == 0:
                ButtonSize.config(foreground="black")
                check2 = 1
            else:
                check2 = check2

        ButtonSize.bind("<Button-1>",ConfigButton)
        ButtonSize.bind("<FocusIn>",ConfigButton)



        FontColourLabel = tk.Label(Setting, text="Font Colour:", bg=bgSetting, fg=fontSetting)
        FontColourLabel['font'] = font.Font(family='Fixedsys', size=fontSet)
        FontColourLabel.place(x=xPos1, y=yPos3_5)

        y = -1
        count3 = 0
        for i in fontColours:
            i = str(i)
            i = i.strip("('")
            i = i.strip("',)")
            if i == fontColour:
                y = count3
                count3 = count3 + 1
            else:
                count3 = count3 + 1

        InitialColour = tk.StringVar(Setting)
        InitialColour.set(fontColours[y])
        FontColour = ttk.Combobox(Setting, justify="center", width=boxWidth, textvariable=InitialColour, state="readonly")
        FontColour['values']=fontColours
        FontColour.configure(foreground="Gray")
        FontColour.place(x=xPos1, y=yPos3_5+add, height=40)

        def ConfigColour(event):
            global check3
            if check3 == 0:
                FontColour.config(foreground="black")
                check3 = 1
            else:
                check3 = check3

        FontColour.bind("<Button-1>",ConfigColour)
        FontColour.bind("<FocusIn>",ConfigColour)

        

        BGColourLabel = tk.Label(Setting, text="Background Colour:", bg=bgSetting, fg=fontSetting)
        BGColourLabel['font'] = font.Font(family='Fixedsys', size=fontSet)
        BGColourLabel.place(x=xPos2, y=yPos3_5)

        z = -1
        count4 = 0
        for i in bgColours:
            i = str(i)
            i = i.strip("('")
            i = i.strip("',)")
            if i == bgColour:
                z = count4
                count4 = count4 + 1
            else:
                count4 = count4 + 1

        InitialBG = tk.StringVar(Setting)
        InitialBG.set(bgColours[z])
        BGColour = ttk.Combobox(Setting, justify="center", width=boxWidth, textvariable=InitialBG, state="readonly")
        BGColour['values']=bgColours
        BGColour.configure(foreground="Gray")
        BGColour.place(x=xPos2, y=yPos3_5+add, height=40)

        def ConfigBG(event):
            global check4
            if check4 == 0:
                BGColour.config(foreground="black")
                check4 = 1
            else:
                check4 = check4

        BGColour.bind("<Button-1>",ConfigBG)
        BGColour.bind("<FocusIn>",ConfigBG)

        def SaveAndExit(event):
            global fontSize
            global buttonSize
            global fontColour
            global bgColour
            
            newFontSize = FontSize.get()
            newButtonSize = ButtonSize.get()
            newFontColour = FontColour.get()
            newBGColour = BGColour.get()

            fontSize = newFontSize
            buttonSize = newButtonSize
            fontColour = newFontColour
            bgColour = newBGColour
            Setting.destroy()
            MainMenu()

        SaveButton = tk.Button(Setting, text="Save and Exit", height=height, bg=buttonSetting, fg=fontSetting)
        SaveButton['font'] = font.Font(size=buttonFont)
        saveWidth = SaveButton.winfo_reqwidth()
        SaveButton.place(x=((screenWidth/2)-(saveWidth/2)), y=yPos5)
        SaveButton.bind("<Button-1>",SaveAndExit)

        Error.pack()
        
        
    MainMenu()
    
SelectionMenu()
