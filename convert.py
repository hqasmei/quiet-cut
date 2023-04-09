import os

# Define the input and output directories
input_dir = "/Users/hosnaqasmei/Desktop/clipper/Verbs"
output_dir = "/Users/hosnaqasmei/Desktop/clipper/Verbs/output"

# Loop through all files in the input directory
for filename in os.listdir(input_dir):
    # Check if the file is a .wav file
    if filename.endswith(".wav"):
        # Generate the input and output file paths
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + ".m4a")

        # Execute the ffmpeg command
        os.system(f"ffmpeg -i {input_path} -c:a aac -b:a 256k {output_path}")
