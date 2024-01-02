import tkinter as tk
from tkinter import ttk, Menu, messagebox, font
import os, sys, json, ipaddress, pyperclip


def mostrar_sobre_el_autor():
    ventana_sobre_autor = tk.Toplevel(pady=10)
    ventana_sobre_autor.title("Sobre el Autor")
    ventana_sobre_autor.geometry("550x375")  # Ajusta el tamaño según tus necesidades
    ventana_sobre_autor.config(bg="#333333")

    def abrir_enlace():
        import webbrowser
        webbrowser.open("https://github.com/mensius87")

    # Cargar y mostrar la imagen del icono
    ruta_imagen_icono = "images/Visual_Nmap_icono.png"
    imagen_icono = tk.PhotoImage(file=ruta_imagen_icono)
    label_imagen_icono = tk.Label(ventana_sobre_autor, image=imagen_icono, bg="#333333")
    label_imagen_icono.image = imagen_icono  # Guarda una referencia de la imagen
    label_imagen_icono.pack()

    fuente_grande = font.Font(family="Helvetica", size=14)
    enlace_label = tk.Label(ventana_sobre_autor, text="Programa desarrolado por mensius87. Licencia MIT. Mis proyectos:" , bg="#333333", fg="white")
    enlace_label.pack()

    # Crear un label con el enlace
    enlace_label = tk.Label(ventana_sobre_autor, text="https://github.com/mensius87", fg="blue", cursor="hand2", bg="#333333", font=fuente_grande)
    enlace_label.pack()

    # Asociar la función abrir_enlace al clic en el label
    enlace_label.bind("<Button-1>", lambda event: abrir_enlace())

    # Cargar y mostrar la imagen del banner
    ruta_imagen_banner = "images/banner_autor.png"
    imagen_banner = tk.PhotoImage(file=ruta_imagen_banner)
    label_imagen_banner = tk.Label(ventana_sobre_autor, image=imagen_banner, bg="#333333")
    label_imagen_banner.image = imagen_banner  # Guarda una referencia de la imagen
    label_imagen_banner.pack()


# Funciones para las opciones del menú
def salir():
    ventana_principal.destroy()

# Colores para el modo oscuro
colores_modo_oscuro = {
    "fondo": "#333333",  # Color de fondo oscuro
    "texto": "#FFFFFF",  # Color de texto claro
}

def modo_oscuro():
    # Establecer el fondo de la ventana principal y los frames
    ventana_principal.config(bg=colores_modo_oscuro["fondo"])
    marco_derecho.config(bg=colores_modo_oscuro["fondo"])
    marco_izquierdo.config(bg=colores_modo_oscuro["fondo"])
    marco_entrada_texto_nombre_salida_archivo.config(bg="#dcdad5")
    menu_bar.config(bg="#dcdad5")
    menu_archivo.config(bg="#dcdad5")
    menu_ver.config(bg="#dcdad5")
    menu_ayuda.config(bg="#dcdad5")

    seccion_resultado_consulta.config(bg=colores_modo_oscuro["fondo"], fg=colores_modo_oscuro["texto"])
    seccion_exportar_resultados.config(bg=colores_modo_oscuro["fondo"], fg=colores_modo_oscuro["texto"])
    seccion_consulta_generada.config(bg=colores_modo_oscuro["fondo"], fg=colores_modo_oscuro["texto"])
    seccion_encabezado_opciones_avanzadas.config(bg=colores_modo_oscuro["fondo"], fg=colores_modo_oscuro["texto"])

    contenedor_general_consulta_generada.config(bg="#dcdad5")
    contenedor_botones.config(bg="#dcdad5")
    contenedor_A.config(bg="#dcdad5")
    contenedor_f.config(bg="#dcdad5")
    contenedor_O.config(bg="#dcdad5")
    contenedor_sV.config(bg="#dcdad5")
    contenedor_T.config(bg="#dcdad5")
    contenedor_checkbuttons_exportar_resultados.config(bg="#dcdad5")
    contenedor_principal_exportar.config(bg="#dcdad5")

    check_normal.config(bg="#dcdad5")
    check_todos_formatos.config(bg="#dcdad5")
    check_grepable.config(bg="#dcdad5")
    check_xml.config(bg="#dcdad5")

    label_nombre_archivo.config(bg="#dcdad5")


    # Cambiar el estilo de los widgets en cada pestaña
    for tab in [tab_descubrimiento_red, tab_tecnica_escaneo, tab_opciones_servicios_y_version, tab_puertos]:
        for widget in tab.winfo_children():
            widget.config(bg="#dcdad5")
            for child in widget.winfo_children():
                if isinstance(child, (tk.Radiobutton, tk.Checkbutton, tk.Label)):
                    child.config(bg="#dcdad5")

    # Configurar el estilo para las pestañas del ttk.Notebook
    style = ttk.Style()
    style.theme_use('clam')  # Usar un tema que permita más personalización

    # Configurar el estilo de las pestañas
    style.configure('Custom.Tab', background=colores_modo_oscuro['fondo'], foreground=colores_modo_oscuro['texto'])

    # Cambiar el estilo de los radiobuttons y checkbuttons
    check_sV.config(bg="#dcdad5")
    check_A.config(bg="#dcdad5")
    check_T.config(bg="#dcdad5")
    check_O.config(bg="#dcdad5")
    check_f.config(bg="#dcdad5")

    # Cambiar el estilo de las etiquetas
    etiqueta_casilla_ip.config(bg=colores_modo_oscuro["fondo"], fg=colores_modo_oscuro["texto"])
    label_nombre_archivo.config(bg="#dcdad5")
    label_A.config(bg="#dcdad5")
    label_f.config(bg="#dcdad5")
    label_O.config(bg="#dcdad5")
    label_sV.config(bg="#dcdad5")
    label_T.config(bg="#dcdad5")


def modo_claro():
    # Preguntar al usuario si realmente quiere reiniciar el programa
    respuesta = messagebox.askyesno("Confirmar reinicio", "Para habilitar el modo claro se necesita reiniciar. Se perderá el progreso actual. ¿Deseas continuar con el reinicio?")
    if respuesta:
        # Si el usuario responde que sí, reinicia el programa
        ventana_principal.destroy()
        os.execl(sys.executable, sys.executable, *sys.argv)


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

def manejar_estado_nivel_intensidad():
    global sV_escala_usada
    # Habilitar o deshabilitar el Scale basado en el estado del Checkbutton -sV
    if var_sV.get() == 1:
        scale_nivel_intensidad.config(state=tk.NORMAL)
    else:
        scale_nivel_intensidad.config(state=tk.DISABLED)
        sV_escala_usada = False  # Restablecer la bandera a False


sV_escala_usada = False

def on_scale_movido(val):
    global sV_escala_usada
    if not sV_escala_usada:
        sV_escala_usada = True
    if var_sV.get() == 0:
        sV_escala_usada = False

    actualizar_consulta_nmap()



# Función para actualizar la consulta de Nmap
def actualizar_consulta_nmap(*args):
    cuadro_texto_consulta_generada.config(state=tk.NORMAL)
    cuadro_texto_consulta_generada.delete('1.0', tk.END)

    #print(opcion_seleccionada_puertos.get())
    #print(entrada_puerto.get())

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
    manejar_estado_nivel_intensidad()
    nivel_instensidad_sV = var_nivel_intensidad.get()

    if var_sV.get() == 1:
        consulta += " -sV"
        if sV_escala_usada == True:
            consulta += f" --version-intensity {nivel_instensidad_sV}"
    if var_A.get() == 1:
        consulta += " -A"
    if var_O.get() == 1:
        consulta += " -O"
    if var_f.get() == 1:
        consulta += " -f"
    if var_T.get() == 1:
        consulta += " -T"


    # Añadir la opción de puertos
    puerto_seleccionado = opcion_seleccionada_puertos.get()
    if puerto_seleccionado == "-p" and entrada_puerto.get():
        consulta += f" -p{entrada_puerto.get()}"
    elif puerto_seleccionado == "-p rango" and (entrada_puerto_inicio.get() and entrada_puerto_fin.get()):
        consulta += f" -p{entrada_puerto_inicio.get()}-{entrada_puerto_fin.get()}"
    elif puerto_seleccionado == "-p-":
        consulta += " -p-"
    elif puerto_seleccionado == "-p específicos" and entrada_puertos_especificos.get():
        if entrada_puertos_especificos.get().endswith(","):
            entrada_puertos_especificos_sin_coma_final = entrada_puertos_especificos.get()
            consulta += f" -p{entrada_puertos_especificos_sin_coma_final[:-1]}"
        else:
            consulta += f" -p{entrada_puertos_especificos.get()}"
    elif puerto_seleccionado == "-F":
        consulta += " -F"

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


def actualizar_puertos(*args):

    if opcion_seleccionada_puertos.get() == "-p":
        consulta = opcion_seleccionada_puertos.get() + " " + entrada_puerto.get()
        entrada_puerto.bind('<KeyRelease>', actualizar_consulta_nmap())
        actualizar_consulta_nmap()
        print(consulta)


    elif opcion_seleccionada_puertos.get() == "-p rango":
        actualizar_consulta_nmap()
        seleccion_puerto = entrada_puerto_inicio.bind('<KeyRelease>', lambda event: actualizar_consulta_nmap())


def validar_puerto_unico(event):
    try:
        puerto = int(entrada_puerto.get())
        if 1 <= puerto <= 65535:
            entrada_puerto.config(bg="#009933", fg="white") # verde
        else:
            entrada_puerto.config(bg="#ff4d4d") # rojo
            actualizar_consulta_nmap()
    except ValueError:
        entrada_puerto.config(bg="#ff4d4d") # rojo

    if entrada_puerto.get() == "":
        entrada_puerto.config(bg="white")  # blanco

    actualizar_consulta_nmap()


def validar_rango_puertos(event):
    puerto_inicio_valido = False
    puerto_fin_valido = False
    puerto_inicio = None
    puerto_fin = None

    texto_puerto_inicio = entrada_puerto_inicio.get()
    texto_puerto_fin = entrada_puerto_fin.get()

    # Validar puerto de inicio
    if texto_puerto_inicio:
        try:
            puerto_inicio = int(texto_puerto_inicio)
            if 1 <= puerto_inicio <= 65535:
                puerto_inicio_valido = True
        except ValueError:
            pass

    # Validar puerto final
    if texto_puerto_fin:
        try:
            puerto_fin = int(texto_puerto_fin)
            if 1 <= puerto_fin <= 65535:
                puerto_fin_valido = True
        except ValueError:
            pass

    # Comprobar la coherencia del rango
    rango_valido = puerto_inicio_valido and puerto_fin_valido and (puerto_inicio is not None) and (puerto_fin is not None) and (puerto_inicio <= puerto_fin)

    # Actualizar colores de fondo según la validación
    color_inicio = "#009933" if puerto_inicio_valido and rango_valido else ("white" if texto_puerto_inicio == "" else "#ff4d4d")
    color_fin = "#009933" if puerto_fin_valido and rango_valido else ("white" if texto_puerto_fin == "" else "#ff4d4d")

    entrada_puerto_inicio.config(bg=color_inicio)
    entrada_puerto_fin.config(bg=color_fin)

    actualizar_consulta_nmap()




def validar_puertos_especificos(event):
    texto_entrada = entrada_puertos_especificos.get().strip()
    puertos_validos = True
    puertos_introducidos = set()

    if texto_entrada:
        puertos_lista = [p.strip() for p in texto_entrada.split(',') if p.strip()]  # Elimina espacios en blanco y elementos vacíos

        for puerto in puertos_lista:
            try:
                valor = int(puerto)
                if valor in puertos_introducidos:
                    puertos_validos = False
                    break
                elif not (1 <= valor <= 65535):
                    puertos_validos = False
                    break
                puertos_introducidos.add(valor)
            except ValueError:
                puertos_validos = False
                break
    else:
        puertos_validos = False

    # Establecer el color de fondo según si la entrada está vacía o no
    entrada_puertos_especificos.config(bg="white" if texto_entrada == "" else ("#009933" if puertos_validos else "#ff4d4d"))

    actualizar_consulta_nmap()




# ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Visual Nmap v1.3 - Generador de consultas Nmap")
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
menu_ayuda.add_command(label="Sobre el autor", command=mostrar_sobre_el_autor)
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

# Configurar grid en marco_derecho
marco_derecho.grid_columnconfigure(0, weight=1)
marco_derecho.grid_rowconfigure(0, weight=1)  # Asignar más peso a la sección de resultados
marco_derecho.grid_rowconfigure(1, weight=0)  # Menos peso a la sección de exportación

# Sección resultado
seccion_resultado_consulta = tk.LabelFrame(marco_derecho, padx=10, pady=10, text="Resultado de la consulta")
seccion_resultado_consulta.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Cuadro de texto para los resultados de nmap
resultado_nmap = tk.Text(seccion_resultado_consulta, bg="black")
resultado_nmap.pack(fill=tk.BOTH, expand=True)

# Sección salida de resultados
seccion_exportar_resultados = tk.LabelFrame(marco_derecho, padx=10, pady=10, text="Exportar resultado")
seccion_exportar_resultados.grid(row=1, column=0, sticky="ew", padx=10, pady=10)


# Configurar el grid de seccion_exportar_resultados para que expanda el contenedor principal solo horizontalmente
seccion_exportar_resultados.grid_rowconfigure(0, weight=0)
seccion_exportar_resultados.grid_columnconfigure(0, weight=1)

# Frame principal para entrada de texto y checkbuttons
contenedor_principal_exportar = tk.Frame(seccion_exportar_resultados)
contenedor_principal_exportar.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

# El resto del código para los checkbuttons y la entrada de texto permanece igual


# Sub-Frame para la entrada de texto y su label
marco_entrada_texto_nombre_salida_archivo = tk.Frame(contenedor_principal_exportar)
marco_entrada_texto_nombre_salida_archivo.pack(side=tk.LEFT, padx=5, pady=5)

label_nombre_archivo = tk.Label(marco_entrada_texto_nombre_salida_archivo, text="Nombre de archivo")
label_nombre_archivo.pack()

entrada_nombre_archivo = tk.Entry(marco_entrada_texto_nombre_salida_archivo)
entrada_nombre_archivo.pack()

# Sub-Frame para los checkbuttons
contenedor_checkbuttons_exportar_resultados = tk.Frame(contenedor_principal_exportar)
contenedor_checkbuttons_exportar_resultados.pack(side=tk.LEFT, padx=5, pady=5)

# Checkbuttons
check_normal = tk.Checkbutton(contenedor_checkbuttons_exportar_resultados, text="Normal")
check_normal.grid(row=0, column=0, sticky="w")

check_xml = tk.Checkbutton(contenedor_checkbuttons_exportar_resultados, text="-oX --> XML")
check_xml.grid(row=0, column=1, sticky="w")

check_grepable = tk.Checkbutton(contenedor_checkbuttons_exportar_resultados, text="-oG --> Greppable")
check_grepable.grid(row=1, column=0, sticky="w")

check_todos_formatos = tk.Checkbutton(contenedor_checkbuttons_exportar_resultados, text="-oA --> Todos los formatos")
check_todos_formatos.grid(row=1, column=1, sticky="w")




# Contenedor izquierdo
marco_izquierdo = tk.Frame(ventana_principal)
marco_izquierdo.pack(side=tk.LEFT, fill=tk.BOTH)

# etiqueta entrada ip o red
etiqueta_casilla_ip = tk.Label(marco_izquierdo, text="Introduce IP, rango o red")
etiqueta_casilla_ip.pack()

# Casilla de entrada para introducir IP o red
entrada_texto_ip = tk.Entry(marco_izquierdo, width=50, fg="white")
entrada_texto_ip.pack()
entrada_texto_ip.bind('<KeyRelease>', lambda event: actualizar_consulta_nmap())

# Sección consulta generada
seccion_consulta_generada = tk.LabelFrame(marco_izquierdo, text="Consulta generada para Nmap v7.94 ")
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
tab_evasion = ttk.Frame(notebook)
tab_scripts = ttk.Frame(notebook)
tab_otras_opciones = ttk.Frame(notebook)

# Añadir pestañas al notebook
notebook.add(tab_descubrimiento_red, text="Descubrimiento de Red")
notebook.add(tab_tecnica_escaneo, text="Ténica de Escaneo")
notebook.add(tab_opciones_servicios_y_version, text="Servicios y versiones")
notebook.add(tab_puertos, text="Puertos")
notebook.add(tab_evasion, text="Evasión")
notebook.add(tab_scripts, text="Scripts")
notebook.add(tab_otras_opciones, text="Otras Opciones")

# Suponiendo que 'notebook' es tu ttk.Notebook y 'tab_x' son las pestañas que quieres deshabilitar
notebook.tab(tab_evasion, state='disabled')
notebook.tab(tab_scripts, state='disabled')
notebook.tab(tab_otras_opciones, state='disabled')



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

    descripcion_descubrimiento_red = tk.Label(contenedor_opciones_descubrimiento_red, text=f"--> {descripcion_tipos_descubrimiento}", anchor="w", justify="left")
    descripcion_descubrimiento_red.pack(side=tk.LEFT, fill="x")

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
    "-F": "escanea los 100 primeros puertos",
    "-T": "Timing (velocidad del escaneo)"
}

contenedor_servicios_y_versiones = tk.Frame(tab_opciones_servicios_y_version, padx=3, pady=3)
contenedor_servicios_y_versiones.pack(anchor=tk.W)

# Variable de control para cada Checkbutton
var_sV = tk.IntVar(value=0)
var_A = tk.IntVar(value=0)
var_O = tk.IntVar(value=0)

# Crear Checkbutton y Label para -sV
contenedor_sV = tk.Frame(contenedor_servicios_y_versiones, padx=3, pady=3)
contenedor_sV.pack(fill=tk.X)
check_sV = tk.Checkbutton(contenedor_sV, text="-sV", variable=var_sV, command=actualizar_consulta_nmap)
check_sV.pack(side=tk.LEFT)
label_sV = tk.Label(contenedor_sV, text=f"--> {opciones_servicios_y_versiones['-sV']}")
label_sV.pack(side=tk.LEFT)

# Crear una variable de control para el nivel de intensidad
var_nivel_intensidad = tk.IntVar(value=0)

# Crear un Scale (deslizador) para el nivel de intensidad
scale_nivel_intensidad = tk.Scale(contenedor_sV, from_=0, to=9, orient=tk.HORIZONTAL, variable=var_nivel_intensidad, command=on_scale_movido)
scale_nivel_intensidad.pack(side=tk.LEFT)
manejar_estado_nivel_intensidad()

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




# Sección Puertos
# Diccionario con las opciones y descripciones
port_options = {
    "-p": "puerto único:",
    "-p rango": "rango de puertos:",
    "-p específicos": "puertos específicos separados por comas:",
    "-F": "escanea los 1000 primeros puertos",
    "-p-": "todos los puertos"
}

# Variable para guardar la opción seleccionada en la pestaña de Puertos
opcion_seleccionada_puertos = tk.StringVar(value="")

# Crear botones radiales, etiquetas y entradas de texto para puertos
for clave, descripcion in port_options.items():
    contenedor_puertos = tk.Frame(tab_puertos, padx=3, pady=3)
    contenedor_puertos.pack(anchor=tk.W)

    # Crear y añadir el Radiobutton
    rb = tk.Radiobutton(contenedor_puertos, text=clave, variable=opcion_seleccionada_puertos, value=clave, command=actualizar_consulta_nmap)
    rb.pack(side=tk.LEFT)

    # Crear y añadir la etiqueta después del Radiobutton
    etiqueta = tk.Label(contenedor_puertos, text=f"--> {descripcion}")
    etiqueta.pack(side=tk.LEFT)

    # Añadir entradas de texto específicas según la clave
    if clave == "-p":
        entrada_puerto = tk.Entry(contenedor_puertos, width=10)
        entrada_puerto.pack(side=tk.LEFT)
        entrada_puerto.bind('<KeyRelease>', validar_puerto_unico)

    elif clave == "-p rango":
        entrada_puerto_inicio = tk.Entry(contenedor_puertos, width=5)
        entrada_puerto_inicio.pack(side=tk.LEFT)
        entrada_puerto_inicio.bind('<KeyRelease>', validar_rango_puertos)

        tk.Label(contenedor_puertos, text="-").pack(side=tk.LEFT)

        entrada_puerto_fin = tk.Entry(contenedor_puertos, width=5)
        entrada_puerto_fin.pack(side=tk.LEFT)
        entrada_puerto_fin.bind('<KeyRelease>', validar_rango_puertos)

    elif clave == "-p específicos":
        entrada_puertos_especificos = tk.Entry(contenedor_puertos, width=30)
        entrada_puertos_especificos.pack(side=tk.LEFT)
        entrada_puertos_especificos.bind('<KeyRelease>', validar_puertos_especificos)

opcion_seleccionada_puertos.set(None)  # Establecer una opción por defecto



var_T = tk.IntVar(value=0)

# Diccionario con opciones y descripciones para Evasión
opciones_evasion = {
    "-T": "Timing (velocidad del escaneo)",
    "-f": "Utilizar técnicas de fragmentación",
    "--mtu": "Especificar el MTU",
    "-D": "Usar hosts señuelo",
    "-S": "Usar una dirección IP de origen falsa",
    "--proxies": "Utilizar proxies",
    "--data-length": "Añadir datos aleatorios a los paquetes enviados"
}



var_f = tk.IntVar(value=0)

# Crear Checkbuttons y Labels para Evasión
# Crear Checkbutton y Label para -f
contenedor_f = tk.Frame(tab_evasion, padx=3, pady=3)
contenedor_f.pack(fill=tk.X)
check_f = tk.Checkbutton(contenedor_f, text="-f", variable=var_f, command=actualizar_consulta_nmap)
check_f.pack(side=tk.LEFT)
label_f = tk.Label(contenedor_f, text=f"--> {opciones_evasion['-f']}")
label_f.pack(side=tk.LEFT)

# Crear Checkbutton y Label para -T
contenedor_T = tk.Frame(tab_evasion, padx=3, pady=3)
contenedor_T.pack(fill=tk.X)
check_T = tk.Checkbutton(contenedor_T, text="-T", variable=var_T, command=actualizar_consulta_nmap)
check_T.pack(side=tk.LEFT)
label_T = tk.Label(contenedor_T, text=f"--> {opciones_evasion['-T']}")
label_T.pack(side=tk.LEFT)


# Diccionario con opciones y descripciones para Scripts
opciones_scripts = {
    "-sC": "Ejecutar scripts por defecto"
}

# Crear Checkbuttons y Labels para Scripts
for comando, descripcion in opciones_scripts.items():
    contenedor = tk.Frame(tab_scripts, padx=3, pady=3)
    contenedor.pack(fill=tk.X)

    var = tk.IntVar(value=0)
    check = tk.Checkbutton(contenedor, text=comando, variable=var)
    check.pack(side=tk.LEFT)

    label = tk.Label(contenedor, text=f"--> {descripcion}")
    label.pack(side=tk.LEFT)




# Diccionario con opciones y descripciones para Otras Opciones
opciones_otras = {
    "-v": "Nivel de verbosidad 1",
    "-vv": "Nivel de verbosidad 2"
}

# Crear Checkbuttons y Labels para Otras Opciones
for comando, descripcion in opciones_otras.items():
    contenedor = tk.Frame(tab_otras_opciones, padx=3, pady=3)
    contenedor.pack(fill=tk.X)

    var = tk.IntVar(value=0)
    check = tk.Checkbutton(contenedor, text=comando, variable=var)
    check.pack(side=tk.LEFT)

    label = tk.Label(contenedor, text=f"--> {descripcion}")
    label.pack(side=tk.LEFT)




# Ejecución de la ventana principal
ventana_principal.mainloop()