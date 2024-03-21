## [1.8] - 21/03/2024
### Cambiado
- Se corrije errata que duplicaba la opción -sL en la sección tipo de escaneo cuando debería de estar solo en reconocimiento de red.
- Se corrije errata que mostraba la opción -sF como -Sf.



## [1.7] - 27/01/2024
### Añadido
- Añadida opción de descubrimiento -PE 


## [1.6] - 06/01/2024
### Añadido
- Se añade sección histórico de consultas:
    - Visualización de las consultas anteriores en una lista donde se ve el número de consulta, la consulta en sí, la fecha y hora.
    - Próximamente se espera añadir la visualización del resultado de la consulta seleccionada en este histórico para evitar tener que lanzar otro escaneo o abrir archivos externos. 
- Se añade funcionalidad en Windows (en pruebas)


## [1.5] - 04/01/2024
### Añadido
- Sección vulnerabilidades es ahora funcional. Permite elegir el modo predeterminado o una categoría específica de vulnerabilidad a través de una lista desplegable.
- Sección otras opciones ahora funcional. Permite el modo verbose, depuración y análisis de IPv6
- Sección exportar resultado ahora es funcional:
    - Permite exportar los resultados de la búsqueda a los diversos formatos de archivo más habituales
    - El cuadro de entrada del nombre de archivo se muestra con fondo rojo si no es un nombre de archivo válido
- Correcciones menores de código y erratas en menús
- Ligera optimización de código


## [1.4] - 03/01/2024
### Añadido
- Sección evasión ahora es funcional
- La escala de -T ahora es funcional y se puede elegir el nivel de 0 a 5 mediante una barra de desplazamiento horizontal
- La entrada de ip, rango de ip's y o red ahora también admite dominios con su correspondiente validación
- Botón escanear empieza a tener funcionalidad: realiza el escaneo y muestra el resultado en la pantalla de la derecha: funcional en Linux
- Sección sobre el autor mejorada


## [1.3] - 02/01/2024
### Añadido
- Icono de programa
- Validaciones a entrada de puertos:
    - Entrada de puerto único: ahora si no se introduce un número válido (entre 1 y 65535) el fondo cambia a rojo
    - Entrada de rangos de puertos: ahora solo se permiten números validos (entre 1 y 65535) y el de la primera casilla debe de ser menor al de la segunda. Si todo es correcto la casilla se pone en verde y, si no, en rojo
    - Entra de puertos específicos: ahora solo permite números separados por comas siempre que sean válidos (entre 1 y 65535) y no estén repetidos. Si todo es correcto, la casilla se pondrá verde, si no, en rojo
- Escalas en las opciones -sV y -T:
    - -sV: se habilita escala del 0 al 9 para activar el modo "--version-intensity" en nivel elegido. Esta opción se activa al mover la escala.
    - -T: se habilita escala de 0 a 5 aun sin funcionalidad
- Secciones: evasión, scripts y "otras opciones" (todas ellas están bloqueadas por no ser funcionales hasta versiones posteriores)
### Cambiado
- Se han reestructurado algunos comandos moviéndolos a secciones más acordes


## [1.2] - 01/01/2024
### Añadido
- Modo oscuro
- Sección de opciones para especificar puertos o rangos de puertos
- Añadida versión de Nmap sobre la que trabaja el programa en el título de la sección de la consulta generada
- Información sobre el autor


## [1.1] - 31/12/2023
### Añadido
- Sección de opciones de escaneo de servicios y versiones añadida
- Opción de introducir un rango de ip's de clase c
- Validación para la entrada ip, rango de ip's y red mediante código de color: fondo verde datos válidos y rojo erróneos
- Ahora si se marca el checkbox -A se deshabilita -O y viceversa por ser redundantes
- Añadido menú elemental del programa con opción de salir (funcional), modo oscuro, modo claro e información sobre el autor (aun no funcionales)


## [1.0] - 31/12/2023
### Añadido
- Lanzamiento inicial del proyecto.
- Función introducir ip o red
- Opciones de descubrimiento de red funcionando
- Opciones de técnicas de escaneo funcionando
- Algunas opciones de búsqueda de servicios y versiones implementadas
- Cuadro para visualizar la consulta creada antes de copiarla o lanzarla
- Botón de copiar consulta al portapapeles funcional
- Botón de limpiar consulta para empezar a crearla de nuevo funcional
- Otras implementaciones gráficas aun no funcionales
- Usable con limitaciones a causa de no estar implementadas aun todas las opciones habituales
