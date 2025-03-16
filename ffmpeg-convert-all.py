import ffmpeg
import argparse

parser = argparse.ArgumentParser(prog="ffmpeg-test-convert",
    description="Take input audio file and convert it to all Android encoding options")

parser.add_argument('filename')
args = parser.parse_args()

codec_formats={
    "aac": {
        "containers": [
            "3gp",
            "m4a",
            "mp4",
            "aac"
        ]
    },
    "amr_nb": {
        "containers": [
#            "3ga", # ffmpeg does not appear to recognize .3ga
            "3gp",
            "amr"
        ],
        "args": {
            "ar": 8000,
            "ab": "12.2k",
            "ac": 1,
        }
    },
    "amr_wb": {
        "containers": [
#            "3ga", # ffmpeg does not appear to recognize .3ga
            "3gp",
            "amr"
        ],
        "args": {
            "ar": 16000,
            "ac": 1,
        }


    },
    "flac": {
        "containers": [
            "flac",
            "mp4",
        ]

    },
    "libopus": {
        "containers": [
            "ogg"
        ]

    },
}

for codec, formats in codec_formats.items():
    print(codec + " is the current codec")
    for container in formats["containers"]:
        print(container + "is the current container")

        stream = ffmpeg.input(args.filename)

        if "args" in formats.keys():
            stream = ffmpeg.output(stream, 
                "outfiles/" + codec + "--" + container + "." + container, 
                acodec=codec, **formats["args"])
        else:
            stream = ffmpeg.output(stream, 
                "outfiles/" + codec + "--" + container + "." + container, 
                acodec=codec)

        ffmpeg.run(stream)


