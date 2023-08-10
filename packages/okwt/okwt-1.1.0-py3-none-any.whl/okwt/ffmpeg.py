import subprocess
import numpy as np


def execute_ffmpeg_command(command):
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    output, error = process.communicate()
    return output, error


def ffmpeg_process_video(input_file, output_file):
    # Extract frames from input video
    command = [
        "ffmpeg",
        "-i",
        input_file,
        "-f",
        "image2pipe",
        "-pix_fmt",
        "rgb24",
        "-vcodec",
        "rawvideo",
        "-",
    ]
    output, error = execute_ffmpeg_command(command)

    # Process individual frames
    frames = np.frombuffer(output, dtype="uint8")
    # Do your processing on `frames` (e.g., convert to grayscale, apply filters, etc.)

    # Compose processed frames into a new video
    command = [
        "ffmpeg",
        "-y",
        "-f",
        "rawvideo",
        "-vcodec",
        "rawvideo",
        "-s",
        "widthxheight",
        "-pix_fmt",
        "rgb24",
        "-r",
        "30",  # Set desired frame rate
        "-i",
        "-",
        "-c:v",
        "libx264",
        "-pix_fmt",
        "yuv420p",
        output_file,
    ]
    execute_ffmpeg_command(command)


# Example usage
input_file = "input.mp4"
output_file = "output.mp4"
ffmpeg_process_video(input_file, output_file)
