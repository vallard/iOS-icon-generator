# iOS-icon-generator

Python tool to generate all the icon sizes you need for an 
iOS application.  

## Prerequisites

I use this on a Mac.  You'll need ImageMagick 

```
brew install imagemagick
```
as well as python. 

## Usage

```
makeicons.py <image name>.png
```

### Sample Output
```
$ ./makeicons.py icon\@512.png 
Making icon icon@29.png
Making icon icon@58.png
Making icon icon@87.png
Making icon icon@40.png
Making icon icon@80.png
Making icon icon@120.png
Making icon icon@60.png
Making icon icon@120.png
Making icon icon@180.png
Making icon icon@76.png
Making icon icon@152.png
Making icon icon@228.png
```


These images can then be placed in the iOS application. 

