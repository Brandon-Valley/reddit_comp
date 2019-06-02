import cv2
file_path = "output.mp4"  # change to your own video path
vid = cv2.VideoCapture(file_path)
height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(height)





# import moviepy.editor as mp
# clip = mp.VideoFileClip("vids_to_compile/post_10.mp4")
# clip_resized = clip.resize(height=720) # make the height 360px ( According to moviePy documenation The width is then computed so that the width/height ratio is conserved.)
# clip_resized.write_videofile("movie_resized.mp4")