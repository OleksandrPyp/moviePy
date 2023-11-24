from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video.fx import all as vfx
input_video_path = "C:/Users/oleksandr_pypenko/#"

video = VideoFileClip(input_video_path)
intro_duration = 8  # 8 seconds
outro_duration = 5   # 5 seconds

intro_clip = video.subclip(0, intro_duration)
sped_up_clip = video.subclip(intro_duration, video.duration - outro_duration).speedx(4)
outro_clip = video.subclip(video.duration - outro_duration, video.duration)
sped_up_clip = sped_up_clip.fx(vfx.colorx, 1.2)

final_video = concatenate_videoclips([intro_clip, sped_up_clip, outro_clip])

output_video_path = "C:/Users/oleksandr_pypenko/#"
final_video.write_videofile(output_video_path)
