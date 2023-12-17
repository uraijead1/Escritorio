
from PIL import ImageTk, Image
import customtkinter 
import tkinter

customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("dark")

app = customtkinter.CTk()
app.geometry("600x400")
app.title("Inicio de Sesión")

def button():
    app.destroy()
    w = customtkinter.CTk()
    w.geometry('1280x720')
    w.title("Aplicativo")
    label = customtkinter.CTkLabel(master=w, text='HOLA')
    label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    w.mainloop()

imgFondo = ImageTk.PhotoImage(Image.open("img/fondo.png"))

l1 = customtkinter.CTkLabel(master=app, image=imgFondo)
l1.pack()

frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2 = customtkinter.CTkLabel(master=frame, text="Inicio de Sesión", font=('Century Gothic', 20))
l2.place(x=50, y=45)

entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Usuario")
entry1.place(x=50, y=100)

entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Contraseña", show='*')
entry2.place(x=50, y=155)

l2 = customtkinter.CTkLabel(master=frame, text="¿Olvistaste tu contraseña?", font=("Century Gothic", 12))
l2.place(x=105, y=195)

btnIngresar = customtkinter.CTkButton(master=frame, width=220, text="Ingresar", corner_radius=6, command=button)
btnIngresar.place(x=50, y=240)

app.mainloop()