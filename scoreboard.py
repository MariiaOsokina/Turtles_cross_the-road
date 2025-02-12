from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 1
        self.hideturtle()
        self.penup()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.goto(-260,260)
        self.write(f"Level: {self.level} ", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level +=1
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write("Game over", align = "center", font=FONT)
