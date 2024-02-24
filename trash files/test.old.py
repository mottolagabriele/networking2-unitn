import tkinter as tk

class Picture:
    def __init__(self, img_path, name, ip):
        self.img_path = img_path
        self.name = name
        self.ip = ip

class NetworkDrawer:
    def __init__(self, root):
        self.root = root
        self.root.title("Rete")

        # Creazione del canvas
        self.canvas = tk.Canvas(self.root, width=1000, height=800, bg='white')
        self.canvas.pack()

        # Dizionario per tenere traccia delle immagini
        self.images = {}

        # Dizionario per tenere traccia dei collegamenti e dei loro colori
        self.connections = {}

    def load_images(self):
        # Caricamento delle immagini
        self.images['switch'] = tk.PhotoImage(file="switch.png").subsample(12)
        self.images['host'] = tk.PhotoImage(file="host.png").subsample(12)
        self.images['server'] = tk.PhotoImage(file="server.png").subsample(12)

    def draw_node(self, x, y, picture):
        self.canvas.create_image(x, y, anchor=tk.NW, image=self.images[picture.img_path])
        self.canvas.create_text(x + 20, y + 50, text=picture.name)
        self.canvas.create_text(x + 20, y + 75, text=picture.ip)

    def draw_connection(self, start_x, start_y, end_x, end_y, color='black'):
        connection_id = self.canvas.create_line(start_x, start_y, end_x, end_y, fill=color, width=3)
        return connection_id

    def draw_network(self):
        self.load_images()

        # Lista di immagini con nome host e IP
        p_h0 =  Picture("host", "h0", "192.168.1.1")
        p_h1 =  Picture("host", "h1", "192.168.1.1")
        p_h2 =  Picture("host", "h2", "192.168.1.2")
        p_h3 =  Picture("host", "h3", "192.168.1.3")
        p_h4 =  Picture("host", "h4", "192.168.1.4")
        p_h5 =  Picture("host", "h5", "192.168.1.5")
        p_h6 =  Picture("host", "h6", "192.168.1.6")
        p_s0 =  Picture("server", "s0", "192.168.1.7")
        p_s1 =  Picture("server", "s1", "192.168.1.7")
        p_s2 =  Picture("server", "s2", "192.168.1.8")
        p_s3 =  Picture("server", "s3", "192.168.1.9")
        p_s4 =  Picture("server", "s4", "192.168.1.10")

        # Definizione degli switch
        p_sw0 = Picture("switch", "sw0", "")
        p_sw1 = Picture("switch", "sw1", "")
        p_sw2 = Picture("switch", "sw2", "")
        p_sw3 = Picture("switch", "sw3", "")
        p_sw4 = Picture("switch", "sw4", "")
        p_sw5 = Picture("switch", "sw5", "")
        p_sw6 = Picture("switch", "sw6", "")

        # Disegno della rete
        offset_x = 200
        self.draw_node(offset_x + 300, 300, p_sw0)    # sw0
        self.draw_node(offset_x + 200, 300, p_sw1)    # sw1
        self.draw_node(offset_x + 400, 300, p_sw2)    # sw2
        self.draw_node(offset_x + 100, 200, p_sw3)    # sw3
        self.draw_node(offset_x + 100, 400, p_sw4)    # sw4
        self.draw_node(offset_x + 500, 200, p_sw5)    # sw5
        self.draw_node(offset_x + 500, 400, p_sw6)    # sw6

        self.draw_node(offset_x-100, 100, p_h1)    # h1
        self.draw_node(offset_x-100, 200, p_h2)    # h2
        self.draw_node(offset_x-100, 300, p_h3)    # h3

        self.draw_node(offset_x-100, 400, p_s1)    # s1
        self.draw_node(offset_x-100, 500, p_s2)    # s2

        self.draw_node(offset_x+700, 100, p_h4)    # h4
        self.draw_node(offset_x+700, 200, p_h5)    # h5
        self.draw_node(offset_x+700, 300, p_h6)    # h6

        self.draw_node(offset_x+700 , 400, p_s3)    # s3
        self.draw_node(offset_x+700 , 500, p_s4)    # s4

        self.draw_node(offset_x + 200, 500, p_h0)    # h0
        self.draw_node(offset_x + 400, 500, p_s0)    # s0

        # Creazione dei collegamenti
        self.connections['sw0_sw1'] = self.draw_connection(offset_x + 300, 300, offset_x + 200, 300)  # sw0 -> sw1
        self.connections['sw0_sw2'] = self.draw_connection(offset_x + 300, 300, offset_x + 400, 300)  # sw0 -> sw2
        self.connections['sw0_s0'] = self.draw_connection(offset_x + 300, 300, offset_x + 200, 500)  # sw0 -> s0
        self.connections['sw0_h1'] = self.draw_connection(offset_x + 300, 300, offset_x - 100, 100)  # sw0 -> h1

        self.connections['sw1_sw3'] = self.draw_connection(offset_x + 200, 300, offset_x + 100, 200)  # sw1 -> sw3
        self.connections['sw1_sw4'] = self.draw_connection(offset_x + 200, 300, offset_x + 100, 400)  # sw1 -> sw4

        self.connections['sw2_sw5'] = self.draw_connection(offset_x + 400, 300, offset_x + 500, 200)  # sw2 -> sw5
        self.connections['sw2_sw6'] = self.draw_connection(offset_x + 400, 300, offset_x + 500, 400)  # sw2 -> sw6

        self.connections['sw3_h2'] = self.draw_connection(offset_x + 100, 200, offset_x - 100, 100)  # sw3 -> h2
        self.connections['sw3_h3'] = self.draw_connection(offset_x + 100, 200, offset_x - 100, 200)  # sw3 -> h3
        self.connections['sw3_h4'] = self.draw_connection(offset_x + 100, 200, offset_x - 100, 300)  # sw3 -> h4

        self.connections['sw4_s1'] = self.draw_connection(offset_x + 100, 400, offset_x - 100, 400)  # sw4 -> s1
        self.connections['sw4_s2'] = self.draw_connection(offset_x + 100, 400, offset_x - 100, 500)  # sw4 -> s2

        self.connections['sw5_h4'] = self.draw_connection(offset_x + 500, 200, offset_x + 700, 200)  # sw5 -> h4
        self.connections['sw5_h5'] = self.draw_connection(offset_x + 500, 200, offset_x + 700, 300)  # sw5 -> h5
        self.connections['sw5_h6'] = self.draw_connection(offset_x + 500, 200, offset_x + 700, 400)  # sw5 -> h6

        self.connections['sw6_s3'] = self.draw_connection(offset_x + 500, 400, offset_x + 700, 400)  # sw6 -> s3
        self.connections['sw6_s4'] = self.draw_connection(offset_x + 500, 400, offset_x + 700, 500)  # sw6 -> s4

    def move_network(self, dx, dy):
        # Sposta tutti gli elementi della rete
        for element in self.canvas.find_all():
            self.canvas.move(element, dx, dy)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkDrawer(root)
    app.draw_network()  # Disegna la rete
    app.move_network(50, 50)  # Sposta la rete di 50 pixel verso il basso e verso destra
    app.run()
