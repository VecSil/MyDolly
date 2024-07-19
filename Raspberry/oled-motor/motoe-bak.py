import RPi.GPIO as GPIO          
from time import sleep




# 定义引脚
ENA = 5    # 控制左轮速度
IN1 = 6    # 控制左轮前进
IN2 = 13   # 控制左轮后退
ENB = 20   # 控制右轮速度
IN3 = 19   # 控制右轮前进
IN4 = 26   # 控制右轮后退

# 设置GPIO模式
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)



# 初始化PWM
p_left = GPIO.PWM(ENA, 1000) 
p_right = GPIO.PWM(ENB, 1000)
p_left.start(25) 
p_right.start(25)


# 初始化方向变量
temp1 = 1   # 左轮状态
temp2 = 1   # 右轮状态

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

while(1):

    x = input()   
    
    if x == 'r':
        print("run")
        if temp1 == 1:
            GPIO.output(IN1, GPIO.HIGH)
            GPIO.output(IN2, GPIO.LOW)
            print("left wheel forward")
        else:
            GPIO.output(IN1, GPIO.LOW)
            GPIO.output(IN2, GPIO.HIGH)
            print("left wheel backward")
        
        if temp2 == 1:
            GPIO.output(IN3, GPIO.HIGH)
            GPIO.output(IN4, GPIO.LOW)
            print("right wheel forward")
        else:
            GPIO.output(IN3, GPIO.LOW)
            GPIO.output(IN4, GPIO.HIGH)
            print("right wheel backward")

    elif x == 's':
        print("stop")
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.LOW)

    elif x == 'f':
        print("forward")
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)
        temp1 = 1
        temp2 = 1

    elif x == 'b':
        print("backward")
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.HIGH)
        temp1 = 0
        temp2 = 0

    elif x == 'l':
        print("low")
        p_left.ChangeDutyCycle(10)
        p_right.ChangeDutyCycle(10)

    elif x == 'm':
        print("medium")
        p_left.ChangeDutyCycle(50)
        p_right.ChangeDutyCycle(50)

    elif x == 'h':
        print("high")
        p_left.ChangeDutyCycle(90)
        p_right.ChangeDutyCycle(90)
    
    elif x == 'e':
        GPIO.cleanup()
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
