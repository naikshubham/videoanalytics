import subprocess

# ffmpeg = 'G:/ffmpeg/bin/ffmpeg'
video_file = 'F:/LTI/Video_Deduplication/Test_data/ads/ad_1.mp4'
output_filename = 'out.mp4'
# cmd = [ffmpeg, '-i' ,video_file, '-af' ,'silencedetect=noise=-30dB:d=0.5', '-f','null' ,'-', 'out.mp4']
# cmd = ['scenedetect', '-i', video_file, '-o', output_filename ,'-s', 'my_video.stats.csv', 'detect-content', 'list-scenes', 'save-images', 'split-video']

cmd = ['scenedetect', '-i', video_file, '-s' ,'video.stats1.csv', 'detect-content', 'list-scenes', '-n', 'split-video']

subprocess.call(cmd)