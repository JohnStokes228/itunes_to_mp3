# itunes_to_mp3
convert itunes music library to mp3 format, because for some reason they arent default compatible with mp3 players - what a scam :(

general design:

    - look in itunes folder for music, get list of albums / songs and shit
    - then parallelise for each album:
        - convert each track to mp3
        - delete m4a file
        - save to new album folder
