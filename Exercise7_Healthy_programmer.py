from pygame import mixer
from datetime import datetime
from time import time
def musicloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open('mylog.txt','a')as fw:
        fw.write(f"{msg} {datetime.now()}\n")
if __name__=='__main__':
    # musicloop('water.mp3','stop')
    init_water=time()
    init_eye=time()
    init_activities=time()

    watersecs=30*60
    eyessecs=40*60
    phy_activities=45*60
    while True:
        if time()-init_water>watersecs:
            print('WATER Drinking Time Now Enter "drank" For Stopping Music .')
            musicloop('water.mp3','drank')
            init_water=time()
            log_now("Drank water at :")

        if time()-init_eye>eyessecs:
            print('EYES Exercise Time Enter "doneeye" For Stopping Music .')
            musicloop('eye.mp3','doneeye')
            init_eye=time()
            log_now("Eyes Reluxed at :")

        if time()-init_activities>phy_activities:
            print('PHYSICAL Exercise Time Enter "done" For Stopping Music .')
            musicloop('exercise.mp3','done')
            init_activities=time()
            log_now("Exercise Done at :")
        

