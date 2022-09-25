
import tkinter as tk
from tkinter import messagebox

"""
Integrantes: 
Harold Enoc Santos Morillo SMIS001621
Meylin Nohely Reyes Medina SMIS032721
Maira Liseth Ramos Parada SMIS012921
"""



def calcular_pago():
    cantidad = float(textCant.get())
    precio = float(textPrecio.get())
    total = round(cantidad*precio,2)

    op = radio.get()

    if(op == 1):

        messagebox.showinfo(title="Pago a realizar", message= f"Debe pagar un total de ${total}")

        pass
    elif(op == 2):
        descuento= round((total*0.20),2)
        pago = total - descuento

        text = f"""
            Descuento por pagar con tarjeta de crédito: ${descuento}
            Total a pagar: ${pago}
        """

        messagebox.showinfo(title="Pago a realizar", message= text)
        pass



    pass

ventana = tk.Tk()
ventana.geometry("550x400")
ventana.config(bg="#F0F8FF")
ventana.title("Cajero del Super Mercado")
textCant = tk.Entry(ventana, bg="#FFEBCD")
textPrecio = tk.Entry(ventana, bg="#FFEBCD")
labelCant = tk.Label(ventana, text="Cantidad de producto")
labelPrecio = tk.Label(ventana, text="Precio del producto")

radio = tk.IntVar()
radioOp1 = tk.Radiobutton(ventana, text = "Pagar en efectivo", value= 1, variable= radio)
radioOp2 = tk.Radiobutton(ventana, text = "Pagar con tarjeta de crédito", value= 2, variable= radio)
boton1 = tk.Button(ventana, text= "Calcular Pago", command=calcular_pago)
boton1.config(bg="#5F9EA0")

textCant.place(x=20, y=20, width=200,height=20)
textPrecio.place(x=20, y=60, width=200,height=20)
labelCant.place(x=220, y=20, width=200,height=20)
labelPrecio.place(x=220, y=60, width=200,height=20)

radioOp1.place(x=50, y=100, width=200,height=20)
radioOp2.place(x=240, y=100, width=200,height=20)
boton1.place(x=180, y=160, width=130,height=40)

ventana.mainloop()


