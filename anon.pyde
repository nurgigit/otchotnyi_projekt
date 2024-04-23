    size(400, 400)  # Устанавливаем размер окна

def draw():
    background(255)  # Устанавливаем белый фон

    # Рассчитываем радиус круга в зависимости от времени
    radius = min(width, height) * 0.5 + 200 * sin(millis() * 0.001)

    # Устанавливаем цвет круга в зависимости от положения мыши
    fill(mouseX, mouseY, 150)
    noStroke()

    # Рисуем круг
    ellipse(width / 2, height / 2, radius, radius)

    # Проверяем, заполнился ли весь холст
    if mousePressed:
        fill (random(0,255),random (0,255), random(0,255))  # Устанавливаем цвет текста
        textSize(32)  # Устанавливаем размер текста
        textAlign(CENTER, CENTER)
        text("s okonchaniem goda", width / 2, height / 2)
