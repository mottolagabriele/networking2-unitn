import tkinter as tk
import subprocess

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Apri xterm esterno")
        self.master.geometry("200x100")

        self.create_widgets()

    def create_widgets(self):
        self.open_terminal_button = tk.Button(self.master, text="Apri xterm", command=self.open_xterm)
        self.open_terminal_button.pack(pady=20)

    def open_xterm(self):
        command = "ls"  # Comando da eseguire nel terminale all'avvio

        # Avvia xterm come processo esterno e passa il comando
        subprocess.Popen(["xterm", "-hold", "-e", "bash", "-c", f"{command}; exec bash"])

root = tk.Tk()
app = Application(master=root)
app.mainloop()
