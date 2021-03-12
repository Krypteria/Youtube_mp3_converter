import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter import Menu
import youtube_dl
import ffmpeg
import os

WIDTH = 725
HEIGHT = 110

# Configuración de la pantalla
# --------------------------------------------------------------------------
root = tk.Tk()
root.title("Conversor Youtube - MP3")
root.config(width=WIDTH, height=HEIGHT)
root.resizable(False, False)

SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()
x_coord = int((SCREEN_WIDTH/2) - (WIDTH/2))
y_coord = int((SCREEN_HEIGHT/2) - (HEIGHT/2))
root.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, x_coord, y_coord))

# Formato de conversión
# --------------------------------------------------------------------------
formato = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

# Etiquetas 
# --------------------------------------------------------------------------
fuente = ('Helvetica', 10, 'bold')

etiquetaTitulo = tk.Label(root, text="Video a convertir: ",  font=fuente)
etiquetaTitulo.place(x = 17, y = 10)

etiquetaEstado = tk.Label(root, text="Estado de la conversión: ", font=fuente)
etiquetaEstado.place(x = 17, y = 70)

# Input 
# --------------------------------------------------------------------------
imagenCambiarRuta = tk.PhotoImage(file = "icons\cambiarRuta.png") #cambiar
RUTA = ""

#Cuadro de texto
entrada = ttk.Entry(root, width=90)
entrada.place(x=20, y=40)

#Etiqueta de estado
estado = tk.StringVar()
estadoContenedor = tk.Label(root, textvariable=estado,  font=fuente)
estadoContenedor.place(x = 190, y = 70)

#Botones
def convertir():
    if(RUTA == ""):
        tk.messagebox.showinfo("Error", "Tienes que seleccionar una carpeta de destino")
    else:
        estado.set("En curso")
        root.update()
        with youtube_dl.YoutubeDL(formato) as ydl:
            os.chdir(RUTA)
            ydl.download([entrada.get()])
            entrada.delete(0, "end")
            estado.set("Completada")


convertirBoton = ttk.Button(root, text="Convertir", command = convertir)
convertirBoton.place(x=575, y=38)

def obtenerPath():
    global RUTA
    rutaTemp = tk.filedialog.askdirectory()
    RUTA = rutaTemp

cambiarRutaBoton = ttk.Button(root, image=imagenCambiarRuta, command = obtenerPath)
cambiarRutaBoton.place(x=660, y=31)

#Menu
menuRaton = Menu(root, tearoff=False)
menuRaton.add_command(label="Pegar")

def mostrarMenu(e):
    w = e.widget
    menuRaton.entryconfigure("Pegar", command = lambda: w.event_generate("<<Paste>>"))
    menuRaton.tk_popup(e.x_root, e.y_root)

root.bind("<Button-3>", mostrarMenu)

# --------------------------------------------------------------------------

def main():
    root.mainloop()

if __name__ == "__main__":
    main()