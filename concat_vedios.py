import os
import re

def concat_vedios():

    videos = []

    if os.path.exists("mylist.txt"):
       os.remove("mylist.txt")

    if os.path.exists("mylistNew.txt"):
       os.remove("mylistNew.txt")

    if os.path.exists("finalversion.mp4"):
       os.remove("finalversion.mp4")

    mycmd1 = "for f in ./OutPutVideo/*.mp4; do echo \"file '$f'\" >> mylist.txt; done"
    mycmd2 = "ffmpeg -f concat -safe 0 -i mylistNew.txt -c copy finalversion.mp4"

    os.system(mycmd1)

    with  open("mylist.txt" ,'r')  as file :
        for line in file :
            videos.append(line.strip())

    videos.sort(key=lambda f: int(re.sub('\D', '', f)))

    with open("mylistNew.txt", 'w') as file:
        for item in videos:
            file.write("{}\n".format(item))

    os.system(mycmd2)
