from pytube import YouTube
from pydub import AudioSegment
import os


def download_audio(url, output_path="D:/producao/tracks to sample"):
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
    audio_path = audio.download(output_path)
    sound = AudioSegment.from_file(audio_path)
    sound.export(f'{output_path}/{yt.title}.mp3', format='mp3')
    os.remove(f'{output_path}/{yt.title}.webm')
    print(f"Audio downloaded: {yt.title}")


if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_audio(video_url)

