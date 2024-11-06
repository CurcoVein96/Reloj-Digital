import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import time

# Crear la ventana principal
root = tk.Tk()
root.title("Reloj con Fondo")
root.geometry("500x300")

# Cargar y colocar la imagen de fondo
bg_image = Image.open("OneDrive/Escritorio/Reloj digital/fondo.jpg") # Reemplaza con la ruta de tu imagen
bg_image = bg_image.resize((500, 300), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Crear y colocar la etiqueta de tiempo sobre la imagen de fondo
time_label = Label(root, font=("Helvetica", 24), fg="white", bg="black")  # Puedes ajustar el color y fuente
time_label.place(relx=0.5, rely=0.5, anchor="center")

# Función para actualizar la hora
def update_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, update_time)  # Actualiza cada segundo

update_time()  # Llamada inicial

root.mainloop()
