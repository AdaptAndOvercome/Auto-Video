#!/bin/bash
set -e

AUDIO="outputs/audio.wav"
VIDEO="outputs/video.mp4"
TEXT="meta/story.txt"

WIDTH=1080
HEIGHT=1920
FPS=30
DURATION=$(ffprobe -i "$AUDIO" -show_entries format=duration -v quiet -of csv="p=0")

ffmpeg -y \
  -f lavfi -i color=c=black:s=${WIDTH}x${HEIGHT}:d=${DURATION}:r=${FPS} \
  -i "$AUDIO" \
  -vf "drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:
       text='$(sed "s/'/’/g" $TEXT)':
       fontcolor=white:
       fontsize=48:
       line_spacing=10:
       x=(w-text_w)/2:
       y=(h-text_h)/2:
       box=1:
       boxcolor=black@0.5:
       boxborderw=20" \
  -c:a aac \
  -shortest \
  "$VIDEO"
