import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import youtube_dl
import ffmpeg
import os

WIDTH = 725
HEIGHT = 110

root = tk.Tk()
root.title("Conversor de videos a MP3")
root.config(width=WIDTH, height=HEIGHT)
root.resizable(False, False)

SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()

fuente = ('Helvetica', 10, 'bold')

RUTA = ""

formato = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

## ETIQUETAS

etiquetaTitulo = tk.Label(root, text="Video a convertir: ",  font=fuente)
etiquetaTitulo.place(x = 17, y = 10)

etiquetaEstado = tk.Label(root, text="Estado de la conversión: ", font=fuente)
etiquetaEstado.place(x = 17, y = 70)

## CUADROS DE TEXTO

entrada = ttk.Entry(root, width=90)
entrada.place(x=20, y=40)

## VARIABLES
estado = tk.StringVar()
estadoContenedor = tk.Label(root, textvariable=estado,  font=fuente)
estadoContenedor.place(x = 190, y = 70)

## BOTONES

imagenCambiarRuta = tk.PhotoImage(file = "D:\Biblioteca\Escritorio\Workspaces\Workspace Python\Tests\cambiarRuta.png")

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


convertirBotton = ttk.Button(root, text="Convertir", command = convertir)
convertirBotton.place(x=575, y=38)

def obtenerPath():
    global RUTA
    rutaTemp = tk.filedialog.askdirectory()
    RUTA = rutaTemp

cambiarRutaBoton = ttk.Button(root, image=imagenCambiarRuta, command = obtenerPath)
cambiarRutaBoton.place(x=660, y=31)

# entry.config(state=tk.NORMAL)  MIENTRAS NO SE COMPLETE LA DESCARGA NO LE DEJO VOLVER A USARLA

def main():
    x_coord = int((SCREEN_WIDTH/2) - (WIDTH/2))
    y_coord = int((SCREEN_HEIGHT/2) - (HEIGHT/2))
    root.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, x_coord, y_coord))
    root.mainloop()

    url = entrada.get()
    print(ruta)


if __name__ == "__main__":
    main()