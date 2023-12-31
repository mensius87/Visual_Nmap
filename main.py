import tkinter as tk
import pyperclip
from tkinter import ttk, Menu
import ipaddress

# Funciones para las opciones del menú
def salir():
    ventana_principal.destroy()

def modo_oscuro():
    # Implementa la funcionalidad del modo oscuro
    pass

def modo_claro():
    # Implementa la funcionalidad del modo claro
    pass

def es_rango_ip_valido(rango_ip):
    try:
        ip_inicio, ip_fin = rango_ip.split('-')
        ipaddress.ip_address(ip_inicio)  # Verifica si la primera parte es una IP válida

        ip_fin = int(ip_fin)  # Verifica si la segunda parte es un número entero
        if ip_fin < 0 or ip_fin > 255:
            return False
    except (ValueError, TypeError):
        return False

    return True


def es_direccion_o_red_valida(direccion):
    try:
        # Intenta interpretar la entrada como una dirección IP
        ipaddress.ip_address(direccion)
        return True

    except ValueError:
        try:
            # Si falla, intenta interpretar la entrada como una red
            ipaddress.ip_network(direccion, strict=False)
            return True
        except ValueError:
            return es_rango_ip_valido(direccion)

def manejar_incompatibilidad_A_O():
    if var_A.get() == 1:
        check_O.config(state=tk.DISABLED)
        var_O.set(0)
    else:
        check_O.config(state=tk.NORMAL)

    if var_O.get() == 1:
        check_A.config(state=tk.DISABLED)
        var_A.set(0)
    else:
        check_A.config(state=tk.NORMAL)


# Función para actualizar la consulta de Nmap
def actualizar_consulta_nmap(*args):
    cuadro_texto_consulta_generada.config(state=tk.NORMAL)
    cuadro_texto_consulta_generada.delete('1.0', tk.END)

    ip_valor = entrada_texto_ip.get()

    if es_direccion_o_red_valida(ip_valor):
        entrada_texto_ip.config(bg='#009933')  # Fondo verde para entrada válida
        # Continuar con la actualización de la consulta si la entrada es válida

    else:
        entrada_texto_ip.config(bg='#ff4d4d')  # Fondo rojo para entrada inválida
    
    # Variables para los comandos
    ip_valor = entrada_texto_ip.get()
    descubrimiento_red = opcion_seleccionada_descubrimiento_red.get()
    tecnicas_escaneo = opcion_seleccionada_tecnica_escaneo.get()

    consulta = "nmap"  # Texto base

    if descubrimiento_red != "None":
        consulta += f" {descubrimiento_red}"

    if tecnicas_escaneo != "None":
        consulta += f" {tecnicas_escaneo}"

    # Verificar el estado de cada Checkbutton y añadir a la consulta
    if var_sV.get() == 1:
        consulta += " -sV"
    if var_A.get() == 1:
        consulta += " -A"
    if var_O.get() == 1:
        consulta += " -O"
    if var_f.get() == 1:
        consulta += " -f"
    if var_T.get() == 1:
        consulta += " -T"

    consulta += f" {ip_valor}"

    cuadro_texto_consulta_generada.insert(tk.END, consulta)
    cuadro_texto_consulta_generada.config(state=tk.DISABLED)


def copiar_al_portapapeles():
    texto_a_copiar= cuadro_texto_consulta_generada.get("1.0", "end-1c")  # Obtiene el texto del área de consulta
    pyperclip.copy(texto_a_copiar)  # Copia el texto al portapapeles

def limpiar_texto_consulta():
    cuadro_texto_consulta_generada.config(state=tk.NORMAL)
    cuadro_texto_consulta_generada.delete("1.0", "end")
    cuadro_texto_consulta_generada.insert(tk.END, comando_fijado_de_serie_nmap)
    cuadro_texto_consulta_generada.config(state=tk.DISABLED)
    opcion_seleccionada_descubrimiento_red.set(None)
    opcion_seleccionada_tecnica_escaneo.set(None)
    entrada_texto_ip.delete("0", "end")
    entrada_texto_ip.config(bg="white")
    var_sV.set(0)
    var_A.set(0)
    var_O.set(0)
    var_f.set(0)
    var_T.set(0)



# ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Generador de consultas Nmap")
ventana_principal.geometry("1500x600")
ventana_principal.minsize(1600, 650)

# Crear un objeto menú
menu_bar = Menu(ventana_principal)

# Crear el menú Archivo y añadir comandos
menu_archivo = Menu(menu_bar, tearoff=0)
menu_archivo.add_command(label="Salir", command=salir)
menu_bar.add_cascade(label="Archivo", menu=menu_archivo)

# Crear el menú Ver y añadir comandos
menu_ver = Menu(menu_bar, tearoff=0)
menu_ver.add_command(label="Modo Oscuro", command=modo_oscuro)
menu_ver.add_command(label="Modo Claro", command=modo_claro)
menu_bar.add_cascade(label="Ver", menu=menu_ver)

# Crear el menú Ayuda y añadir comandos
menu_ayuda = Menu(menu_bar, tearoff=0)
menu_ayuda.add_command(label="Sobre el autor")
menu_bar.add_cascade(label="Ayuda", menu=menu_ayuda)

# Configurar la ventana para usar este menú
ventana_principal.config(menu=menu_bar)

# Obtener dimensiones de la pantalla
ancho_pantalla = ventana_principal.winfo_screenwidth()
alto_pantalla = ventana_principal.winfo_screenheight()

# Posicionar la ventana
ventana_principal.geometry(f"+{ancho_pantalla}+0")



# Contenedor derecho
marco_derecho = tk.Frame(ventana_principal)
marco_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Sección resultado
seccion_resultado_consulta = tk.LabelFrame(marco_derecho, padx=10, pady=10, text="Resultado de la consulta")
seccion_resultado_consulta.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Cuadro de texto para los resultados de nmap
resultado_nmap = tk.Text(seccion_resultado_consulta, bg="black")
resultado_nmap.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Sección salida de resultados
seccion_exportar_resultados = tk.LabelFrame(marco_derecho, padx=10, pady=10, text="Exportar resultado")
seccion_exportar_resultados.pack(padx=10, pady=10, fill=tk.X)

# Marco para la entrada de texto y su label
marco_entrada_texto_nombre_salida_archivo = tk.Frame(seccion_exportar_resultados)
marco_entrada_texto_nombre_salida_archivo.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

label_nombre_archivo = tk.Label(marco_entrada_texto_nombre_salida_archivo, text="Nombre de archivo")
label_nombre_archivo.pack()

entrada_nombre_archivo = tk.Entry(marco_entrada_texto_nombre_salida_archivo)
entrada_nombre_archivo.pack()

# Marco para los checkbuttons
marco_checkbuttons = tk.Frame(seccion_exportar_resultados)
marco_checkbuttons.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

# Checkbuttons
check_normal = tk.Checkbutton(marco_checkbuttons, text="Normal")
check_normal.grid(row=0, column=0, sticky="w")

check_xml = tk.Checkbutton(marco_checkbuttons, text="-oX --> XML")
check_xml.grid(row=0, column=1, sticky="w")

check_grepable = tk.Checkbutton(marco_checkbuttons, text="-oG --> Greppable")
check_grepable.grid(row=1, column=0, sticky="w")

check_todos_formatos = tk.Checkbutton(marco_checkbuttons, text="-oA --> Todos los formatos")
check_todos_formatos.grid(row=1, column=1, sticky="w")






# Contenedor izquierdo
marco_izquierdo = tk.Frame(ventana_principal)
marco_izquierdo.pack(side=tk.LEFT, fill=tk.BOTH)

# etiqueta entrada ip o red
etiqueta_casilla_ip = tk.Label(marco_izquierdo, text="Introduce IP, rango o red")
etiqueta_casilla_ip.pack()

# Casilla de entrada para introducir IP o red
entrada_texto_ip = tk.Entry(marco_izquierdo, width=40, fg="white")
entrada_texto_ip.pack()
entrada_texto_ip.bind('<KeyRelease>', lambda event: actualizar_consulta_nmap())

# Sección consulta generada
seccion_consulta_generada = tk.LabelFrame(marco_izquierdo, text="Consulta generada para Nmap")
seccion_consulta_generada.pack(padx=10, pady=10, fill=tk.BOTH)



# Contenedor general consulta generada
contenedor_general_consulta_generada = tk.Frame(seccion_consulta_generada)
contenedor_general_consulta_generada.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)



# Contenedor consulta generada
contenedor_consulta_generada = tk.Frame(contenedor_general_consulta_generada)
contenedor_consulta_generada.pack(padx=5, pady=5, fill=tk.X)

# Cuadro texto consulta generada
cuadro_texto_consulta_generada = tk.Text(contenedor_consulta_generada, height=2, width=100)
cuadro_texto_consulta_generada.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Insertar texto inicial "nmap" y deshabilitar la edición
comando_fijado_de_serie_nmap = "nmap"  # Texto inicial predeterminado
cuadro_texto_consulta_generada.insert(tk.END, comando_fijado_de_serie_nmap)
cuadro_texto_consulta_generada.config(state=tk.DISABLED)



# Contenedor botones
contenedor_botones = tk.Frame(contenedor_general_consulta_generada)
contenedor_botones.pack(padx=5, pady=5, fill=tk.X)

# Botón copiar
icono_copiar = tk.PhotoImage(file="images/duplicar.png")
boton_copiar = tk.Button(contenedor_botones, text="Copiar", bg="blue", image=icono_copiar, command=copiar_al_portapapeles)
boton_copiar.pack(side=tk.RIGHT, padx=5)

# Botón limpiar
icono_limpiar_consulta = tk.PhotoImage(file="images/limpiar.png")
boton_limpiar_consulta = tk.Button(contenedor_botones, text="Limpiar", bg="red", image=icono_limpiar_consulta, command=limpiar_texto_consulta)
boton_limpiar_consulta.pack(side=tk.RIGHT, padx=5)

# Botón escanear
boton_escanear = tk.Button(contenedor_botones, text="ESCANEAR", bg="green", fg="white")
boton_escanear.pack(side=tk.BOTTOM, padx=5, fill=tk.BOTH, expand=True)



# Sección opciones avanzadas
seccion_encabezado_opciones_avanzadas = tk.LabelFrame(marco_izquierdo, padx=5 ,pady=5,text="Opciones avanzadas")
seccion_encabezado_opciones_avanzadas.pack(padx=10, pady=10, fill=tk.BOTH)



# Crear Notebook (Pestañas)
notebook = ttk.Notebook(seccion_encabezado_opciones_avanzadas)
notebook.pack(expand=True, fill="both")

# Crear pestañas
tab_descubrimiento_red = ttk.Frame(notebook)
tab_tecnica_escaneo = ttk.Frame(notebook)
tab_opciones_servicios_y_version = ttk.Frame(notebook)
tab_puertos = ttk.Frame(notebook)

# Añadir pestañas al notebook
notebook.add(tab_descubrimiento_red, text="Descubrimiento de Red")
notebook.add(tab_tecnica_escaneo, text="Ténica de Escaneo")
notebook.add(tab_opciones_servicios_y_version, text="Servicios y versiones")
notebook.add(tab_puertos, text="Puertos")




# Diccionario con opciones y sus descripciones
opciones_descubrimiento_red = {
    "-sL": "List Scan: Simplemente lista las IP especificadas sin enviar paquetes a ellas.",
    "-sn": "Ping Scan: Realiza un escaneo ping para determinar qué hosts están activos.",
    "-Pn": "No Ping: Evita el descubrimiento de hosts y asume que están activos.",
    "-PS": "TCP SYN Ping Scan: Utiliza un escaneo SYN para determinar qué hosts están activos.",
    "-PA": "TCP ACK Ping Scan: Utiliza paquetes ACK para determinar qué hosts están activos.",
    "-PU": "UDP Ping Scan: Utiliza paquetes UDP para determinar qué hosts están activos.",
    "-PR": "ARP Ping Scan: Utiliza solicitudes ARP para determinar qué hosts están activos.",
    "-n": "No DNS Resolution: Evita la resolución DNS durante el escaneo."
}

# Variable para guardar la opción seleccionada
opcion_seleccionada_descubrimiento_red = tk.StringVar(value="")

# Crear botones radiales y descripciones alineadas horizontalmente
for opcion_descubrimiento_red, descripcion_tipos_descubrimiento in opciones_descubrimiento_red.items():
    contenedor_opciones_descubrimiento_red = tk.Frame(tab_descubrimiento_red, padx=3, pady=3)
    contenedor_opciones_descubrimiento_red.pack(anchor=tk.W)

    radiobutton_opcion_descubrimiento_red = tk.Radiobutton(contenedor_opciones_descubrimiento_red, text=opcion_descubrimiento_red, variable=opcion_seleccionada_descubrimiento_red, value=opcion_descubrimiento_red, command=actualizar_consulta_nmap)
    radiobutton_opcion_descubrimiento_red.pack(side=tk.LEFT)

    descripcion_tecnica_escaneo = tk.Label(contenedor_opciones_descubrimiento_red, text=f"--> {descripcion_tipos_descubrimiento}", anchor="w", justify="left")
    descripcion_tecnica_escaneo.pack(side=tk.LEFT, fill="x")

# Asociar None como valor inicial para deseleccionar
opcion_seleccionada_descubrimiento_red.set(None)




# Sección ténicas de escaneo
# Diccionario con opciones y sus descripciones
opciones_tecnica_escaneo = {
    "-sS": "TCP SYN Scan: Escanea puertos específicos utilizando un paquete SYN.",
    "-sT": "TCP Connect Scan: Conecta a los puertos especificados para determinar si están abiertos.",
    "-sA": "TCP ACK Scan: Determina si los puertos están filtrados, no filtrados o cerrados.",
    "-sU": "UDP Scan: Escanea puertos UDP para determinar su estado.",
    "-Sf": "FIN Scan: Envía un paquete FIN para determinar si el puerto está abierto o cerrado.",
    "-sX": "Xmas Scan: Envía un conjunto de flags para determinar la respuesta del puerto.",
    "-Sp": "SCTP INIT Scan: Escanea puertos SCTP utilizando el mensaje INIT.",
    "-sN": "Null Scan: Envía un paquete con todos los flags TCP apagados para determinar la respuesta del puerto.",
    "-sL": "List Scan: Lista las IP sin enviar paquetes a ellas."
}

# Variable para guardar la opción seleccionada
opcion_seleccionada_tecnica_escaneo = tk.StringVar(value="")

for opcion_tecnica_escaneo, descripcion_tecnica_escaneo in opciones_tecnica_escaneo.items():
    contenedor_tecnica_escaneo = tk.Frame(tab_tecnica_escaneo, padx=3, pady=3)
    contenedor_tecnica_escaneo.pack(anchor=tk.W)

    rb = tk.Radiobutton(contenedor_tecnica_escaneo, text=opcion_tecnica_escaneo, variable=opcion_seleccionada_tecnica_escaneo, value=opcion_tecnica_escaneo, command=actualizar_consulta_nmap)
    rb.pack(side=tk.LEFT)

    desc_label = tk.Label(contenedor_tecnica_escaneo, text=f"--> {descripcion_tecnica_escaneo}", anchor="w", justify="left")
    desc_label.pack(side=tk.LEFT, fill="x")

opcion_seleccionada_tecnica_escaneo.set(None)



# Sección servicios y versiones
# Diccionario con opciones y descripciones
opciones_servicios_y_versiones = {
    "-sV": "nivel de intensidad",
    "-A": "activar detección de sistema operativo y versión de servicios",
    "-O": "activar detección de sistema operativo",
    "-f": "utilizar técnicas de fragmentación",
    "-T": "Timing (velocidad del escaneo)"
}

contenedor_servicios_y_versiones = tk.Frame(tab_opciones_servicios_y_version, padx=3, pady=3)
contenedor_servicios_y_versiones.pack(anchor=tk.W)

# Variable de control para cada Checkbutton
var_sV = tk.IntVar(value=0)
var_A = tk.IntVar(value=0)
var_O = tk.IntVar(value=0)
var_f = tk.IntVar(value=0)
var_T = tk.IntVar(value=0)

# Crear Checkbutton y Label para -sV
contenedor_sV = tk.Frame(contenedor_servicios_y_versiones, padx=3, pady=3)
contenedor_sV.pack(fill=tk.X)
check_sV = tk.Checkbutton(contenedor_sV, text="-sV", variable=var_sV, command=actualizar_consulta_nmap)
check_sV.pack(side=tk.LEFT)
label_sV = tk.Label(contenedor_sV, text=f"--> {opciones_servicios_y_versiones['-sV']}")
label_sV.pack(side=tk.LEFT)

# Crear Checkbutton y Label para -A
contenedor_A = tk.Frame(contenedor_servicios_y_versiones, padx=3, pady=3)
contenedor_A.pack(fill=tk.X)
check_A = tk.Checkbutton(contenedor_A, text="-A", variable=var_A, command=lambda: [manejar_incompatibilidad_A_O(), actualizar_consulta_nmap()])
check_A.pack(side=tk.LEFT)
label_A = tk.Label(contenedor_A, text=f"--> {opciones_servicios_y_versiones['-A']}")
label_A.pack(side=tk.LEFT)

# Crear Checkbutton y Label para -O
contenedor_O = tk.Frame(contenedor_servicios_y_versiones, padx=3, pady=3)
contenedor_O.pack(fill=tk.X)
check_O = tk.Checkbutton(contenedor_O, text="-O", variable=var_O, command=lambda: [manejar_incompatibilidad_A_O(), actualizar_consulta_nmap()])
check_O.pack(side=tk.LEFT)
label_O = tk.Label(contenedor_O, text=f"--> {opciones_servicios_y_versiones['-O']}")
label_O.pack(side=tk.LEFT)

# Crear Checkbutton y Label para -f
contenedor_f = tk.Frame(contenedor_servicios_y_versiones, padx=3, pady=3)
contenedor_f.pack(fill=tk.X)
check_f = tk.Checkbutton(contenedor_f, text="-f", variable=var_f, command=actualizar_consulta_nmap)
check_f.pack(side=tk.LEFT)
label_f = tk.Label(contenedor_f, text=f"--> {opciones_servicios_y_versiones['-f']}")
label_f.pack(side=tk.LEFT)

# Crear Checkbutton y Label para -T
contenedor_T = tk.Frame(contenedor_servicios_y_versiones, padx=3, pady=3)
contenedor_T.pack(fill=tk.X)
check_T = tk.Checkbutton(contenedor_T, text="-T", variable=var_T, command=actualizar_consulta_nmap)
check_T.pack(side=tk.LEFT)
label_T = tk.Label(contenedor_T, text=f"--> {opciones_servicios_y_versiones['-T']}")
label_T.pack(side=tk.LEFT)



# Ejecución de la ventana principal
ventana_principal.mainloop()