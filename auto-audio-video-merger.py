import os
import subprocess

# Get the name of the parent directory
parent_dir = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

# Create the output directory name
output_dir_name = f"{parent_dir}output"

# Create the output directory if it does not exist
output_dir = os.path.join('.', output_dir_name)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get a list of all mp3 and mp4 files in the current directory
mp3_files = [file for file in os.listdir('.') if file.endswith('.mp3')]
mp4_files = [file for file in os.listdir('.') if file.endswith('.mp4')]

# Find pairs of files with matching names (excluding the extension)
matching_files = set(f[:-4] for f in mp3_files) & set(f[:-4] for f in mp4_files)

# Process each pair of files with matching names
for base_name in matching_files:
    mp3_file = f"{base_name}.mp3"
    mp4_file = f"{base_name}.mp4"
    output_file = f"{base_name}_output.mp4"
    output_path = os.path.join(output_dir, output_file)

    # Reduce the volume of the video to 15% and merge the mp3 audio, then render to a new file
    subprocess.run([
        'ffmpeg',
        '-i', mp4_file,
        '-i', mp3_file,
        '-c:v', 'copy',
        '-filter_complex', '[0:a]volume=0.15[a1];[a1][1:a]amerge=inputs=2[aout]',
        '-map', '0:v',
        '-map', '[aout]',
        '-c:a', 'aac',
        '-strict', '-2',  # This option may be needed if using an older version of ffmpeg
        output_path
    ])

    print(f"Processing complete and saved to directory: {output_path}")

