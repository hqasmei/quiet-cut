from tkinter import *
from tkinter import filedialog, simpledialog
from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub.playback import play
import os

root = Tk()
root.title("Audio Clipper")
root.geometry("200x200")


def select_file():
    # Get the audio file path
    file_path = filedialog.askopenfilename()

    # Load the audio file
    audio_file = AudioSegment.from_file(file_path, format="m4a")

    # Split the audio file into clips
    audio_clips = split_on_silence(audio_file, min_silence_len=500, silence_thresh=-50)

    # Ask the user to enter a folder name to save the audio clips
    folder_name = simpledialog.askstring("Folder Name", "Enter a name for the output folder:")

    # Create the output folder
    output_dir = os.path.join(os.getcwd(), folder_name)
    os.makedirs(output_dir, exist_ok=True)

    # Display each clip and ask the user to name it before exporting it to the output folder
    for i, clip in enumerate(audio_clips):
        clip_label = Label(root, text=f"Clip {i + 1}", font=("Helvetica", 14))
        clip_label.pack()

        # Create a temporary file to play the clip
        temp_file = os.path.join(output_dir, f"clip_{i}.wav")
        clip.export(temp_file, format="wav")

        # Load the clip into a new AudioSegment object and play it
        clip_audio = AudioSegment.from_file(temp_file, format="wav")

        def play_clip():
            # Load the clip into a new AudioSegment object and play it
            clip_audio = AudioSegment.from_file(temp_file, format="wav")
            play(clip_audio)

        play_button = Button(root, text="Play", command=play_clip)
        play_button.pack()

        # Ask the user to enter a name for the clip
        clip_name = simpledialog.askstring(f"Clip {i + 1} Name", "Enter a name for the clip:")
        if clip_name:
            # Export the clip to the output folder using the entered name
            output_file = os.path.join(output_dir, f"{clip_name}.wav")
            clip.export(output_file, format="wav")

        # Remove the temporary file and the play button
        os.remove(temp_file)
        play_button.destroy()


select_file_button = Button(root, text="Select File", command=select_file, pady=20, padx=20)
select_file_button.pack(pady=20)

root.mainloop()
