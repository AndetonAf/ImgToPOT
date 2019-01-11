# Image to Image with POT (Power Of Two)

Simple program to put the images in POT

## Getting Started

if you don't know what is "Power Of Two" :

https://software.intel.com/en-us/articles/opengl-performance-tips-power-of-two-textures-have-better-performance
https://www.katsbits.com/tutorials/textures/make-better-textures-correct-size-and-power-of-two.php

## How working
When executing the program select all the photos that you want to transform into "POT" after that all the Images will be saved in a new folder created where the program is called "POT"

### ToPOT.exe
Compiled with

```
pyinstaller --onefile --windowed ToPOT.py
```

Download : [ToPOT.exe](ToPot.exe)

### Examples

Without POT

[//]: # (Image References)
[image1]: nebulosa2.jpg "630x354"
![alt text][image1]

With POT

[//]: # (Image References)
[image2]: ./POT/nebulosa2.png " 1024x512"
![alt text][image2]

### Can also help you
Script to slice Images in Unity3d
https://gist.github.com/shadesbelow/8a6ddc54db795241f3cff539db6ea487
