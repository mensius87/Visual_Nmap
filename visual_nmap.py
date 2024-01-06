import tkinter
import tkinter as tk
from tkinter import ttk, Menu, messagebox, font
import os, sys, json, ipaddress, pyperclip, platform, subprocess, re, datetime

def mostrar_sobre_el_autor():
    ventana_sobre_autor = tk.Toplevel(pady=10)
    ventana_sobre_autor.title("Sobre el Autor")
    ventana_sobre_autor.geometry("550x335")  # Ajusta el tamaño según tus necesidades
    ventana_sobre_autor.config(bg="#333333")

    def abrir_enlace():
        import webbrowser
        webbrowser.open("https://github.com/mensius87")

    # Cargar y mostrar la imagen del icono
    ruta_imagen_icono = os.path.join('images', 'Visual_Nmap_icono.png')
    imagen_icono = tk.PhotoImage(file=ruta_imagen_icono)
    label_imagen_icono = tk.Label(ventana_sobre_autor, image=imagen_icono, bg="#333333")
    label_imagen_icono.image = imagen_icono  # Guarda una referencia de la imagen
    label_imagen_icono.pack()

    fuente_grande = font.Font(family="Helvetica", size=14)
    enlace_label = tk.Label(ventana_sobre_autor, text="Programa desarrollado por mensius87. Licencia MIT. Mis proyectos:" , bg="#333333", fg="white")
    enlace_label.pack()

    # Crear un label con el enlace
    enlace_label = tk.Label(ventana_sobre_autor, text="https://github.com/mensius87", fg="#ADD8E6", cursor="hand2", bg="#333333", font=fuente_grande)
    enlace_label.pack()

    # Asociar la función abrir_enlace al clic en el label
    enlace_label.bind("<Button-1>", lambda event: abrir_enlace())

    # Cargar y mostrar la imagen del banner
    ruta_imagen_banner = os.path.join('images', 'banner_autor.png')
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
    sV_valor_intensidad.config(bg="#dcdad5")
    scale_nivel_intensidad.config(bg="#dcdad5")

    seccion_resultado_consulta.config(bg=colores_modo_oscuro["fondo"], fg=colores_modo_oscuro["texto"])
    seccion_exportar_resultados.config(bg=colores_modo_oscuro["fondo"], fg=colores_modo_oscuro["texto"])
    seccion_consulta_generada.config(bg=colores_modo_oscuro["fondo"], fg=colores_modo_oscuro["texto"])
    seccion_encabezado_opciones_avanzadas.config(bg=colores_modo_oscuro["fondo"], fg=colores_modo_oscuro["texto"])
    seccion_historial_consultas.config(bg="#dcdad5")

    contenedor_general_consulta_generada.config(bg="#dcdad5")
    contenedor_botones.config(bg="#dcdad5")
    contenedor_A.config(bg="#dcdad5")
    contenedor_f.config(bg="#dcdad5")
    contenedor_O.config(bg="#dcdad5")
    contenedor_sV.config(bg="#dcdad5")
    contenedor_T.config(bg="#dcdad5")
    contenedor_checkbuttons_exportar_resultados.config(bg="#dcdad5")
    contenedor_principal_exportar.config(bg="#dcdad5")
    contenedor_script_especifico.config(bg="#dcdad5")
    contenedor_script_por_defecto.config(bg="#dcdad5")
    contenedor_otras_opciones.config(bg="#dcdad5")
    contenedor_general_historico.config(bg="#dcdad5")
    contenedor_tabla_historico.config(bg="#dcdad5")

    # Cambiar los estilos para la sección de historial de consultas
    seccion_historial_consultas.config(bg=colores_modo_oscuro["fondo"], fg=colores_modo_oscuro["texto"])
    contenedor_general_historico.config(bg=colores_modo_oscuro["fondo"])
    contenedor_tabla_historico.config(bg=colores_modo_oscuro["fondo"])

    # Cambiar el estilo del Treeview (historial_consultas)
    style = ttk.Style()
    style.configure("Treeview", background=colores_modo_oscuro["fondo"], fieldbackground=colores_modo_oscuro["fondo"], foreground=colores_modo_oscuro["texto"])
    style.configure("Treeview.Heading", background=colores_modo_oscuro["fondo"], foreground=colores_modo_oscuro["texto"])

    # Cambiar el color del fondo y del texto de los elementos seleccionados
    style.map("Treeview", background=[('selected', '#0078D7')], foreground=[('selected', 'white')])

    check_verbosidad_1.config(bg="#dcdad5")
    check_verbosidad_2.config(bg="#dcdad5")
    check_normal.config(bg="#dcdad5")
    check_todos_formatos.config(bg="#dcdad5")
    check_grepable.config(bg="#dcdad5")
    check_xml.config(bg="#dcdad5")

    label_descripcion_script.config(bg="#dcdad5")
    label_script.config(bg="#dcdad5")

    label_nombre_archivo.config(bg="#dcdad5")

    # Cambiar el estilo de los widgets en cada pestaña
    for tab in [tab_descubrimiento_red, tab_tecnica_escaneo, tab_opciones_servicios_y_version, tab_puertos, tab_evasion, tab_scripts, tab_otras_opciones]:
        for widget in tab.winfo_children():
            widget.config(bg="#dcdad5")
            for child in widget.winfo_children():
                if isinstance(child, (tk.Radiobutton, tk.Checkbutton, tk.Label, tk.Scale)):
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
    check_sC.config(bg="#dcdad5")
    check_script_especifico.config(bg="#dcdad5")
    check_verbosidad_1.config(bg="#dcdad5")
    check_verbosidad_2.config(bg="#dcdad5")
    scale_nivel_depuracion.config(bg="#dcdad5")

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


def es_dominio_valido(dominio):
    patron_dominio_con_www = re.compile(r'^www\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.[a-zA-Z]{2,6}$')
    patron_dominio_sin_www = re.compile(r'^[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.[a-zA-Z]{2,6}$')

    if dominio.startswith('www.'):
        return bool(patron_dominio_con_www.match(dominio))
    else:
        return bool(patron_dominio_sin_www.match(dominio))


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


def es_direccion_o_red_o_dominio_valido(direccion):
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
            if es_rango_ip_valido(direccion):
                return True
            else:
                return es_dominio_valido(direccion)


def manejar_incompatibilidad_A_O_sV():
    # Deshabilitar -O y -sV si -A está seleccionado
    if var_A.get() == 1:
        check_O.config(state=tk.DISABLED)
        check_sV.config(state=tk.DISABLED)
        var_O.set(0)
        var_sV.set(0)
    else:
        # Habilitar -O y -sV sólo si ellos mismos no están seleccionados
        if var_O.get() == 0:
            check_O.config(state=tk.NORMAL)
        if var_sV.get() == 0:
            check_sV.config(state=tk.NORMAL)

    # Deshabilitar -A si -O o -sV están seleccionados
    if var_O.get() == 1 or var_sV.get() == 1:
        check_A.config(state=tk.DISABLED)
        var_A.set(0)
    else:
        # Habilitar -A sólo si -A no está seleccionado
        if var_A.get() == 0:
            check_A.config(state=tk.NORMAL)


sV_escala_usada = False
def manejar_estado_nivel_intensidad_sV():
    global sV_escala_usada  # Asegúrate de utilizar la variable global

    if var_sV.get() == 1:
        scale_nivel_intensidad.config(state=tk.NORMAL)
        # No cambiar sV_escala_usada aquí para mantener su estado anterior
    else:
        scale_nivel_intensidad.config(state=tk.DISABLED)
        sV_escala_usada = False  # Restablecer la bandera cuando -sV se desactiva


def si_escala_movida_sV(val):
    global sV_escala_usada
    sV_escala_usada = True  # Establecer la bandera en True cuando se mueve la escala

    # Actualizar el valor de intensidad solo si la escala ha sido usada
    if sV_escala_usada:
        sV_valor_intensidad.config(text=str(val))
    actualizar_consulta_nmap()


T_escala_usada = False
def manejar_estado_nivel_intensidad_T():

    if var_T.get() == 1:
        scale_nivel_intensidad_T.config(state=tk.NORMAL)
    else:
        scale_nivel_intensidad_T.config(state=tk.DISABLED)


def si_escala_movida_T(val):
    global T_escala_usada
    if not T_escala_usada:
        T_escala_usada = True
    if var_T.get() == 0:
        T_escala_usada = False

    T_valor_intensidad.config(text=str(val))
    actualizar_consulta_nmap()


depuracion_escala_usada = False
def manejar_estado_nivel_intensidad_d():

    if var_T.get() == 1:
        scale_nivel_depuracion.config(state=tk.NORMAL)
    else:
        scale_nivel_depuracion.config(state=tk.DISABLED)


depuracion_valor_intensidad = None

def si_escaca_movida_d(val):
    global depuracion_escala_usada
    if not depuracion_escala_usada:
        depuracion_escala_usada = True
    if var_depuracion.get() == 0:
        depuracion_escala_usada = False

    # Actualizar el texto del label con el valor de la escala
    depuracion_valor_intensidad.config(text=str(val))
    actualizar_consulta_nmap()



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
    entrada_nombre_archivo.delete("0", "end")
    entrada_texto_ip.delete("0", "end")
    entrada_texto_ip.config(bg="white")
    var_sV.set(0)
    var_A.set(0)
    var_O.set(0)
    var_f.set(0)
    var_T.set(0)
    opcion_seleccionada_puertos.set(0)
    var_script_seleccionado.set("")
    var_script_especifico.set(0)
    var_sC.set(0)
    check_script_especifico.config(state=tk.NORMAL)
    check_sC.config(state=tk.NORMAL)
    combobox_scripts.config(state=tk.NORMAL)
    var_verbosidad_1.set(0)
    var_verbosidad_2.set(0)
    var_depuracion.set(0)
    var_ipv6.set(0)
    check_verbosidad_1.config(state=tk.NORMAL)
    check_verbosidad_2.config(state=tk.NORMAL)
    check_grepable.config(state=tk.NORMAL)
    check_normal.config(state=tk.NORMAL)
    check_todos_formatos.config(state=tk.NORMAL)
    check_xml.config(state=tk.NORMAL)
    var_grepable.set(0)
    var_normal.set(0)
    var_xml.set(0)
    var_todos_formatos.set(0)

    actualizar_consulta_nmap()


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


contador_consultas = 0

def ejecutar_escaneo_nmap():
    global contador_consultas  # Referencia a la variable global para el contador de consultas

    # Comando base de Nmap
    comando_nmap_base = "nmap"
    if platform.system() == "Windows":
        comando_nmap_base = "C:\\Nmap\\nmap.exe"

    # Obtener la consulta del cuadro de texto
    consulta_nmap = cuadro_texto_consulta_generada.get('1.0', tk.END).strip()

    # Verificar si la consulta está vacía
    if not consulta_nmap:
        messagebox.showinfo("Información", "Introduce un comando de Nmap válido.")
        return

    # Construir el comando completo
    comando_nmap = f" {consulta_nmap}"

    # Obtener la fecha y hora actual
    fecha_hora_actual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Incrementar el contador de consultas para asignar un nuevo ID
    contador_consultas += 1

    try:
        # Ejecutar el comando Nmap
        resultado = subprocess.check_output(comando_nmap, shell=True, text=True, stderr=subprocess.STDOUT)
        resultado_nmap.config(state=tk.NORMAL)
        resultado_nmap.delete('1.0', tk.END)
        resultado_nmap.insert('1.0', resultado)
        resultado_nmap.config(state=tk.DISABLED, fg='green')

        # Agregar la consulta y el resultado al historial
        historial_consultas.insert("", "end", values=(contador_consultas, comando_nmap, fecha_hora_actual))
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Hubo un error al ejecutar Nmap:\n{e.output}")

# Resto del código, incluyendo la definición de las variables y widgets de Tkinter...




'''
def ejecutar_escaneo_nmap():
    comando_nmap = f"nmap {cuadro_texto_consulta_generada.get('1.0', tk.END).strip()}"

    print("Ejecutando comando:", comando_nmap)  # Imprime para depurar

    if comando_nmap.strip():
        try:
            resultado = subprocess.check_output(comando_nmap, shell=True, text=True, stderr=subprocess.STDOUT)
            resultado_nmap.config(state=tk.NORMAL)
            resultado_nmap.delete('1.0', tk.END)
            resultado_nmap.insert('1.0', resultado)
            resultado_nmap.config(state=tk.DISABLED, fg='green')
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Hubo un error al ejecutar Nmap:\n{e.output}")
    else:
        messagebox.showinfo("Información", "Introduce un comando de Nmap válido.")
'''


def actualizar_consulta_nmap(*args):
    cuadro_texto_consulta_generada.config(state=tk.NORMAL)
    cuadro_texto_consulta_generada.delete('1.0', tk.END)

    ip_valor = entrada_texto_ip.get()

    # Verifica si la dirección IP o red es válida
    if not es_direccion_o_red_o_dominio_valido(ip_valor):
        entrada_texto_ip.config(bg='#ff4d4d')  # Fondo rojo para entrada inválida

    else:
        entrada_texto_ip.config(bg='#009933')  # Fondo verde para entrada válida

    if ip_valor == "" or ip_valor == None:
        entrada_texto_ip.config(bg='white')

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
    manejar_estado_nivel_intensidad_sV()
    nivel_instensidad_sV = var_nivel_intensidad.get()

    if var_sV.get() == 1:
        consulta += " -sV"
        if sV_escala_usada:
            consulta += f" --version-intensity {var_nivel_intensidad.get()}"

    if var_A.get() == 1:
        consulta += " -A"
    if var_O.get() == 1:
        consulta += " -O"
    if var_f.get() == 1:
        consulta += " -f"
    if var_T.get() == 1:
        consulta += " -T"
    if var_T.get() == 1:
        nivel_intensidad_T = var_nivel_intensidad_T.get()
        consulta += f"{nivel_intensidad_T}"
    # Añadir la opción --mtu si está seleccionada
    if var_mtu.get() == 1:
        valor_mtu = scale_mtu.get()  # Obtener el valor del Scale
        consulta += f" --mtu {valor_mtu}"
    if var_D.get() == 1:
        consulta += " -D"
    if var_S.get() == 1:
        consulta += " -S"
    if var_proxies.get() == 1:
        consulta += " --proxies"
    if var_data_length.get() == 1:
        consulta += " --data-length"

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

    if var_sC.get() == 1:
        consulta += " -sC"
    elif var_script_especifico.get() == 1 and var_script_seleccionado.get():
        consulta += f" --script={var_script_seleccionado.get().rstrip()}"

    if var_ipv6.get() == 1:
        consulta += " -6"

    # Agregar opciones de formato de salida
    nombre_archivo = entrada_nombre_archivo.get().strip()
    if nombre_archivo:
        if var_normal.get() == 1:
            consulta += f" -oN {nombre_archivo}.nmap"
        if var_xml.get() == 1:
            consulta += f" -oX {nombre_archivo}.xml"
        if var_grepable.get() == 1:
            consulta += f" -oG {nombre_archivo}.gnmap"
        if var_todos_formatos.get() == 1:
            consulta += f" -oA {nombre_archivo}"

    consulta += f" {ip_valor}"

    # Agregar opciones de verbosidad o depuración si están seleccionadas
    if var_verbosidad_1.get() == 1:
        consulta += " -v"
    elif var_verbosidad_2.get() == 1:
        consulta += " -vv"
    if var_depuracion.get() == 1:
        nivel_depuracion = var_nivel_depuracion.get()
        consulta += f" -d{nivel_depuracion}"


    cuadro_texto_consulta_generada.insert(tk.END, consulta)
    cuadro_texto_consulta_generada.config(state=tk.DISABLED)


# ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Visual Nmap v1.6 - Generador de consultas Nmap")
ventana_principal.geometry("1500x665")
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




def validar_nombre_archivo(event):
    nombre_archivo = entrada_nombre_archivo.get().strip()
    patron = re.compile(r'^[a-zA-Z0-9_.-]+$')  # Expresión regular para validar el nombre del archivo

    if patron.match(nombre_archivo):
        entrada_nombre_archivo.config(bg='#009933')  # Fondo blanco para entrada válida o vacía
    else:
        entrada_nombre_archivo.config(bg='#ff4d4d')  # Fondo rojo para entrada inválida
    if nombre_archivo == "":
        entrada_nombre_archivo.config(bg='white')


    actualizar_consulta_nmap()  # Actualizar la consulta de Nmap

def actualizar_formato_salida():
    # Comprobar si algún check de formato de salida está seleccionado
    algun_formato_seleccionado = var_normal.get() == 1 or var_xml.get() == 1 or var_grepable.get() == 1 or var_todos_formatos.get() == 1

    # Habilitar o deshabilitar la entrada del nombre del archivo
    if algun_formato_seleccionado:
        entrada_nombre_archivo.config(state=tk.NORMAL)
    else:
        entrada_nombre_archivo.config(state=tk.DISABLED)
        entrada_nombre_archivo.delete(0, tk.END)  # Opcional: Limpiar la entrada si se deseleccionan todos los formatos

    # Si se selecciona -oA, desactiva los demás formatos
    if var_todos_formatos.get() == 1:
        var_normal.set(0)
        var_xml.set(0)
        var_grepable.set(0)
        check_normal.config(state=tk.DISABLED)
        check_xml.config(state=tk.DISABLED)
        check_grepable.config(state=tk.DISABLED)
    else:
        check_normal.config(state=tk.NORMAL)
        check_xml.config(state=tk.NORMAL)
        check_grepable.config(state=tk.NORMAL)

        # Desactivar -oA si se selecciona otro formato
        if algun_formato_seleccionado:
            var_todos_formatos.set(0)
            check_todos_formatos.config(state=tk.DISABLED)
        else:
            check_todos_formatos.config(state=tk.NORMAL)

    actualizar_consulta_nmap()


var_normal = tk.IntVar(value=0)
var_xml = tk.IntVar(value=0)
var_grepable = tk.IntVar(value=0)
var_todos_formatos = tk.IntVar(value=0)

# Sección salida de resultados
seccion_exportar_resultados = tk.LabelFrame(marco_derecho, padx=10, pady=10, text="Exportar resultado")
seccion_exportar_resultados.grid(row=1, column=0, sticky="ew", padx=10, pady=10)

# Configurar el grid de seccion_exportar_resultados para que expanda el contenedor principal solo horizontalmente
seccion_exportar_resultados.grid_rowconfigure(0, weight=0)
seccion_exportar_resultados.grid_columnconfigure(0, weight=1)

# Frame principal para entrada de texto y checkbuttons
contenedor_principal_exportar = tk.Frame(seccion_exportar_resultados)
contenedor_principal_exportar.grid(row=0, column=0, sticky="ew", padx=5, pady=5)


# Sub-Frame para la entrada de texto y su label
marco_entrada_texto_nombre_salida_archivo = tk.Frame(contenedor_principal_exportar)
marco_entrada_texto_nombre_salida_archivo.pack(side=tk.LEFT, padx=5, pady=5)

label_nombre_archivo = tk.Label(marco_entrada_texto_nombre_salida_archivo, text="Nombre de archivo")
label_nombre_archivo.pack()

entrada_nombre_archivo = tk.Entry(marco_entrada_texto_nombre_salida_archivo, state=tk.DISABLED)
entrada_nombre_archivo.pack()
entrada_nombre_archivo.bind('<KeyRelease>', lambda event: [actualizar_consulta_nmap(), validar_nombre_archivo(event)])

# Sub-Frame para los checkbuttons
contenedor_checkbuttons_exportar_resultados = tk.Frame(contenedor_principal_exportar)
contenedor_checkbuttons_exportar_resultados.pack(side=tk.LEFT, padx=5, pady=5)


# Checkbuttons
check_normal = tk.Checkbutton(contenedor_checkbuttons_exportar_resultados, text="Normal", variable=var_normal, command=actualizar_formato_salida)
check_normal.grid(row=0, column=0, sticky="w")

check_xml = tk.Checkbutton(contenedor_checkbuttons_exportar_resultados, text="-oX --> XML", variable=var_xml, command=actualizar_formato_salida)
check_xml.grid(row=0, column=1, sticky="w")

check_grepable = tk.Checkbutton(contenedor_checkbuttons_exportar_resultados, text="-oG --> Greppable", variable=var_grepable, command=actualizar_formato_salida)
check_grepable.grid(row=1, column=0, sticky="w")

check_todos_formatos = tk.Checkbutton(contenedor_checkbuttons_exportar_resultados, text="-oA --> Todos los formatos", variable=var_todos_formatos, command=actualizar_formato_salida)
check_todos_formatos.grid(row=1, column=1, sticky="w")






# Contenedor izquierdo
marco_izquierdo = tk.Frame(ventana_principal)
marco_izquierdo.pack(side=tk.LEFT, fill=tk.BOTH)

# etiqueta entrada ip o red
etiqueta_casilla_ip = tk.Label(marco_izquierdo, text="Introduce IP, rango, red o dominio")
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
ruta_icono_copiar = os.path.join('images', 'duplicar.png')
icono_copiar = tk.PhotoImage(file=ruta_icono_copiar)
boton_copiar = tk.Button(contenedor_botones, text="Copiar", bg="blue", image=icono_copiar, command=copiar_al_portapapeles)
boton_copiar.pack(side=tk.RIGHT, padx=5)

# Botón limpiar
ruta_icono_limpiar_consulta = os.path.join('images', 'limpiar.png')
icono_limpiar_consulta = tk.PhotoImage(file=ruta_icono_limpiar_consulta)
boton_limpiar_consulta = tk.Button(contenedor_botones, text="Limpiar", bg="red", image=icono_limpiar_consulta, command=limpiar_texto_consulta)
boton_limpiar_consulta.pack(side=tk.RIGHT, padx=5)

# Botón escanear
boton_escanear = tk.Button(contenedor_botones, text="ESCANEAR", bg="green", fg="white", command=ejecutar_escaneo_nmap)
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




# Diccionario con opciones y sus descripciones
opciones_descubrimiento_red = {
    "-sL": "List Scan: enumera direcciones IP sin generar tráfico de red.",
    "-sn": "Ping Scan: identifica hosts activos mediante pings de red.",
    "-Pn": "No Ping: presume que todos los hosts están activos, omitiendo el descubrimiento previo.",
    "-PS": "TCP SYN Ping Scan: detecta hosts activos con pings SYN en TCP.",
    "-PA": "TCP ACK Ping Scan: utiliza pings ACK en TCP para identificar hosts en línea.",
    "-PU": "UDP Ping Scan: descubre hosts activos con pings UDP.",
    "-PR": "ARP Ping Scan: localiza hosts activos en redes locales usando ARP.",
    "-n": "No DNS Resolution: omite la resolución de DNS para acelerar el escaneo."
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
    "-sS": "TCP SYN Scan: verifica puertos abiertos simulando el inicio de una conexión TCP pero sin completar la conexión",
    "-sT": "TCP Connect Scan: comprueba la apertura de puertos completando una conexión TCP",
    "-sA": "TCP ACK Scan: usa paquetes ACK para determinar si los puertos están filtrados o no",
    "-sU": "UDP Scan: examina puertos UDP enviando paquetes UDP para ver si responden",
    "-Sf": "FIN Scan: envía paquetes FIN a puertos para identificar cuáles no están filtrados",
    "-sX": "Xmas Scan: usa paquetes con combinaciones inusuales de flags para analizar puertos",
    "-Sp": "SCTP INIT Scan: inspecciona puertos SCTP mediante mensajes de inicio SCTP",
    "-sN": "Null Scan: envía paquetes sin ningún flag activado para observar reacciones de puertos",
    "-sL": "List Scan: enumera IPs objetivo sin enviar tráfico activo a los puertos"
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
    "-sV": "detección de versiones de servicios. Se puede especificar la intensidad de 0 (ligero) a 9 (agresivo)",
    "-O": "detección de sistema operativo: activa la identificación del sistema operativo del objetivo",
    "-A": "detección avanzada: combina detección de SO, versiones de servicios y script scanning"
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
check_sV = tk.Checkbutton(contenedor_sV, text="-sV", variable=var_sV, command=lambda: [manejar_incompatibilidad_A_O_sV(), actualizar_consulta_nmap()])
check_sV.pack(side=tk.LEFT)
label_sV = tk.Label(contenedor_sV, text=f"--> {opciones_servicios_y_versiones['-sV']}")
label_sV.pack(side=tk.LEFT)

# Crear una variable de control para el nivel de intensidad
var_nivel_intensidad = tk.IntVar(value=0)

# Crear un Scale (deslizador) para el nivel de intensidad
scale_nivel_intensidad = tk.Scale(contenedor_sV, from_=0, to=9, showvalue= False, orient=tk.HORIZONTAL, variable=var_nivel_intensidad, command=si_escala_movida_sV)
scale_nivel_intensidad.pack(side=tk.LEFT)
manejar_estado_nivel_intensidad_sV()

sV_valor_intensidad = tk.Label(contenedor_sV, text="0")
sV_valor_intensidad.pack(side=tk.LEFT)


# Crear Checkbutton y Label para -A
contenedor_A = tk.Frame(contenedor_servicios_y_versiones, padx=3, pady=3)
contenedor_A.pack(fill=tk.X)
check_A = tk.Checkbutton(contenedor_A, text="-A", variable=var_A, command=lambda: [manejar_incompatibilidad_A_O_sV(), actualizar_consulta_nmap()])
check_A.pack(side=tk.LEFT)
label_A = tk.Label(contenedor_A, text=f"--> {opciones_servicios_y_versiones['-A']}")
label_A.pack(side=tk.LEFT)

# Crear Checkbutton y Label para -O
contenedor_O = tk.Frame(contenedor_servicios_y_versiones, padx=3, pady=3)
contenedor_O.pack(fill=tk.X)
check_O = tk.Checkbutton(contenedor_O, text="-O", variable=var_O, command=lambda: [manejar_incompatibilidad_A_O_sV(), actualizar_consulta_nmap()])
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
    "-p-": "escanea los 65535 puertos existentes"
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


# Sección evasión
var_T = tk.IntVar(value=0)


# Diccionario con opciones y descripciones para Evasión
opciones_evasion = {
    "-T": "ajusta la velocidad del escaneo. Un valor bajo es más sigiloso pero lento, un valor alto es más rápido pero más detectable.",
    "-f": "fragmenta los paquetes de red para intentar evadir detectores y firewalls.",
    "--mtu": "tamaño personalizado para los paquetes de red y evadir así filtros o redes con restricciones de tamaño de paquete.",
    "-D": "usa direcciones IP falsas como señuelos junto con tu dirección real para confundir y diluir los registros en los sistemas de seguridad.",
    "-S": "finge que los paquetes provienen de otra dirección IP, no de tu verdadera dirección IP.",
    "--proxies": "envía los paquetes a través de uno o más proxies para ocultar el origen real de los escaneos.",
    "--data-length": "añade datos aleatorios a los paquetes para cambiar su tamaño y apariencia ayudando a evadir algunos tipos de detección."
}
# Crear Checkbutton y Label para -T
contenedor_T = tk.Frame(tab_evasion, padx=3, pady=3)
contenedor_T.pack(fill=tk.X)
check_T = tk.Checkbutton(contenedor_T, text="-T", variable=var_T, command=actualizar_consulta_nmap)
check_T.pack(side=tk.LEFT)
check_T.config(command=lambda: [manejar_estado_nivel_intensidad_T(), actualizar_consulta_nmap()])
label_T = tk.Label(contenedor_T, text=f"--> {opciones_evasion['-T']}")
label_T.pack(side=tk.LEFT)

# Variable de control para el nivel de intensidad de -T
var_nivel_intensidad_T = tk.IntVar(value=0)

# Crear un Scale (deslizador) para el nivel de intensidad de -T
scale_nivel_intensidad_T = tk.Scale(contenedor_T, from_=0, to=5, showvalue=False, orient=tk.HORIZONTAL, variable=var_nivel_intensidad_T, command=si_escala_movida_T)
scale_nivel_intensidad_T.pack(side=tk.LEFT)
scale_nivel_intensidad_T.config(state=tk.DISABLED)

T_valor_intensidad = tk.Label(contenedor_T, text="0")
T_valor_intensidad.pack(side=tk.LEFT)

var_f = tk.IntVar(value=0)

# Crear Checkbuttons y Labels para Evasión
# Crear Checkbutton y Label para -f
contenedor_f = tk.Frame(tab_evasion, padx=3, pady=3)
contenedor_f.pack(fill=tk.X)
check_f = tk.Checkbutton(contenedor_f, text="-f", variable=var_f, command=actualizar_consulta_nmap)
check_f.pack(side=tk.LEFT)
label_f = tk.Label(contenedor_f, text=f"--> {opciones_evasion['-f']}")
label_f.pack(side=tk.LEFT)

# Crear el contenedor para la opción --mtu
contenedor_mtu = tk.Frame(tab_evasion, padx=3, pady=3)
contenedor_mtu.pack(fill=tk.X)

# Crear Checkbutton y Label para --mtu
var_mtu = tk.IntVar(value=0)
check_mtu = tk.Checkbutton(contenedor_mtu, text="--mtu", variable=var_mtu, command=actualizar_consulta_nmap)
check_mtu.pack(side=tk.LEFT)
label_mtu = tk.Label(contenedor_mtu, text=f"--> {opciones_evasion['--mtu']}")
label_mtu.pack(side=tk.LEFT)

# Crear un Scale (deslizador) para el valor de MTU
def ajustar_mtu(val):
    """ Ajusta el valor del MTU al múltiplo de 8 más cercano """
    mtu_valor_intensidad.config(text=str(val))
    actualizar_consulta_nmap()
    return int(val) // 8 * 8


scale_mtu = tk.Scale(contenedor_mtu, from_=8, to=1500, resolution=8, showvalue=0, orient=tk.HORIZONTAL, command=ajustar_mtu)
scale_mtu.pack(side=tk.LEFT)

mtu_valor_intensidad = tk.Label(contenedor_mtu, text="0")
mtu_valor_intensidad.pack(side=tk.LEFT)


# Crear Checkbutton y Label para -D (hosts señuelo)
var_D = tk.IntVar(value=0)
contenedor_D = tk.Frame(tab_evasion, padx=3, pady=3)
contenedor_D.pack(fill=tk.X)
check_D = tk.Checkbutton(contenedor_D, text="-D", variable=var_D, command=actualizar_consulta_nmap)
check_D.pack(side=tk.LEFT)
label_D = tk.Label(contenedor_D, text=f"--> {opciones_evasion['-D']}")
label_D.pack(side=tk.LEFT)

# Crear Checkbutton y Label para -S (dirección IP de origen falsa)
var_S = tk.IntVar(value=0)
contenedor_S = tk.Frame(tab_evasion, padx=3, pady=3)
contenedor_S.pack(fill=tk.X)
check_S = tk.Checkbutton(contenedor_S, text="-S", variable=var_S, command=actualizar_consulta_nmap)
check_S.pack(side=tk.LEFT)
label_S = tk.Label(contenedor_S, text=f"--> {opciones_evasion['-S']}")
label_S.pack(side=tk.LEFT)

# Crear Checkbutton y Label para --proxies (utilizar proxies)
var_proxies = tk.IntVar(value=0)
contenedor_proxies = tk.Frame(tab_evasion, padx=3, pady=3)
contenedor_proxies.pack(fill=tk.X)
check_proxies = tk.Checkbutton(contenedor_proxies, text="--proxies", variable=var_proxies, command=actualizar_consulta_nmap)
check_proxies.pack(side=tk.LEFT)
label_proxies = tk.Label(contenedor_proxies, text=f"--> {opciones_evasion['--proxies']}")
label_proxies.pack(side=tk.LEFT)

# Crear Checkbutton y Label para --data-length (añadir datos aleatorios)
var_data_length = tk.IntVar(value=0)
contenedor_data_length = tk.Frame(tab_evasion, padx=3, pady=3)
contenedor_data_length.pack(fill=tk.X)
check_data_length = tk.Checkbutton(contenedor_data_length, text="--data-length", variable=var_data_length, command=actualizar_consulta_nmap)
check_data_length.pack(side=tk.LEFT)
label_data_length = tk.Label(contenedor_data_length, text=f"--> {opciones_evasion['--data-length']}")
label_data_length.pack(side=tk.LEFT)



def actualizar_descripcion_script(event):
    script_seleccionado = var_script_seleccionado.get()
    descripcion = opciones_scripts.get(script_seleccionado, "")
    label_descripcion_script.config(text=descripcion)

    if combobox_scripts:
        var_script_especifico.set(1)

    actualizar_consulta_nmap()


# Función para manejar la selección de scripts
def seleccion_script(checkbutton_seleccionado):
    if checkbutton_seleccionado == check_sC:
        if var_sC.get() == 1:
            # Si -sC está seleccionado, deshabilita la selección de script específico
            check_script_especifico.config(state=tk.DISABLED)
            combobox_scripts.set('')
            label_descripcion_script.config(text='')
            combobox_scripts.config(state=tk.DISABLED)
        else:
            # Si -sC se deselecciona, habilita la selección de script específico
            check_script_especifico.config(state=tk.NORMAL)
            combobox_scripts.config(state=tk.NORMAL)

        actualizar_consulta_nmap()

    elif checkbutton_seleccionado == check_script_especifico:
        if var_script_especifico.get() == 1:
            # Si se selecciona un script específico, deshabilita -sC
            check_sC.config(state=tk.DISABLED)
        else:
            # Si se deselecciona un script específico, habilita -sC
            check_sC.config(state=tk.NORMAL)

        actualizar_consulta_nmap()


# Crear una variable de control para el Combobox
var_script_seleccionado = tk.StringVar()


# Diccionario con opciones y descripciones para Scripts
opciones_scripts = {
    "auth": "scripts relacionados con la autenticación",
    "broadcast": "descubre hosts no listados",
    "brute": "intenta adivinar contraseñas",
    "discovery": "recolecta información sobre los hosts",
    "dos": "prueba vulnerabilidades de denegación de servicio",
    "exploit": "intenta explotar vulnerabilidades conocidas",
    "external": "interactúa con servicios externos",
    "fuzzer": "prueba aplicaciones con entradas inesperadas",
    "intrusive": "scripts que podrían alertar a los admins de red",
    "malware": "busca indicadores de malware",
    "safe": "scripts que no son considerados intrusivos",
    "version":  "cripts que intentan determinar información de versión de los servicios",
    "vuln": "revisa vulnerabilidades conocidas"
}


# Contenedor para la opción -sC (Scripts por defecto)
contenedor_script_por_defecto = tk.Frame(tab_scripts)
contenedor_script_por_defecto.pack(fill=tk.X, padx=3, pady=3)

# Checkbutton para -sC
var_sC = tk.IntVar(value=0)
check_sC = tk.Checkbutton(contenedor_script_por_defecto, text="-sC (Scripts por defecto)", variable=var_sC, command=lambda: seleccion_script(check_sC))
check_sC.pack(side=tk.LEFT)

# Contenedor para la selección de script específico
contenedor_script_especifico = tk.Frame(tab_scripts)
contenedor_script_especifico.pack(fill=tk.X, padx=3, pady=3)

# Checkbutton para activar la selección de script específico
var_script_especifico = tk.IntVar(value=0)
check_script_especifico = tk.Checkbutton(contenedor_script_especifico, text="", variable=var_script_especifico, command=lambda: seleccion_script(check_script_especifico))
check_script_especifico.pack(side=tk.LEFT)

# Label y Combobox para scripts específicos
label_script = tk.Label(contenedor_script_especifico, text="Script específico:")
label_script.pack(side=tk.LEFT, padx=(5,0))

combobox_scripts = ttk.Combobox(contenedor_script_especifico, textvariable=var_script_seleccionado, values=list(opciones_scripts.keys()), state="readonly", width=20)
combobox_scripts.pack(side=tk.LEFT, padx=(5,0))
combobox_scripts.bind("<<ComboboxSelected>>", actualizar_descripcion_script)

# Label para mostrar la descripción del script seleccionado
label_descripcion_script = tk.Label(contenedor_script_especifico, text="")
label_descripcion_script.pack(side=tk.LEFT, padx=(5,0))




# Variables globales para las opciones
var_verbosidad_1 = tk.IntVar(value=0)
var_verbosidad_2 = tk.IntVar(value=0)
var_depuracion = tk.IntVar(value=0)
var_nivel_depuracion = tk.IntVar(value=0)  # Nivel de depuración
var_ipv6 = tk.IntVar(value=0)

# Función para manejar la exclusión mutua de -v, -vv y -d
def manejar_exclusion_mutua_verbosidad():
    if var_verbosidad_1.get() == 1:
        var_verbosidad_2.set(0)
        check_verbosidad_2.config(state=tk.DISABLED)
    else:
        check_verbosidad_2.config(state=tk.NORMAL)

    if var_verbosidad_2.get() == 1:
        var_verbosidad_1.set(0)
        check_verbosidad_1.config(state=tk.DISABLED)
    else:
        check_verbosidad_1.config(state=tk.NORMAL)

    # Habilitar o deshabilitar la escala de -d
    if var_depuracion.get() == 1:
        scale_nivel_depuracion.config(state=tk.NORMAL)
    else:
        scale_nivel_depuracion.config(state=tk.DISABLED)
        var_nivel_depuracion.set(0)  # Resetear el valor de la escala

    actualizar_consulta_nmap()

# Diccionario con opciones y descripciones para Otras Opciones
opciones_otras = {
    "-v": ("Nivel de verbosidad 1: muestra información sobre el escaneo", var_verbosidad_1),
    "-vv": ("Nivel de verbosidad 2: muestra aun más información sobre el escaneo que -v", var_verbosidad_2),
    "-d": ("Nivel de depuración: más verbosidad aun que -vv. Intensidad de 0 (menos detalle) a 9 (máximo detalle)", var_depuracion),
    "-6": ("Escanea IPv6", var_ipv6)
}

# Crear Checkbuttons, Labels y Scale para Otras Opciones
check_verbosidad_1 = None
check_verbosidad_2 = None
scale_nivel_depuracion = None

for comando, (descripcion, variable) in opciones_otras.items():
    contenedor_otras_opciones = tk.Frame(tab_otras_opciones, padx=3, pady=3)
    contenedor_otras_opciones.pack(fill=tk.X)

    check = tk.Checkbutton(contenedor_otras_opciones, text=comando, variable=variable, command=manejar_exclusion_mutua_verbosidad)
    check.pack(side=tk.LEFT)

    if comando == "-v":
        check_verbosidad_1 = check
    elif comando == "-vv":
        check_verbosidad_2 = check


    label = tk.Label(contenedor_otras_opciones, text=f"--> {descripcion}")
    label.pack(side=tk.LEFT)

    if comando == "-d":
        # Crear un Scale (deslizador) para el nivel de depuración
        scale_nivel_depuracion = tk.Scale(contenedor_otras_opciones, showvalue=False, from_=0, to=9, orient=tk.HORIZONTAL, variable=var_nivel_depuracion, command=si_escaca_movida_d)
        scale_nivel_depuracion.pack(side=tk.LEFT)
        scale_nivel_depuracion.config(state=tk.DISABLED)

        depuracion_valor_intensidad = tk.Label(contenedor_otras_opciones, text="0")
        depuracion_valor_intensidad.pack(side=tk.LEFT)



# Función para inicializar el historial de consultas
def inicializar_historial_consultas():
    global historial_consultas
    historial_consultas = ttk.Treeview(contenedor_tabla_historico, columns=("Nº", "consulta", "fecha"), show="headings")
    historial_consultas.heading("Nº", text="Nº")
    historial_consultas.heading("consulta", text="Consulta")
    historial_consultas.heading("fecha", text="Fecha")

    # Configurando el ancho de las columnas
    historial_consultas.column("Nº", width=20)  # Ancho para la columna "Nº"
    historial_consultas.column("consulta", width=625) # Ancho para la columna "consulta"
    historial_consultas.column("fecha", width=100)  # Ancho para la columna "fecha"

    historial_consultas.pack(fill=tk.BOTH, expand=True)
    historial_consultas.bind("<<TreeviewSelect>>", on_historial_select)



# Función para manejar la selección en el historial
def on_historial_select(event):
    for seleccionado in historial_consultas.selection():
        item = historial_consultas.item(seleccionado)
        mostrar_resultado(item['values'][2])  # Asumiendo que guardas el resultado en la tercera posición de values


# Sección historial de consultas
seccion_historial_consultas = tk.LabelFrame(marco_izquierdo, text="Historial de Consultas")
seccion_historial_consultas.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

# Contenedor general historial de consultas
contenedor_general_historico= tk.Frame(seccion_historial_consultas)
contenedor_general_historico.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Contenedor tabla histórico
contenedor_tabla_historico = tk.Frame(contenedor_general_historico)
contenedor_tabla_historico.pack(fill=tk.BOTH, expand=True,)





inicializar_historial_consultas()



# Ejecución de la ventana principal
try:
    ventana_principal.mainloop()
except KeyboardInterrupt:
    pass