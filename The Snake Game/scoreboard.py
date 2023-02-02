from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = 0
        with open("score.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_score()
        self.hideturtle()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center",font=("Courier", 18, "normal"))
        
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align = "center",font=("Courier", 18, "normal"))
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", "W") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
        
    def increse_score(self):
        self.score += 1
        self.update_score()
        
        