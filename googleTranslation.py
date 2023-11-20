import tkinter as tk
import customtkinter
from tkinter import ttk
from googletrans import LANGUAGES, Translator


def Translate():
    translator = Translator()
    translated = translator.translate(text_.get(), dest= lang_menu.get())
    translate_text.delete(0.0, 'end')
    translate_text.insert(0.0, translated.text)
    translate_text.pack(padx = 10, pady = 10)

# SYSTEM SETTINGS
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')


# OUR APP FRAME
app = customtkinter.CTk()
app.geometry('780x480')
app.title('Google Translation')

# ADDING UI ELEMENTS
title = customtkinter.CTkLabel(app, text = 'Google Translation', font = ('Arial', 24))
title.pack(padx = 10, pady = 10)

# SELECT DESTINATION LANGUAGE
lang_var = tk.StringVar() 
langauges = list(LANGUAGES.values())
lang_menu = customtkinter.CTkOptionMenu(
    app,
    width = 30, 
    corner_radius = 3, 
    values = langauges,
    variable = lang_var,
    
    )
lang_menu.pack(padx = 10, pady = 10)


# TEXT INPUT
text_var = tk.StringVar()
text_ = customtkinter.CTkEntry(app, width = 350,  height = 60, textvariable = text_var)
text_.pack(padx = 10, pady = 10)

# TRANSLATE BUTTON
translate = customtkinter.CTkButton(app, text = 'Translate', command = Translate)
translate.pack(padx = 10, pady = 10)

# DISPLAY TRANSLATED TEXT
translate_text = customtkinter.CTkTextbox(app, width= 350, height= 60,  corner_radius=5)
# translate_text.pack(padx = 10, pady = 10)




app.mainloop()
