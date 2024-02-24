import tkinter as tk
import subprocess
import threading

class NetworkApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Progetto di Networking 2")
        self.geometry("1000x500")

        self.configure(bg="#f0f0f0")

        self.frame_top = tk.Frame(self, bg="#f0f0f0")
        self.frame_top.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        self.image_path = "network_image.png"  # Percorso dell'immagine della rete
        self.load_image()

        self.start_button = tk.Button(self.frame_top, text="START", bg="#007bff", fg="white", relief=tk.FLAT, command=self.on_start_button_clicked)
        self.start_button.pack(fill=tk.X, pady=5)

        self.stop_button = tk.Button(self.frame_top, text="STOP", bg="#007bff", fg="white", relief=tk.FLAT, command=self.on_stop_button_clicked)
        self.stop_button.pack(fill=tk.X, pady=5)

        self.normal_state_button = tk.Button(self.frame_top, text="NORMAL STATE", bg="#007bff", fg="white", relief=tk.FLAT, command=self.on_normal_state_button_clicked)
        self.normal_state_button.pack(fill=tk.X, pady=5)

        self.critical_state_button = tk.Button(self.frame_top, text="CRITICAL STATE", bg="#007bff", fg="white", relief=tk.FLAT, command=self.on_critical_state_button_clicked)
        self.critical_state_button.pack(fill=tk.X, pady=5)

        self.stop_event = threading.Event()

    def load_image(self):
        self.image = tk.PhotoImage(file=self.image_path)
        self.img_label = tk.Label(self.frame_top, image=self.image, bg="#f0f0f0")
        self.img_label.pack(side=tk.LEFT, padx=10)

    def on_start_button_clicked(self):
        # Avvia clear_mininet_topology e start_slicing_scenario
        self.clear_mininet_topology()
        self.start_slicing_scenario()

    def clear_mininet_topology(self):
        # Pulisce la topologia Mininet
        subprocess.run(['bash', 'clear_mininet_topology.sh'])

    def start_slicing_scenario(self):
        # Avvia start_slicing_scenario in un nuovo terminale
        subprocess.Popen(['xterm', '-hold', '-e', 'sudo', 'ryu-manager', 'slicing_scenario.py'])

    def on_stop_button_clicked(self):
        # Imposta il flag per terminare i thread
        self.stop_event.set()

    def on_normal_state_button_clicked(self):
        # Avvia il comune scenario
        subprocess.Popen(['bash', 'common_scenario.sh'])

    def on_critical_state_button_clicked(self):
        # Avvia lo scenario critico
        subprocess.Popen(['bash', 'sos_scenario.sh'])



if __name__ == "__main__":
    app = NetworkApp()
    app.mainloop()
