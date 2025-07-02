import tkinter as tk
import time

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Pizzería Digital")
ventana.geometry("500x400")

# Lista de pedidos (posteriormente se irán cargando)"LISTA"
lista_pedidos = tk.Listbox(ventana)
lista_pedidos.pack(pady=10)

# Menú desplegable (carga de pizzas) "CARGA"
def agregar_pedido(pizza):
    lista_pedidos.insert(tk.END, pizza)
#barra sostenedora
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)
#menu principal
menu_pizzas = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Menú de Pizzas", menu=menu_pizzas)

# Categorías de pizzas
clasicas = ["Muzzarella", "Napolitana", "Fugazzeta"] 
especiales = ["4 Quesos", "Rúcula", "Calabresa"]
#menu secundario (todavia no agrego al menu principal tengo que seleccionar y recorrer)
submenu_clasicas = tk.Menu(menu_pizzas, tearoff=0)
submenu_especiales = tk.Menu(menu_pizzas, tearoff=0)
#recorre y selecciona la pizza "SELECCION"
for pizza in clasicas:
    #"lambda p=pizza: crea una función anónima que guarda el valor actual de pizza en una copia local (p).
    # Así, cuando se hace clic en el ítem del menú, se llama a agregar_pedido(p) con el valor correcto."
    # de lo contrario por el for tomaria solo la ultima pizza
    submenu_clasicas.add_command(label=pizza, command=lambda p=pizza: agregar_pedido(p))
for pizza in especiales:
    submenu_especiales.add_command(label=pizza, command=lambda p=pizza: agregar_pedido(p))
#agrega las listas a cada submenu "AGREGA" (recien acá agrego el menu)
menu_pizzas.add_cascade(label="Clásicas", menu=submenu_clasicas)
menu_pizzas.add_cascade(label="Especiales", menu=submenu_especiales)

# Botón para eliminar pedido "ELIMINA"
def eliminar_pedido():
    seleccion = lista_pedidos.curselection()
    if seleccion:
        lista_pedidos.delete(seleccion)

btn_eliminar = tk.Button(ventana, text="Eliminar Pedido", command=eliminar_pedido)
btn_eliminar.pack(pady=5)

# Reloj en tiempo real "TIEMPO"
reloj = tk.Label(ventana, font=('Arial', 20), bg='black', fg='white')
reloj.pack(pady=10)

def actualizar_reloj():
    hora_actual = time.strftime('%H:%M:%S')
    reloj.config(text=hora_actual)
    ventana.after(1000, actualizar_reloj)

actualizar_reloj()

ventana.mainloop()
