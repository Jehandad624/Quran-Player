import quran
import json
from quran import Chapters
import requests
from pydub import AudioSegment
from pytubefix import YouTube
from pytubefix import Playlist
from pytubefix import request
from moviepy.editor import *
import random
from pydub import AudioSegment
import shutil
import os
from moviepy.editor import VideoFileClip
from mutagen.mp3 import MP3
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})
def translation(surah_num:str ,ayah_num:str , ayah_range):
    translation = []
    for i in range(int(ayah_range)):
        url = f"https://api.quran.com/api/v4/verses/by_key/{surah_num}:{ayah_num}?translations=84"
        payload = {}
        headers = {
        'Accept': 'application/json'
          }
        ayah_num = int(ayah_num) +1 
        ayah_num = str(ayah_num)
        response = requests.request("GET", url, headers=headers, data=payload)
        meow = json.loads(response.text)["verse"]["translations"][0]["text"]
        translation.append(meow)
    return translation
p = Playlist('https://www.youtube.com/playlist?list=PLWK_JRUhdXNsPcFoPmKlfz7qccVkCnID7')
video = random.choice(p.videos)
video_stream = video.streams.filter(file_extension='mp4', adaptive=True, only_video=True).order_by('resolution').desc().first()
output_path = 'downloads/'
download = video_stream.download(output_path=output_path, filename="veedio_original.mp4")
print(f"Video saved succesfully")
z = str(input("Please enter the number of  which reciter you want to listen to,""\n 1 — Abdul Baset \n \
2 — Abdul Baset (Murattal) \n \
3 — Abdurrahman As-Sudais \n \
4 — Abu Bakr Shatri \n \
5 — Hani Ar Rifai \n \
6 — Khalil Al Husary (Murattal) \n \
7 — Mishari Al Afasy \n \
8 — Siddiq Al-Minshawi (Mujawwad) \n \
9 — Siddiq Al-Minshawi (Murattal) \n \
10 — Saud Ash-Shuraym \n \
11 - Hussary Muallim \n"))
if int(z)>11 or int(z)<0:
    print("Please try again in range 1-11")
    quit()
surah_num = str(input("Enter the Surah num: "))
ayah_num = str(input("Enter the Ayah num! "))
ayah_range = input("If you want, how many ayah's would you like to listen? Say no if none. ")
if ayah_range.lower() == "no":
    ayah_range = 1
ayah_files = []
ayah_lengths = []
x = translation(surah_num,ayah_num,ayah_range)
for i in range(int(ayah_range)):
    url = f"https://api.quran.com/api/v4/recitations/{z}/by_ayah/{surah_num}:{ayah_num}"
    payload = {}
    headers = {
        'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    audio = json.loads(response.text)["audio_files"][0]["url"]
    audio = str(audio)
    recitation = f"https://audio.qurancdn.com/{audio}"
    ayah_num = int(ayah_num) + 1
    ayah_num = str(ayah_num)
    save_path = f"videos/ayah_{i + 1}.mp3"
    ayah_files.append(save_path)
    with open(save_path, "wb") as file:
        file.write(requests.get(f"https://audio.qurancdn.com/{audio}").content)
    meow = MP3(f"videos/ayah_{i+1}.mp3")
    ayah_lengths.append(meow.info.length)
print(ayah_lengths)

combined_file = "downloads/combined_audio.mp3"

with open(combined_file, "wb") as combined:
    for file in ayah_files:
        with open(file, "rb") as audio:
            shutil.copyfileobj(audio, combined)

for file in ayah_files:
    if file != combined_file:
        try:
            os.remove(file)
            print(f"Deleted: {file}")
        except Exception as e:
            print(f"Failed to delete {file}: {e}")
length = sum(ayah_lengths)
print(sum(ayah_lengths))
videoclip = VideoFileClip("downloads/veedio_original.mp4")
new_clip = videoclip.without_audio().subclip(0, length + 2)
new_clip.write_videofile("downloads/veedio_silent.mp4")

video_1 = VideoFileClip("downloads/veedio_silent.mp4")
y = 0
start_time = 0
text_clips = []
for i, translation in enumerate(x):
    text_clip = TextClip(translation, fontsize=36, color='white', bg_color='black', method='caption', size=(video_1.size[0], 180), interline=4).set_start(start_time).set_duration(ayah_lengths[i]).set_pos('bottom')
    text_clips.append(text_clip)
    start_time = ayah_lengths[i] + start_time
video_1 = CompositeVideoClip([video_1, *text_clips])


audioclip = AudioFileClip("downloads/combined_audio.mp3")
final = video_1.set_audio(audioclip)
final.write_videofile("downloads/finale_fixed.mp4", codec="libx264", audio_codec="aac")
try:
    video_1.close()
    videoclip.close()
except:
    print("0")
temp_videos = [
    "downloads/veedio_original.mp4",
    "downloads/veedio_silent.mp4",
    "downloads/combined_audio.mp3"
]

for file in temp_videos:
    if os.path.exists(file):
        try:
            os.remove(file)
            print(f"Deleted: {file}")
        except Exception as e:
            print(f"Failed to delete {file}: {e}")