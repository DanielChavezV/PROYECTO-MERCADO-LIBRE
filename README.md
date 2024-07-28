### BIENVENIDO A MI PROYECTO DE PRUEBAS EN SELENIUM

![Py](https://slackmojis.com/emojis/58444-selenium/download) ![Py](https://slackmojis.com/emojis/50032-visual-studio/download) ![Py](https://slackmojis.com/emojis/257-github/download)  

**INSTALACIÓN DEL PROYECTO**

**Instalación en Windows:**

Instalar python en un versión  mayor a la 3.6, deberás instalar Selenium y PyUnitReport - (Librería que nos permite generar reportes en HTML)

**Pasos:**

1.  Verificar que versión de Pyhon tenemos instalada en el equipo, usando el comando:

	![Py](https://static.platzi.com/media/user_upload/image-24e1653c-07ed-4245-9d44-bd3f72e4e59f.jpg)

1.  Si no tienes instalado Python acceder a: https://www.python.org/downloads/ para descargar e instalar.

	![Py](https://static.platzi.com/media/user_upload/image-b254c79f-f38d-4023-a9e4-e86d8449894a.jpg)

	![Py](https://static.platzi.com/media/user_upload/image-d2651ced-9917-45ad-b326-eec597ed5f27.jpg)

3. Verificar nuevamente que versión de pyhon se instaló en el equipo:

	![Py](https://static.platzi.com/media/user_upload/image-c1d89ca0-5fa9-4e79-a85d-192ec956a319.jpg)

4. Instalar Selenium con el comando:

	![Py](https://static.platzi.com/media/user_upload/image-7dbc0062-fc25-4a9d-b405-cb02e5b921d0.jpg)
	
	![Py](https://static.platzi.com/media/user_upload/image-d25b9d3b-6cd9-4422-9c5e-25def4122c9e.jpg)

5. Instalar PyUnitReport con el comando: 

	![Py](https://static.platzi.com/media/user_upload/image-f50ffd08-1ab2-4960-9daa-9b4535dd9737.jpg)

	![Py](https://static.platzi.com/media/user_upload/image-f64ed63d-6e46-43fd-bb47-0870ea1fd6c5.jpg)



# Crear y Activar un Ambiente Virtual 

Al crear un ambiente virtual estás aislando tu proyecto del resto de tu computadora y haciendo que funcione con módulos independientes. Es decir, para llevar este curso puedes tener una versión de Python y Selenium y para hacer otro proyecto puedes tener versiones distintas. Esto hace que los proyectos no se rompan.

Usualmente, sin hacer uso de ambientes virtuales, los proyectos en tu computadora se verían así:

![Py](https://static.platzi.com/media/user_upload/Untitled-bf9d42f1-5c44-4521-8b1f-8052334b96c0.jpg)

Pero, al organizarlo profesionalmente, tus proyectos aislados en ambientes virtuales se verían de esta forma:

![Py](https://static.platzi.com/media/user_upload/Untitled%20%281%29-8f77947f-7ca7-4c49-9ab4-c462d734678f.jpg)

**Si trabajas en Windows puedes poner lo siguiente:**




    #Crear
    py -m venv nameOfVirtualEnv
    
    #Activar
    .\nameOfVirtualEnv\Scripts\activate
    
    #Desactivar 
    deactivate

Te sugiero que, si trabajas en Windows, uses una terminal basada en Unix como Cmder o un WSL

## # **Se muestran errores en la terminal, ¿qué hacer?**

Si te sale un error, lo más probable es que haya errores por no tener paquetes descargados o no tener Python actualizado. Soluciónalo así:



    sudo apt update
    sudo apt -y upgrade
	
    #Instalando el módulo para ambientes virtuales
    sudo apt-get install python3.8-venv o python3.9-venv según la versión

## # **Instalación de dependencias**

Recuerda tener activado el ambiente virtual. Luego pones esto en la terminal.

    pip install selenium==4.1.3
    sudo apt-get install python3.9-venv

## ¡Listo, ya puedes continuar con el proyecto!


[========]

# PRUEBA TÉCNICA

Este proyecto de prueba es creado desde el curso de Introducción a Selenium con Python de Platzi. En el cual pretende abarcar todos los conceptos y términos aprendidos en cada una de las clases del curso, tales como:

- Automatizar el navegador para testing, scraping y tareas repetitivas

- Automatizar casos de pruebas, suites de pruebas y generar reportes

- Aplicar DDT y POM a los scripts

A continuación este es el orden de la Prueba Técnica:

##### **FLUJO EN MERCADO LIBRE: ** 


    1. Ingresar a mercadolibre.com
    2. Seleccionar 'Colombia' como país
    3. Buscar el término "Playstation4"
    4. Filtrar por condición "Nuevos"
    5. Filtrar por la Ubicación "Bogotá"
    6. Ordenar de Mayor a Menor precio
    7. Obtener el nombre y Precio de los primeros 5 Articulos
