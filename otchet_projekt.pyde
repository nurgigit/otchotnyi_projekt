import random
player_x = 100
object1_y = 0
score = 0
object1_x = 300

def setup():
    size(800,800)
def draw():
    global player_x, object1_y, score, object1_x
    
    background(255)
    
    fill(255, 0, 0)
    rect(player_x,700, 80, 80)
    
    ellipse(300, object1_y, 50, 50)
    object1_y += 2

    if object1_y >= 675 and player_x >= object1_x - 100 and player_x <= object1_x + 25:
        object1_y = 0
        object1_x = random.randint(25, 775)
        score += 1
        
    elif object1_y >= 775:
        object1_y = 0
        object1_x = random.randint(25, 775)
        score -= 1
        
    print(score)
    print(player_x)
    print(object1_y)
    if keyPressed:
        if key == "A" or key == "a" or key == 'ф' or  key == 'Ф':
            player_x -= 3
        elif key == "D" or key == "d" or key == 'в' or key == 'В':        
            player_x += 3
