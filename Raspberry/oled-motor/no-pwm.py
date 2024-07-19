import RPi.GPIO as GPIO
import pygame

# 初始化pygame
pygame.init()

# 创建一个窗口（尽管我们不需要它）
screen = pygame.display.set_mode((100, 100))

# 定义引脚
IN1 = 22
IN2 = 13
IN3 = 19
IN4 = 26

# 设置GPIO模式
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

def forward():
    # 同时正转
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

def backward():
    # 同时倒转
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

def left():
    # 左转：OUT1, OUT2的电机正转；OUT3, OUT4的电机不转
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

def right():
    # 右转：OUT1, OUT2的电机不转；OUT3, OUT4的电机正转
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

def stop():
    # 停止所有电机
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                forward()
            elif event.key == pygame.K_s:
                backward()
            elif event.key == pygame.K_a:
                left()
            elif event.key == pygame.K_d:
                right()
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]:
                stop()

# 退出pygame和GPIO
pygame.quit()
GPIO.cleanup()