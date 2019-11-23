# Moonlings-Python-Scripts
Python script written to make image editing

## Usage

### Resize Texture
Resize Texture is used for quickly resizing images, new sizes have to be a divisible by 2. **Requires Pillow**

drag the image you want to resize onto the `Resize Texture.bat`. after that you will be promted to enter a new Hight, Width, and resample method. Once all of those have been chosen the script will overwrite the input image with the new resized image.

You can also run to `Batch Resize Texture.bat` to resize all .png files in the current folder.
Other script such as Icon Switch, Icon WiiU, and Make Emote, resize an image to a predefined size. Those being, Icon Switch = 166x166(used for BOTW icons), Icon WiiU = 96x96(used for BOTW icons), and Make Emote = 256x256(For use with discord).

### Channel Split and Merge
Channel Split and Merge is used to an Alpha channel from an image and then re add it later. **Requires Pillow and Numpy**
#### Channel Split
Simply drag the image you want onto the `Channel_Split.py`, it will then output and `_RGB.png` and a `_A.png`.
the RGB image will have the RGB channels and a solid Alpha channel, where as the A image will have the Alpha channel copied into the RGB channels and a solid Alpha channel for easy editing.
#### Channel Merge
Once your done editing the RGB and or A images you'll want to put them back together. Simply drag both the RGA and A image onto the `Channel_Merge.py` script and it will output the image overwriting the original(assuming you haven't renamed anything). 
How this work is it uses the frist argument and the RGB and the second as the Alpha, **So make sure to drag the RGB on first**.

### Convert to RGBA PNG
Converts the image into a .png with the RGBA format. **Requires Pillow**

### Dump RGBA
Dumps the R, G, B, and A channels into sperate images. **Requires Pillow**

### Channel Choose
Used to pick and choose what image channels you want. **Requires Pillow and Numpy**

Drag the image onto and bat and input the new vaule for each channel(0 - 255). anything over 255(256+) the image's existing channel will be used.
