import tkinter as tk
import customtkinter
from tkinter import ttk
from googletrans import LANGUAGES, Translator

# # LANGUAGE TRANSLATION FUNCTION 
def Translate():
    translator = Translator()
    translated_text = translator.translate(user_text.get(index1= 0.0, index2='end'), dest= lang_menu.get())
    
    translated_text_box.delete(0.0, 'end')
    translated_text_box.insert(0.0, translated_text.text)

# SYSTEM SETTINGS
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

# OUR APP FRAME
app = customtkinter.CTk()
app.geometry('880x480')
app.title('Google Translation')

# THE APP TITLE
title = customtkinter.CTkLabel(app, text = 'Google Translation', font = ('Arial', 24))
title.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)

# TEXT INPUT
user_text = customtkinter.CTkTextbox(
    app,
    width = 400,  height = 350,
    font = ('Arial', 20),
    )
user_text.grid(row = 1, column = 0, padx = 10, pady = 10)

# DISPLAY TRANSLATED TEXT
translated_text_box = customtkinter.CTkTextbox(
    app, width= 400, height= 350,  corner_radius=5,
    font = ('Arial', 20)

    )
translated_text_box.grid(row = 1, column = 1, padx = 10, pady = 10)

# SELECT DESTINATION LANGUAGE
lang_var = tk.StringVar() 
langauges = list(LANGUAGES.values())
lang_menu = customtkinter.CTkOptionMenu(
    app,
    width = 30, 
    corner_radius = 3, 
    values = langauges,
    variable = lang_var,
    font = ('Arial', 12)

    )
lang_menu.grid(row = 2, column = 0, padx = 10, pady = 10, ipadx = 2, ipady = 2)
lang_menu.set('Choose Language')
# TRANSLATE BUTTON
translate_button = customtkinter.CTkButton(
    app, text = 'Translate', command = Translate,
    font= ('Arial', 14)
    )
translate_button.grid(row = 2, column = 1, padx = 10, pady = 10)

app.mainloop()
