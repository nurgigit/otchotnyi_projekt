import random

secret_number = random.randint(1,3)
attempts = 2

def setup():
    size(400, 400)
    textSize(20)
    textAlign(CENTER, CENTER)
    fill(255)

def draw():
    background(0)
    text("Guess the number!", width/2, 50)
    text("Attempts: " + str(attempts), width/2, 100)

def keyPressed():
    if key == ENTER:
        check_guess(int(input("Enter your guess: ")))
