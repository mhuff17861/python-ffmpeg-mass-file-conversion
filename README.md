# Python Script Setup Instructions

## Install ffmpeg

If you want to use the script in full, you will need to compile ffmpeg in full using the instructions below (which assume you are on Ubuntu, sorry if you're not ❤ ):

- Retrieve the source code from [ffmpeg](https://ffmpeg.org/)
- Run `apt install libopencore-amrnb-dev libvo-amrwbenc-dev libopus-dev`
- In the source folder, run `./configure --enable-libopencore-amrnb --enable-libvo-amrwbenc --enable-libopus --enable-version3`
- `make`
- `make install`

If you do not want to go through the hassle of compiling ffmpeg yourself, the ubuntu package available via apt covers most of the codecs. Just comment out the options for amr_nb and amr_wb in the python script file.

## Setup python virtual environment

- `python3 -m venv ffmpeg-test`
- `source ffmpeg-test/bin/activate`
- `pip install ffmpeg-python`

## Download a test audio file

You can probably find a short one from [freesound.org](https://freesound.org)

## Get script file

Place the following code in `whatever-name-you-want.py`

## Run it

`python ./ffmpeg-convert-all.py filename.ext`
