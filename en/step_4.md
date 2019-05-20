## Using the camera

Now your camera is connected and the software is enabled, you can get started by trying out the command line tools for the camera.

- Open a terminal window by clicking the black monitor icon in the taskbar:

![Open terminal](images/open-terminal-annotated.png)

- Enter the following command to take a still picture using the camera and save it to the desktop:

```bash
raspistill -o Desktop/image.jpg
```

![raspistill command entered into the terminal](images/raspistill-image.png)

- Run the command and you'll see the camera preview open for 5 seconds before capturing a still picture. 

- You'll see your photo appear on the Desktop. Double-click the file icon to open it:

    ![Image on Desktop](images/desktop-annotated.png)

- The `raspistill` command can accept many different options allowing you to modify the output such as `-h` and `-w` to change the height and width of the image:

```bash
raspistill -o Desktop/image-small.jpg -w 640 -h 480
```

- The `raspivid` command can be used to take video with the camera:

```bash
raspivid -o Desktop/vid.h264
```

- To play the video, double click the `vid.h264` file on the Desktop to open it in VLC Media Player.

For more information on the command line tools see the documentation for [raspistill](https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md) and [raspivid]([path](https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspivid.md)).
