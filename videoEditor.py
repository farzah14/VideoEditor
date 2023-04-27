from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
import moviepy.editor as mp

EDIT_TYPE = {
    0: "rotate",
    1: "convert_mp4_to_mp3",
    2: "add_song_on_video"
}

def welcomeMessage():
    print("Welcome in video editor")

def rotateVideo():
    print("Welcome Rotate Video")
    inputName = input("nama video untuk di rotate(.mp4) : ")
    clip = VideoFileClip(inputName)
    rotate = clip.rotate(int(input("berapa derajat video untuk dirotate : ")))
    outputName = input("nama untuk export video(.mp4) : ")
    rotate.write_videofile(outputName)
    print("Rotate Video Success")
    
    
def convertVideo():
    print("Welcome Convert Video From MP4 to MP3")
    inputName = input("nama video untuk di convert(.mp4) : ")
    video = mp.VideoFileClip(inputName)
    outputName = input("nama untuk export audio(.mp3) : ")
    video.audio.write_audiofile(outputName)
    print("Convert Success")
    


def addSongOnVideo():
    print("welcome to the add song on video")
    
    userInputNameVideo = input("enter video name for add song(.mp4) : ")
    
    clip = VideoFileClip(userInputNameVideo)
    
    #subclip, memotong video/lagu
    userInputNameSong = input("enter audio name(.mp3) : ")
    
    song = AudioFileClip(userInputNameSong).subclip(0,10)
    
    result = clip.set_audio(song)
    
    result.write_videofile(input("enter output name : "))   
    
    print("Success")
    
    

def userQuestion():
    user = input("do you want edit video(y/n) : ").lower()
    if user == "y".lower():
        
        print("\n""type edit : ")
        
        for option in EDIT_TYPE:
            print(f"{option}, {EDIT_TYPE.get(option)}")
        
        print("pilih berdasarkan indeks\n")
        
        userTypeEdit = int(input("what do you want edit video : "))
        
        if userTypeEdit in EDIT_TYPE:
            
            result = EDIT_TYPE[userTypeEdit]
            
            if result == EDIT_TYPE.get(0):
                return rotateVideo()
            elif result == EDIT_TYPE.get(1):
                return convertVideo()
            elif result == EDIT_TYPE.get(2):
                return addSongOnVideo()
            
        else:
            print("please input valid data")
            quit()
            
    else:
        quit()

def main():
    welcomeMessage()
    userQuestion()

if __name__ == "__main__":
    main()

