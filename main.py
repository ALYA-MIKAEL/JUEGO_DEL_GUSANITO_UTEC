from ursina import*  # Importamos Ursina
from random import randint
# Importamos random
app = Ursina()
# Ejecutamos Ursina para el fondo, la plataforma del juego y la manzana
# Crear el fondo
Entity(model='quad', scale=60, texture='fondo_utec')

# Creamos la plataforma de desplazamiento del gusanito
campo = Entity(model='quad',texture='campo_del_jusanito',scale=(12,12),
      position=(19 // 2, 19 // 2, -0.01))

# Creamos la manzanita
manzana = Entity(parent=campo,model='sphere',color=color.red,scale=0.05,
      position=(0.1,0.1,-0.03),collider='box')

text = Text(text="\n:) REGLAS DEL JUEGO: \n1. Come la mayor cantidad de manzanitas posibles"
                                     "\n2. Si el gusanito toca la pared, !PIERDES!",position=(-0.80,0.4,6))

body=[]
# Posicion de la pantalla de juego
camera.position = (19 // 2, -18, -18)
# Inclinación del juego
camera.rotation_x = -56
# Vista del juego
class juego(Entity):
  def __init__(self):
    super().__init__() # Usamos para dar acceso a metodos y propiedades
    # El 'self' es un parámetro especial que siempre se utilizará como una referencia al objeto mismo
    # Debe ser siempre el primer parámetro formal; no obstante, nunca se le dará un valor de parámetro real en la invocación
    self.parent = campo
    self.model = 'sphere'  # Forma del gusanito
    self.color = color.smoke  # Color del gusanito
    self.scale = 0.05  # Tamaño del gusanito
    self.position = (0,0,-0.03)  # Posicion del gusanito
    self.collider = 'box'
    self.dx = 0
    self.dy = 0
    self.eaten = 0

  def update(self):
    # En Python, la global 'palabra clave' permite modificar la variable fuera del alcance actual.
    # Se utiliza para crear una variable global y realizar cambios en la variable en un contexto local.
    global body, text
    self.x += time.dt * self.dx
    self.y += time.dt * self.dy

    # Cuando el gusanito se choca contra la pared
    hit_info = self.intersects()
    if hit_info.hit:

      Audio('mordida.mp3')  # Añadimos un audio cuando la serpiente come manzanas
      self.eaten += 1  # Se añade uno cada vez que el gusanito coma una manzana
      text.y = -1
      text = Text(text=f"Manzanas obtenidas: {self.eaten}",position=(0,0.3),origin=(0,0),
                  scale=1.5,color=color.cyan,background=True)  # Muestra la cantidad de manzanas que se va obteniendo

      # Posiciones aleatorias de la manzanita
      manzana.x = randint(-4,4)*0.1
      manzana.y = randint(-4,4)*0.1

      nuevo_cuerpo = Entity(parent=campo,model='sphere',z=-0.029, color=color.brown,scale=0.05)

      body.append(nuevo_cuerpo)

    # Mueve los segmentos finales, primero en el rango
    for i in range(len(body)-1,0,-1):
      body[i].position=body[i-1].position

    # Primer segmento
    if len(body) > 0:
      body[0].x = self.x
      body[0].y = self.y

    # Comprobación de los límites
    if abs(self.x) > 0.47 or abs(self.y) > 0.47:
      Audio('perdedor.mp3')  # Añadimos un audio cuando la serpiente choca en una pared o a si mismo
      for segment in body:
        segment.position = (10,10)
      body = []
      self.eaten = 0
      print_on_screen("HAS PERDIDO.¡NO CHOQUES!",position=(0,0),origin=(0,0),scale=2, duration=2)  # Imprime en consola el mensaje de derrota
      self.position = (0,0)
      self.dx = 0
      self.dy = 0

  # Función que permite mover al gusanito
  def input(self, key):
    if key == "right arrow":  # Flecha derecha
      self.dx = 0.3
      self.dy = 0
    if key == "left arrow":  # Flecha izquierda
      self.dx = -0.3
      self.dy = 0
    if key == "up arrow":  # Flecha hacia arriba
      self.dx = 0
      self.dy = 0.3
    if key == "down arrow":  # Flecha hacia abajo
      self.dx = 0
      self.dy = -0.3

player = juego()  # Se ejecuta el juego
app.run()