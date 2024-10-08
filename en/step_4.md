## How to control the Camera Module via the command line

Now your Camera Module is connected and the software is enabled, try out the command line tools `rpicam-still` and `rpicam-vid`.

--- task ---
- Open a terminal window by clicking the black monitor icon in the taskbar:

![Open terminal](images/open-terminal-annotated.png)

--- /task ---

--- task ---
- Type in the following command to take a still picture and save it to the Desktop:

```bash
rpicam-still -o ~/Desktop/image.jpg
```
--- /task ---

--- task ---
- Press <kbd>Enter</kbd> to run the command.
--- /task ---

When the command runs, you can see the camera preview open before a still picture is taken. 

--- task ---
- Look for the picture file icon on the Desktop, and double-click the file icon to open the picture.

![Image on Desktop](images/desktop-annotated.png)
--- /task ---

By adding different options, you can set the size and look of the image the `rpicam-still` command takes.

--- task ---
- Add `--width` and `--height` to change the dimensions of the image:

```bash
rpicam-still -o ~/Desktop/image-small.jpg --width 640 --height 480
```
--- /task ---

--- task ---
- Now record a video with the Camera Module by using the following `rpicam-vid` command:

```bash
rpicam-vid -o ~/Desktop/video.mp4
```
--- /task ---

--- collapse ---

---
title: I'm not using a Raspberry Pi 5
---

You will need to use `libav`

```bash
rpicam-vid -t 10000 --codec libav --libav-format mp4 -o ~/Desktop/video.mp4
```

**Tip:** The `10000` is the number of milliseconds to record

--- /collapse ---

--- task ---
- Play the video file by typing the following command:

```bash  
vlc ~/Desktop/video.mp4
```
Alternatively, double-click the `video.mp4` file icon on the desktop.

--- /task ---

For more information and other options you can use with these commands, read the [documentation for rpicam-still](https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-still) and the [documentation for rpicam-vid](https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-vid).
