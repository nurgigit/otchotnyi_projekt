    player_x = 100
object1 = 0
score = 0

def setup():
    size(800,800)
def draw():
    global player_x, object1, score
    
    background(255)
    
    fill(255, 0, 0)
    rect(player_x,700, 80, 80)
    
    ellipse(300, object1, 50, 50)
    object1 += 5

    if object1 >= 675 and player_x >= 200 and player_x <= 325:
        object1 = 300
        score += 1
        
    elif object1 >= 775:
        object1 = 0
        score -= 1
        
    print(score)
    print(player_x)
    print(object1)
    if keyPressed:
        if key == "A" or key == "a" or key == 'ф' or  key == 'Ф':
            player_x -= 3
        elif key == "D" or key == "d" or key == 'в' or key == 'В':
            player_x += 3
