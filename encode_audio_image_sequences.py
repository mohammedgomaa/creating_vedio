import os
import glob

def encode_audio_image_sequences()
    FileCounter = len(glob.glob('audio/*.wav'))
    for i in range(FileCounter):
        myCmd = "ffmpeg -loop 1 -i images/" +str(i) + ".png -i audio/" + str(i) +".wav -c:v libx264 -c:a aac -b:a 192k -shortest OutPutVideo/" + str(i) +".mp4"
        print myCmd
        os.system(myCmd)
