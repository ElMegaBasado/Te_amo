import turtle

# Función para dibujar un corazón con turtle
def dibujar_corazon():
    turtle.bgcolor("lightblue")  # Fondo azul claro
    turtle.speed(3)
    turtle.color("red")
    
    turtle.begin_fill()
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50, 200)
    turtle.right(140)
    turtle.circle(50, 200)
    turtle.forward(133)
    turtle.end_fill()

# Función para escribir el mensaje debajo del corazón
def escribir_mensaje():
    turtle.penup()
    turtle.goto(0, -100)  # Posicionamos el texto debajo del corazón
    turtle.color("darkblue")
    turtle.write("¡Feliz cumpleaños, mi amor!", align="center", font=("Arial", 18, "bold"))
    
# Función principal que ejecuta todo
def main():
    turtle.setup(500, 500)
    turtle.title("¡Feliz Cumpleaños!")
    
    # Dibujamos el corazón
    dibujar_corazon()
    
    # Escribimos el mensaje
    escribir_mensaje()

    # Pausa para ver el dibujo
    turtle.hideturtle()
    turtle.done()

# Ejecutar la función principal
if __name__ == "__main__":
    main()
