import customtkinter
from googletrans import LANGUAGES, Translator


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('880x480')
        self.title('Google Translation')
        self.maxsize(880, 480)
        
        # self.set_appearance_mode('System')
        # self.set_default_color_theme('blue')

        # APP TITLE 
        self.title = customtkinter.CTkLabel(
            master = self,
            text = 'Google Translation',
            font = ('Arial', 24),
        )
        self.title.grid(
            padx = 10,
            pady = 10,
            row = 0,
            columnspan = 2
        )

        # USER INPUT TEXT 
        self.user_text = customtkinter.CTkTextbox(
            master = self,
            width = 400,
            height = 350,
            font = ('Arial', 20)
        )
        self.user_text.grid(
            padx = 10,
            pady = 10,
            ipadx = 10,
            ipady = 10,
            row = 1,
            column = 0
        )


        # TRANSLATED OUTPUT TEXT 
        self.translated_text_box = customtkinter.CTkTextbox(
            master = self,
            width = 400,
            height = 350,
            font = ('Arial', 20)
        )

        self.translated_text_box.grid(
            padx = 10,
            pady = 10,
            ipadx = 10,
            ipady = 10,
            row = 1,
            column = 1
        )


        # DESTINATION LANGUAGE MENU 
        language = list(LANGUAGES.values())
        self.lang_menu = customtkinter.CTkOptionMenu(
            master = self,
            values = language,
            font = ('Arial', 12)
        )

        self.lang_menu.grid(
            padx = 10,
            pady = 10,
            row = 2,
            column = 0,
            sticky = 'ew'
        )
        self.lang_menu.set('Choose Language')

        # BUTTON TO TRANSLATE THE TEXT 
        self.translate_button = customtkinter.CTkButton(
            master = self,
            text = 'Translate',
            font = ('Arial', 12),
            command = self.Translate
        )

        self.translate_button.grid(
            padx = 10,
            pady = 10,
            row = 2,
            column = 1,
            sticky = 'ew'
        )

    # TRANSLATE USER TEXT AND DISPLAY ON TEXT BOX 
    def Translate(self):
        self.translator = Translator()
        self.translated_text = self.translator.translate(
            self.user_text.get(index1 = 0.0, index2 = 'end'),
            dest = self.lang_menu.get()
        )

        self.translated_text_box.delete(0.0, 'end')
        self.translated_text_box.insert(0.0, self.translated_text.text)


if __name__ == '__main__':
    app = App()
    app.mainloop()