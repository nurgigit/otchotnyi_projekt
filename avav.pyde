def setup():
    size(600, 600)  # Устанавливаем размер окна

def draw():
    background(2)  # Устанавливаем белый фон

    # Рассчитываем радиус круга в зависимости от времени
    radius = min(width, height) * 0.5 + 200 * sin(millis() * 0.002)
    fill(random (0,255),random(0,255),random (0,255)
    # Устанавливаем цвет круга в зависимости от положения мыши
    
    # Рисуем круг
    ellipse(width / 2, height / 2, radius, radius)

    # Проверяем, заполнился ли весь холст
    if mousePressed:
        fill (random(0,255),random (0,255), random(0,255))  # Устанавливаем цвет текста
        textSize(29)  # Устанавливаем размер текста
        textAlign(CENTER, CENTER)
        text("S okonchaniem uchebnogo goda", width / 2, height / 2)
        
    def setup():
        frameRate(1)
    
    def draw():
        strokeWeight(3)
        stroke(250)
        point(random(0,800),random(0,600))  
  
