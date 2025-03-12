# Quran Video Generator

This Python script creates a video with Quranic recitations and translations overlaid on a background video. It downloads audio recitations, generates subtitles, and synchronizes everything into a final video.

## Features
- Download Quranic recitations from a user-selected reciter
- Fetch Quranic translations for specified ayahs
- Download a random video from a YouTube playlist
- Overlay translations as text onto the video
- Synchronize audio recitation with video and subtitles
- Clean up temporary files after execution

## Requirements
- Python 3.10+
- moviepy==1.0.3
- mutagen==1.47.0
- pydub==0.25.1
- pytubefix==8.12.2
- Requests==2.32.3
- ImageMagick (with path configured in the script)

## Setup
1. Install required libraries:

```
pip install requests pydub pytubefix moviepy mutagen
```

2. Install ImageMagick and ensure the `magick.exe` path is set correctly in the script:

```python
change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})
```

## How to Use
1. Run the script.
2. Choose a reciter from the provided list (1–11).
3. Enter the Surah number and Ayah number.
4. Specify how many Ayahs you want to listen to, or type "no" for just one Ayah.
5. The script will:
   - Fetch translations and recitations
   - Download and process a random video
   - Combine the video, audio, and subtitles
   - Save the final video as `downloads/finale_fixed.mp4`

## Output
- **downloads/finale_fixed.mp4**: Final synchronized video with recitation and subtitles

## Cleanup
The script automatically deletes temporary files after execution:
- Original and silent versions of the video
- Combined audio file
- Individual Ayah audio files

## Notes
- Ensure your YouTube playlist URL is correct.
- Confirm ImageMagick is properly installed and configured.
- Handle API rate limits when fetching data from the Quran API.

## License
This project is licensed under the MIT License.

