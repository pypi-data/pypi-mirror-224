import pydub
from pydub import AudioSegment
import os

def get_mp3_durations(folder_path):
    durations = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.mp3'):
            file_path = os.path.join(folder_path, file_name)
            audio = AudioSegment.from_file(file_path, format="mp3")
            duration_seconds = audio.duration_seconds
            duration_minutes = int(duration_seconds // 60)
            duration_seconds_remainder = int(duration_seconds % 60)
            duration_string = f"{duration_minutes:02}:{duration_seconds_remainder:02}"
            durations.append((file_name, duration_string))
    
    return durations

def main():
    folder_path = input("Enter the folder path: ")
    mp3_durations = get_mp3_durations(folder_path)

    for file_name, duration_string in mp3_durations:
        print(f"{file_name}: {duration_string}")

if __name__ == "__main__":
    main()
