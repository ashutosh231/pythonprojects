from moviepy.editor import *

video = VideoFileClip("/Users/ashutoshkumar/Documents/ashu c++/c++/python/babu.mp4").subclip(00,2)
video.write_gif("Test2.gif")