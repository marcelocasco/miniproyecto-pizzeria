import tkinter as tk
import time
from tkinter import messagebox

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Pizzería Digital")
ventana.geometry("500x550")

# Diccionario de precios de pizzas (¡Importante para esta funcionalidad!)
precios_pizzas = {
    "Muzzarella": 8000,
    "Napolitana": 9000,
    "Fugazzeta": 8500,
    "4 Quesos": 11000,
    "Rúcula": 10500,
    "Calabresa": 9500
}

# Lista de pedidos
lista_pedidos = tk.Listbox(ventana)
lista_pedidos.pack(pady=10, fill=tk.BOTH, expand=True)

# Menú desplegable
# --- MODIFICACIÓN AQUÍ: AGREGAR PIZZA CON PRECIO ---
def agregar_pedido(pizza):
    precio = precios_pizzas.get(pizza, 0) # Obtiene el precio, si no lo encuentra, usa 0
    lista_pedidos.insert(tk.END, f"{pizza} - ${precio:,.2f}")#el Listbox acumula las pizzas posteriormente toma mostrar_total

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_pizzas = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Menú de Pizzas", menu=menu_pizzas)

# Categorías de pizzas
clasicas = ["Muzzarella", "Napolitana", "Fugazzeta"]
especiales = ["4 Quesos", "Rúcula", "Calabresa"]

submenu_clasicas = tk.Menu(menu_pizzas, tearoff=0)
submenu_especiales = tk.Menu(menu_pizzas, tearoff=0)

for pizza in clasicas:
    submenu_clasicas.add_command(label=pizza, command=lambda p=pizza: agregar_pedido(p))
for pizza in especiales:
    submenu_especiales.add_command(label=pizza, command=lambda p=pizza: agregar_pedido(p))

menu_pizzas.add_cascade(label="Clásicas", menu=submenu_clasicas)
menu_pizzas.add_cascade(label="Especiales", menu=submenu_especiales)

# Botón para eliminar pedido
def eliminar_pedido():
    seleccion = lista_pedidos.curselection()
    if seleccion:
        lista_pedidos.delete(seleccion)

btn_eliminar = tk.Button(ventana, text="Eliminar Pedido", command=eliminar_pedido)
btn_eliminar.pack(pady=5)



## Funcionalidad de Mostrar Total (Ajustada)

#Para que la función `mostrar_total` siga funcionando correctamente, ahora necesita extraer solo el nombre de la pizza de la cadena ` "Pizza - $Precio" ` que se muestra en la `Listbox`.


def mostrar_total():
    total = 0
    items_pedido = lista_pedidos.get(0, tk.END) #items va de 0 al ultimo valor agregados anteriormente en agregar_pizza
    for item_str in items_pedido: 
        # Extraemos solo el nombre de la pizza de la cadena (ej. "Muzzarella - $8,000.00")
        pizza_nombre = item_str.split(' - ')[0] #guarda solamente el nombre
        if pizza_nombre in precios_pizzas:
            total += precios_pizzas[pizza_nombre] #llama al valor del diccionario con la clave nombre "clave:valor"
    
    messagebox.showinfo("Total del Pedido", f"El total de su pedido es: ${total:,.2f}")

btn_mostrar_total = tk.Button(ventana, text="Mostrar Total", command=mostrar_total)
btn_mostrar_total.pack(pady=5)
#Funcionalidad de Confirmar Pedido
#ython

def confirmar_pedido():
    if lista_pedidos.size() > 0:#messagebox tiene 2 texto 1 para la ventana y despues de la , coma lo que dice la ventana
        respuesta = messagebox.askyesno("Confirmar Pedido", "¿Desea confirmar su pedido?")#askyesno ventana si/no
        if respuesta:
            messagebox.showinfo("Pedido Confirmado", "¡Su pedido ha sido confirmado con éxito!")
            lista_pedidos.delete(0, tk.END)
        else:
            messagebox.showinfo("Pedido Cancelado", "Su pedido no ha sido confirmado.")
            lista_pedidos.delete(0, tk.END)
    else:
        messagebox.showwarning("Pedido Vacío", "No hay elementos en el pedido para confirmar.")

btn_confirmar_pedido = tk.Button(ventana, text="Confirmar Pedido", command=confirmar_pedido)
btn_confirmar_pedido.pack(pady=5)

reloj = tk.Label(ventana, font=('Arial', 20), bg='black', fg='white')
reloj.pack(pady=10)

def actualizar_reloj():
    hora_actual = time.strftime('%H:%M:%S')
    reloj.config(text=hora_actual)
    ventana.after(1000, actualizar_reloj)

actualizar_reloj()

ventana.mainloop()