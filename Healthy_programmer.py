from pygame import mixer
from datetime import datetime
from time import time

def musicloop(file,stopper,exi):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break
        elif a==exi:
            mixer.music.stop()
            exit()

def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg}{datetime.now()}\n")


if __name__ =='__main__':
    init_water=time()
    init_eyes=time()
    init_exer=time()
    watersecs=3
    exsecs=4
    eyessecs=4

    while True:
        if time()-init_water>watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm. Enter 'exit' to exit the program")
            musicloop("water.mp3","drank","exit")
            init_water=time()
            log_now("Drank water at ")


        elif time()-init_eyes>eyessecs:
            print("Eye exercise time. Enter 'done' to stop the alarm. Enter 'exit' to exit the program")
            musicloop("eye.mp3","done","exit")
            init_eyes=time()
            log_now("Exercised eyes at ")

        elif time()-init_exer>exsecs:
            print("Exercise time. Enter 'Ex done' to stop the alarm. Enter 'exit' to exit the program")
            musicloop("exercise.mp3","Ex done","exit")
            init_exer=time()
            log_now("Exercised at ")

