from moviepy.editor import *

file_name="intro"                                                        # give the file name correctly
my_clip=VideoFileClip(f"{file_name}.mp4")            # don't forget to mention the extension ( .mp4 )
my_clip.audio.write_audiofile(f"{file_name}.mp3") # don't forget to mention the extension ( .mp3 )
print(f"Audio File Name : {my_clip.filename}")
print(f"Audio File Duration : {my_clip.duration}")


