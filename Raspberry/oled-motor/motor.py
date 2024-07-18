import RPi.GPIO as GPIO
import time

# 设置GPIO引脚编号模式
GPIO.setmode(GPIO.BCM)

# 定义GPIO引脚
ENA = 5
IN1 = 22
IN2 = 13
IN3 = 19
IN4 = 26
ENB = 20

# 设置GPIO引脚为输出模式
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)

# 创建PWM对象
pwmA = GPIO.PWM(ENA, 100)  # 设置频率为100Hz
pwmB = GPIO.PWM(ENB, 100)  # 设置频率为100Hz
pwmA.start(0)  # 启动PWM信号，占空比为0
pwmB.start(0)  # 启动PWM信号，占空比为0

# 定义电机正转函数
def forward():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwmA.ChangeDutyCycle(100)  # 设置占空比为100%
    pwmB.ChangeDutyCycle(100)  # 设置占空比为100%

# 定义电机反转函数
def reverse():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwmA.ChangeDutyCycle(100)  # 设置占空比为100%
    pwmB.ChangeDutyCycle(100)  # 设置占空比为100%

# 主循环
try:
    while True:
        forward()  # 正转
        time.sleep(2)  # 持续2秒

        reverse()  # 反转
        time.sleep(2)  # 持续2秒

except KeyboardInterrupt:
    # 清理资源并停止PWM
    pwmA.stop()
    pwmB.stop()
    GPIO.cleanup()
