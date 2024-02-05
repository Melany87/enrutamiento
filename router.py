import tkinter as tk
from PIL import Image, ImageTk

def disconnect_link():
    selected_router = disconnect_router_var.get()
    router = routers[selected_router]
    router_status[selected_router].set('desconectado')
    router.configure(bg='red')

def reconnect_link():
    selected_router = connect_router_var.get()
    router = routers[selected_router]
    router_status[selected_router].set('conectado')
    router.configure(bg='green')

# Crear la ventana principal
root = tk.Tk()
root.title('Simulador de Red')

# Configurar variables para las opciones de selección
disconnect_router_var = tk.StringVar()
connect_router_var = tk.StringVar()

# Crear contenedor principal
container = tk.Frame(root, width=1100, bg='#fff', padx=90, pady=20, bd=5, relief='solid')
container.pack()

# Crear routers y conexiones
routers = {}
router_status = {}

for router_id in range(1, 5):
    router_key = f'router{router_id}'

    router_status[router_key] = tk.StringVar()
    router_status[router_key].set('X')

    image = Image.open(f'router.png')  # Ajusta la ruta y la extensión de la imagen según tu caso
    image = image.resize((130, 140), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
    photo = ImageTk.PhotoImage(image)

    router = tk.Label(container, text=f'R{router_id}', width=150, height=160, font=('Arial', 16, 'bold'),
                      bg='gray', fg='white', bd=2, relief='solid', textvariable=router_status[router_key],
                      image=photo, compound='top')
    router.image = photo  # Para evitar que la imagen se elimine debido a la recolección de basura de Python
    router.grid(row=0, column=(router_id - 1) * 2, padx=10, pady=5)

    routers[router_key] = router

    # Agregar conexiones horizontales
    if router_id < 4:
        connection_line = tk.Frame(container, width=50, height=2, bg='#3498db')
        connection_line.grid(row=0, column=(router_id - 1) * 2 + 1, pady=5)

# Crear opciones de selección para desconectar enlace
disconnect_router_label = tk.Label(container, text='Seleccione el router a desconectar:')
disconnect_router_label.grid(row=1, column=0, pady=5, sticky='e')

disconnect_router_menu = tk.OptionMenu(container, disconnect_router_var, *routers.keys())
disconnect_router_menu.grid(row=1, column=1, pady=5)

disconnect_button = tk.Button(container, text='Desconectar Enlace', command=disconnect_link)
disconnect_button.grid(row=2, column=0, columnspan=2, pady=10)

# Crear opciones de selección para reconectar enlace
connect_router_label = tk.Label(container, text='Seleccione el router a conectar:')
connect_router_label.grid(row=3, column=0, pady=5, sticky='e')

connect_router_menu = tk.OptionMenu(container, connect_router_var, *routers.keys())
connect_router_menu.grid(row=3, column=1, pady=5)

connect_button = tk.Button(container, text='Reconectar Enlace', command=reconnect_link)
connect_button.grid(row=4, column=0, columnspan=2, pady=10)

# Iniciar la aplicación
root.mainloop()
