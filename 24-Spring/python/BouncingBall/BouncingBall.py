# Original source: https://blog.naver.com/isaac7263/221582646013

from tkinter import *
import random, os, sys

class Scoreboard:
    global canvas
    def __init__(self):
        self.canvas = canvas
        self.score = 0
        self.score_view = self.canvas.create_text(700, 15, text="SCORE: " + str(self.score), fill="black")

    def increase_score(self):
        self.score += 1
        self.canvas.itemconfig(self.score_view, text="SCORE: " + str(self.score))

class Ball:
    def __init__(self, canvas, paddle, top, scoreboard, color):
        self.canvas = canvas
        self.paddle = paddle
        self.top = top
        self.scoreboard = scoreboard
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color) # 공 그리기

        initial_x = self.canvas.winfo_width() * 0.5
        initial_y = self.canvas.winfo_height() * 0.6
        self.canvas.move(self.id, initial_x, initial_y) # 공의 위치를 설정하는 정적인 값

        # 공의 시작 방향 변경
        starts = [i for i in range(-3,4) if i != 0]
        random.shuffle(starts)
        self.x = starts[random.randint(0, len(starts) - 1)]
        self.y = -int(self.canvas.winfo_height() * 0.005)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        # self.canvas_height와 self.canvas_width:
        # 캔버스의 현재 높이와 너비를 저장하여, 공이 캔버스의 경계를 넘어서 이동하지 않도록 하는 데 사용하기 위함

        # 바닥에 닿는 경우 체크
        self.touch_floor = False

    def hit_bottom(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)

        # 공의 오른쪽 면의 위치가 패들의 왼쪽 위치보다 크고,
        # 공의 왼쪽 위치가 패들의 오른쪽 위치보다 작은지
        if pos[0] <= paddle_pos[2] and pos[2] >= paddle_pos[0]:
            if paddle_pos[1] <= pos[3] <= paddle_pos[3]: # 공이 패들보다 공중에 떠있는 경우 제외
                return True
        return False

    def hit_top(self, pos):
        top_pos = self.canvas.coords(self.top.id)

        if pos[0] <= top_pos[2] and pos[2] >= top_pos[0]:
            if top_pos[1] <= pos[3] <= top_pos[3]:
                return True
        return False

    # 공을 움직이고 경계에 닿으면 방향을 변경
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        # self.x와 self.y:
        # 매 프레임마다 공의 움직임을 제어하는 x축, y축 속도를 지정하기 위해 사용되는 값
        pos = self.canvas.coords(self.id) # 식별 번호로 캔버스에 그려진 현재의 x와 y좌표를 반환
        # pos값은 [x1, y1, x2, y2] 형태의 리스트 값
        # x1과 y1은 공의 좌측 상단, x2와 y2는 공의 우측 하단
        if pos[1] <= 0: self.y = 3 # 공을 아래로 방향 전환시키기 위해 self.y의 값을 양수로 조정
        if pos[3] >= self.canvas_height:
            self.y = -3
            self.touch_floor = True # 공이 바닥에 닿는 경우 패배
        # 공이 측면에 부딪히는 경우를 고려
        if pos[0] <= 0: self.x = 3
        if pos[2] >= self.canvas_width: self.x = -3

        # Paddle에 부딪힌 경우
        if self.hit_bottom(pos): self.y = -3

        # TopPaddle에 부딪힌 경우
        if self.y < 0 and self.hit_top(pos):
            self.y = 3
            self.scoreboard.increase_score()

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)

        initial_x = self.canvas.winfo_width() * 0.4
        initial_y = self.canvas.winfo_height() * 0.8
        self.canvas.move(self.id, initial_x, initial_y)

        self.x = 0
        self.canvas_width = self.canvas.winfo_width()

        # key 바인딩
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)


    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0: self.x = 0
        elif pos[2] >= self.canvas_width: self.x = 0

    def turn_left(self, event): self.x = -int(self.canvas_width * 0.005)
    def turn_right(self, event): self.x = int(self.canvas_width * 0.005)

class TopPaddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 20, fill=color)

        initial_x = self.canvas.winfo_width() * 0.4
        initial_y = self.canvas.winfo_height() * 0.1
        self.canvas.move(self.id, initial_x, initial_y)

        self.x = 2

        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0: self.x = 1 # 숫자가 클수록 빠르게 움직임
        elif pos[2] >= self.canvas_width: self.x = -1

def restart(event):
    global path
    global tk
    try:
        if ('normal' == tk.state()):
            tk.destroy()
    finally:
        os.system(f'python "{path}"')

def game_loop():
    if not ball.touch_floor:
        ball.draw()
        paddle.draw()
        top.draw()
    tk.after(10, game_loop) # 10ms = 초당 100번 함수 호출

path = os.path.realpath(sys.argv[0])

# Frame 생성
tk = Tk() # Tk 객체: 버튼, 입력상자, 그림 그릴 수 있는 캔버스 제공
tk.title("Bouncing Ball")
tk.resizable(0, 0) # 고정된 프레임 크기, 사이즈 변경 불가
tk.wm_attributes("-topmost", 1) # 다른 모든 창들 앞에 캔버스를 가진 창이 위치함

canvas = Canvas(tk, width=800, height=500, bd=0, highlightthickness=0, bg="white")
# bd=0, highlightthickness=0 => 캔버스 외곽에 둘러싼 외곽선(border)이 없도록
canvas.pack() # 위 설정값대로 크기를 맞춤
canvas.bind_all("<KeyPress-Return>", restart)

btn = Button(tk, text="Quit", command=tk.quit) # 'Quit' 버튼에 tk.quit 함수 연결
btn.place(x=5, y=5)
# btn.pack() # 화면에 표시하라는 지시 명령
# 버튼이 기본적으로 캔버스 내에서 자동적으로 정렬

scoreboard = Scoreboard(tk)
tk.update() # Tkinter가 변경된 GUI 요소들을 즉시 처리하고 화면에 그 결과를 반영

paddle = Paddle(canvas, 'blue')
top = TopPaddle(canvas, 'red')
ball = Ball(canvas, paddle, top, scoreboard, 'green')

tk.after(10, game_loop)
tk.mainloop() # 이벤트 루프 시작