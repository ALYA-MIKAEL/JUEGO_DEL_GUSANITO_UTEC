# EL JUEGO DEL GUSANITO
![This is an image](https://www4.minijuegosgratis.com/v3/games/thumbnails/214311_1.jpg)

El juego consiste en una línea que no para de moverse, el usuario lo controla con las flechas de:

 → derecha 

 ← izquierda

 ↑ arriba

 ↓ abajo 

Así el gusanito no puede chocarse con las paredes ni consigo mismo.

El obejtivo del juego es no chocarse y comer la mayor cantidad de manzanas rojas y que el gusano crezca lo más que máximo posible.


## INTEGRANTES
1. Noé Ananias Paredes Rauraico / NoeParedes
2. Kevin Richard Dulanto / kevinrdf
3. Valeria Saidid Miranda Ibarra / ALYA-MIKAEL
4. Jhan Charles Manchay Flores/ JhanUTEC


## INSTRUCCIONES DEL JUEGO
Importamos nuestro módulo Ursina y también el módulo random, de esta manera, podemos generar aleatoriamente una manzana y colocarla en una ubicación aleatoria.

Para crear un fondo: 
app=ursina()

La aplicación es igual a la función de Ursina:
app.run()

La aplicación se va a ejecutar:
Entity(model='quad', scale=60, texture='fondo_utec')

Se crea la entidad para crear el fondo de nuestro juego, que es igual a un cuádruple con una escala de 60 y con una textura de la UTEC.

Ahora creamos el campo del juego: 
campo = Entity(model='quad',texture=’campo_del_jusanito’,scale=(12,12),
     position=(19 // 2,19// 2, -0.01))

Agregamos dos sonidos que permitirán una mejor experiencia al usuario. Con el “mordida.mp3”, cada vez que la serpiente se come una manzana hay un sonido de comer y cuando se estrella contra una pared o a sí mismo, hay un silbido gracias al “perdedor.mp3”.

Al ejecutar el código, el usuario deberá utilizar las flechas:
 
→ derecha

← izquierda

↑ arriba

↓ abajo
 
Y evitar chocarse contra las paredes, o se perderá.


## VISTA PREVIA DEL JUEGO

![image](https://user-images.githubusercontent.com/90013732/146306968-49775566-1307-45ba-9eec-f171b15a4d51.png)
