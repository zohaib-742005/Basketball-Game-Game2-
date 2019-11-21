#Game2 file
from gamelib import *

#variables
game = Game(800,800,"Basketball")

bk = Image("BasketballCourt.jpg",game)
bk.resizeTo(800,800)

Player1 = Image("Player1.png",game)
Player1.resizeBy(-50)
Player1.setSpeed(8,60)


Player2 = Image("Player2.png",game)
Player2.resizeBy(-50)
Player2.setSpeed(10,60)

Ball = Image("Ball.jpg",game)
Ball.resizeBy(-50)
Ball.setSpeed(12,60)


#essential game loop
while not game.over:
    game.processInput()

    bk.draw()
    Player1.move(True)
    Player2.move(True)
    game.update(30)

game.quit()
