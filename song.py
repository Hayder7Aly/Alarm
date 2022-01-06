from pygame import mixer

def func1(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    # while True:
    #     if  stop=='no':
    #         mixer.music.stop()

func1('water.mp3')
input()
