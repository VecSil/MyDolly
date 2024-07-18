import RPi.GPIO as GPIO
import socket
import sys
import os
from PIL import Image, ImageDraw, ImageFont
import OLED_1in3

# 初始化 OLED
def initialize_oled(picdir):
    disp = OLED_1in3.OLED_1in3()
    disp.Init()
    disp.clear()
    return disp

# 显示文本到 OLED
def display_text(disp, picdir, text):
    image = Image.new('1', (disp.width, disp.height), "WHITE")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    draw.text((10, 10), text, font=font, fill=0)
    image = image.rotate(180)
    disp.ShowImage(disp.getbuffer(image))

# GPIO 设置
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  # 禁用GPIO警告
IN1 = 12
IN2 = 16
IN3 = 20
IN4 = 21
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# 定义电机控制函数
def forward():
    print("Moving forward")
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

def backward():
    print("Moving backward")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

def left():
    print("Turning left")
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

def right():
    print("Turning right")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

def stop():
    print("Stopping")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

# 创建 TCP 服务器
try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.43.141', 6666))  # 监听所有接口
    server_socket.listen(1)
    print("Waiting for connection...")
except OSError as e:
    print(f"Error binding to address: {e}")
    sys.exit(1)

picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
disp = initialize_oled(picdir)  # 初始化 OLED

try:
    while True:
        client_socket, addr = server_socket.accept()
        print("Connected by", addr)
        client_socket.send("Hello, client!".encode())  # 发送消息给客户端

        while True:
            data = client_socket.recv(1).decode()
            if not data:
                break
            print("Received:", data)

            if data == 'X':
                left()
            elif data == 'B':
                right()
            elif data == 'Y':
                forward()
            elif data == 'A':
                backward()
            elif data == 'P':
                display_text(disp, picdir, "┑(￣Д ￣)┍")
            elif data == 'O':
                display_text(disp, picdir, "ヽ(*´∀`)ﾉ")
            elif data == 'I':
                display_text(disp, picdir, "   (╬•̀皿•́)")
            elif data == 'Q':
                stop()
                client_socket.close()
                break  # 退出循环，关闭连接
            else:
                stop()

except KeyboardInterrupt:
    print("Server is shutting down.")
finally:
    server_socket.close()  # 关闭服务器套接字
    GPIO.cleanup()  # 清理 GPIO 资源
    disp.module_exit()  # 退出 OLED 模块