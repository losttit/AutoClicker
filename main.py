import customtkinter as CTk
import mouse
import keyboard
from plyer import notification


class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("220x190")
        self.title("Autoclicker")
        self.resizable(False, False)

        self.choose_frame = CTk.CTkFrame(master=self, fg_color="transparent")
        self.choose_frame.grid(row=1, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.choose_char = CTk.CTkEntry(master=self.choose_frame, width=180, placeholder_text="Choose button")
        self.choose_char.grid(row=1, column=0, padx=(0, 20), pady=(0, 10))

        self.choose_freq = CTk.CTkEntry(master=self.choose_frame, width=180,
                                        placeholder_text="Choose frequency msec")
        self.choose_freq.grid(row=2, column=0, padx=(0, 20), pady=(0, 10))

        self.btn_select = CTk.CTkButton(master=self.choose_frame, text="Select", width=180,
                                      command=self.start_autoclicker)
        self.btn_select.grid(row=3, column=0, padx=(0, 20))

        self.text = CTk.CTkLabel(master=self, text="")
        self.text.grid(row=4, column=0, padx=(0, 20))

        self.isClicking = False
        self.frq = 0

    def clicker(self):
        if self.isClicking:
            mouse.double_click(button="left")
        self.after(self.frq, self.clicker)

    def set_clicker(self):
        self.isClicking = not self.isClicking
        if self.isClicking:
            self.show("Autoclicker", "is running")
        else:
            self.show("Autoclicker", "is turned off")

    def start_autoclicker(self):
        btn = self.choose_char.get()
        frq = int(self.choose_freq.get())
        self.choose_char.configure(state="disabled")
        self.choose_freq.configure(state="disabled")
        self.btn_select.configure(state="disabled")
        keyboard.add_hotkey(btn, self.set_clicker)
        self.frq = frq
        output = ("You've chosen Button: " + btn + "\nand Frequency: " + str(frq))
        self.text.configure(text=output)
        self.clicker()

    @staticmethod
    def show(title, message):
        notification.notify(title=title, message=message, app_icon="aim.ico", timeout=1)


if __name__ == "__main__":
    app = App()
    app.mainloop()

