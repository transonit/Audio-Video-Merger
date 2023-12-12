# Audio-Video-Merger Script

## Description
This script is designed to automate the process of merging MP3 audio files with MP4 video files. It reduces the volume of the video to 15% and merges the MP3 audio, then renders the output to a new MP4 file. The output files are automatically organized into a directory named after the parent directory with "output" appended to it.

## Requirements
- Python 3.x
- FFmpeg installed and added to the system's PATH

## Usage
1. Place the script in the same directory as your MP3 and MP4 files.
2. Run the script using Python:
   ```shell
   python audio_video_merger.py
The script will process all matching MP3 and MP4 files (files with the same name excluding the extension) and save the merged output in the designated output directory.
## Output Directory
The output files will be saved in a directory named <parent_dir_name>-output, where <parent_dir_name> is the name of the parent directory of the script.

## Note
The script assumes that for each MP4 file, there is a corresponding MP3 file with the same base name.
The script will not overwrite existing files in the output directory. If a file with the same name already exists, you will need to manually handle it.
## License
This project is open-sourced under the MIT License. See the LICENSE file for more information.

## Contributions
Contributions are welcome! Please feel free to submit a pull request or create an issue for any bugs or feature requests.

## Acknowledgments
Thank you for using this script. If you find it helpful, please consider starring the repository on GitHub.
