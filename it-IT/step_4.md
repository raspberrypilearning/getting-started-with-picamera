## How to control the Camera Module via the command line

Now your Camera Module is connected and the software is enabled, try out the command line tools `raspistill` and `raspivid`.

- Open a terminal window by clicking the black monitor icon in the taskbar:

![Open terminal](images/open-terminal-annotated.png)

- Type in the following command to take a still picture and save it to the Desktop:

```bash
raspistill -o Desktop/image.jpg
```

![raspistill command entered into the terminal](images/raspistill-image.png)

- Press <kbd>Enter</kbd> to run the command.

When the command runs, you can see the camera preview open for five seconds before a still picture is taken.

- Look for the picture file icon on the Desktop, and double-click the file icon to open the picture.

    ![Image on Desktop](images/desktop-annotated.png)

By adding different options, you can set the size and look of the image the `raspistill` command takes.

- For example, add `-h` and `-w` to change the height and width of the image:

```bash
raspistill -o Desktop/image-small.jpg -w 640 -h 480
```

- Now record a video with the Camera Module by using the following `raspivid` command:

```bash
raspivid -o Desktop/video.h264
```

- In order to play the video file, double-click the `video.h264` file icon on the Desktop to open it in VLC Media Player.

For more information and other options you can use with these commands, read the [documentation for raspistill](https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md) and the [documentation for raspivid](https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspivid.md).
