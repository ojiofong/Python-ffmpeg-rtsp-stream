"""
Requirements: You must have either 'ffmpeg' or 'python-ffmpeg' library installed on your machine

Maybe install python-ffmpeg since it also installs ffmpeg and allows you to explore both.

To explore `python-ffmpeg` library bindings here are some examples:
https://github.com/kkroening/ffmpeg-python/tree/master/examples

It doesn't matter how the problem is solved, but you may find that there are more
resources for executing direct ffmpeg commands
"""

import subprocess

stream_url = "rtsp://184.72.239.149/vod/mp4:BigBuckBunny_175k.mov"
output_file = "out.png"  # .jpg is also fine

# This command grabs each frame from stream_url and
# writes/overwrites to the same output file on the disk.

# Ideally we want to grab each image frame on the fly
# without saving it to the disk and convert it to rgb for processing

command = [
    'ffmpeg',
    '-i', stream_url,
    '-vf', 'fps=15',
    '-pix_fmt', 'rgb24',
    '-y',
    '-s', '%dx%d' % (640, 360),
    '-update', '1',
    output_file,
]

subprocess.call(command)
