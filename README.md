# iOS-icon-generator

Python tool to generate all the icon sizes you need for an 
iOS application.  

## Mac Installation Instructions

You'll need ImageMagick and Python.

```
brew install imagemagick
```
as well as python. 

Then to use its simple:
```
git clone https://github.com/vallard/iOS-icon-generator.git
cp makeicons.py <your image directory>/
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

