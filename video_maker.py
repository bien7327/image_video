from moviepy.editor import *

# configuration 
image_folder = "./assets/"
video_name = "video.mp4"
duration = 0.01 # duration of each image in seconds
video_fps = 16 # video fps


# get the images liste from the folder by names
pre_images = os.listdir(image_folder)
img = []
for i in pre_images:
    i = image_folder + i
    img.append(i)

clips = []
# create the clips for each image
for i in img:
    clips.append(ImageClip(i).set_duration(duration))

# append the clips to the final video
final = concatenate_videoclips(clips, method="compose")

# export the video 
final.write_videofile(video_name, fps=video_fps, remove_temp=True, codec="libx264", audio_codec="aac")