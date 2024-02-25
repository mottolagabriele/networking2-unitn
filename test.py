import tkinter as tk
import subprocess
import threading
import NetworkDrawer


class NetworkApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Progetto di Networking 2")
        self.geometry("2000x1400")

        self.configure(bg="#f0f0f0")

        self.frame_top = tk.Frame(self, bg="#f0f0f0")
        self.frame_top.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        self.image_path = "network_image.png"  # Percorso dell'immagine della rete
        self.load_network()

        self.start_button = tk.Button(self.frame_top, text="START", bg="#007bff", fg="white", relief=tk.FLAT, command=self.on_start_button_clicked)
        self.start_button.pack(fill=tk.X, pady=5)

        self.stop_button = tk.Button(self.frame_top, text="STOP", bg="#007bff", fg="white", relief=tk.FLAT, command=self.on_stop_button_clicked, state=tk.DISABLED)
        self.stop_button.pack(fill=tk.X, pady=5)
        
        self.normal_state_button = tk.Button(self.frame_top, text="NORMAL STATE", bg="#007bff", fg="white", relief=tk.FLAT, command=self.on_normal_state_button_clicked, state=tk.DISABLED)
        self.normal_state_button.pack(fill=tk.X, pady=5)

        self.full_state_button = tk.Button(self.frame_top, text="FULL STATE", bg="#007bff", fg="white", relief=tk.FLAT, command=self.on_full_state_button_clicked, state=tk.DISABLED)
        self.full_state_button.pack(fill=tk.X, pady=5)
        
        self.isolated_state_button = tk.Button(self.frame_top, text="ISOLATED STATE", bg="#007bff", fg="white", relief=tk.FLAT, command=self.on_isolated_state_button_clicked, state=tk.DISABLED)
        self.isolated_state_button.pack(fill=tk.X, pady=5)
        
        self.service_state_button = tk.Button(self.frame_top, text="SERVICE STATE", bg="#007bff", fg="white", relief=tk.FLAT, command=self.on_service_state_button_clicked, state=tk.DISABLED)
        self.service_state_button.pack(fill=tk.X, pady=5)

        self.stop_event = threading.Event()

        self.terminal_output = tk.Text(self.frame_top, bg="black", fg="white", height=10)
        self.terminal_output.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def load_network(self):
        # Crea un frame per la rete
        self.network_frame = tk.Frame(self.frame_top, bg="#f0f0f0")
        self.network_frame.pack(side=tk.LEFT, padx=10)

        # Crea un'istanza di NetworkDrawer per disegnare la rete all'interno del frame della rete
        self.network_drawer = NetworkDrawer.NetworkDrawer(self.network_frame)
        self.network_drawer.draw_network()




    def on_start_button_clicked(self):
        # Disabilita il pulsante START e abilita gli altri
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.service_state_button.config(state=tk.NORMAL)
        self.normal_state_button.config(state=tk.NORMAL)
        self.full_state_button.config(state=tk.NORMAL)
        self.isolated_state_button.config(state=tk.NORMAL)

        # Avvia clear_mininet_topology e start_slicing_scenario
        self.clear_mininet_topology()
        self.start_slicing_scenario()

    def clear_mininet_topology(self):
        # Pulisce la topologia Mininet
        subprocess.run(['bash', 'clear_mininet_topology.sh'])
        self.display_output("Cleared Mininet Topology\n")

    def start_slicing_scenario(self):
        # Avvia start_slicing_scenario in un nuovo terminale
        #subprocess.Popen(['xterm', '-hold', '-e', 'sudo', 'ryu-manager', 'slicing_scenario.py'], stdout=subprocess.PIPE)
        #self.display_output("Started Slicing Scenario\n")

        #command = "ls"  # Comando da eseguire nel terminale all'avvio
        command = "sudo ryu-manager slicing_scenario.py"  # Comando da eseguire nel terminale all'avvio

        # Avvia xterm come processo esterno e passa il comando
        subprocess.Popen(["xterm", "-hold", "-e", "bash", "-c", f"{command}; exec bash"])

    def on_stop_button_clicked(self):
        # Disabilita gli altri pulsanti e abilita START
        self.stop_button.config(state=tk.DISABLED)
        self.open_cli.config(state=tk.DISABLED)
        self.normal_state_button.config(state=tk.DISABLED)
        self.full_state_button.config(state=tk.DISABLED)
        self.isolated_state_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)

        # Termina il processo di slicing e chiude il terminale
        self.stop_slicing_scenario()

        # Pulisce la topologia Mininet
        self.clear_mininet_topology()

    def stop_slicing_scenario(self):
        # Termina il processo di slicing e chiude il terminale
        subprocess.run(['pkill', '-f', 'slicing_scenario.py'])
        self.display_output("Stopped Slicing Scenario\n")

    def on_normal_state_button_clicked(self):
        # Avvia il comune scenario
        process = subprocess.Popen(['bash', 'common_scenario.sh'], stdout=subprocess.PIPE)
        output, _ = process.communicate()
        self.display_output(output.decode("utf-8"))
        self.display_output("Started Normal State Scenario\n")
        self.network_drawer.normale_state()

    def on_full_state_button_clicked(self):
        # Avvia lo scenario full
        process = subprocess.Popen(['bash', 'full_scenario.sh'], stdout=subprocess.PIPE)
        output, _ = process.communicate()
        self.display_output(output.decode("utf-8"))
        self.display_output("Started Full State Scenario\n")
        self.network_drawer.full_state()
    
    def on_isolated_state_button_clicked(self):
        # Avvia lo scenario isolato
        process = subprocess.Popen(['bash', 'isolated_scenario.sh'], stdout=subprocess.PIPE)
        output, _ = process.communicate()
        self.display_output(output.decode("utf-8"))
        self.display_output("Started Isolated State Scenario\n")
        self.network_drawer.isolated_state()
    
    def on_service_state_button_clicked(self):
        # Avvia lo scenario isolato
        process = subprocess.Popen(['bash', 'service_scenario.sh'], stdout=subprocess.PIPE)
        output, _ = process.communicate()
        self.display_output(output.decode("utf-8"))
        self.display_output("Started Service State Scenario\n")
        self.network_drawer.normale_state()

    def display_output(self, text):
        self.terminal_output.insert(tk.END, text)
        self.terminal_output.see(tk.END)

   

if __name__ == "__main__":
    app = NetworkApp()
    app.mainloop()
