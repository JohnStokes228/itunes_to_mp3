# itunes_to_mp3
convert itunes music library to mp3 format, because for some reason they arent default compatible with mp3 players - what a scam :(

general design:

    - look in itunes folder for music, get list of albums / songs and shit
    - then parallelise for each track:
        - convert each track to mp3 if it hasnt already been done
        - delete the original m4a file
        - save to new album folder, matching original structure

code could do with an logger of some kind and maybe some form of actual packaging as atm its a bit of a wild west type sitch. runs though which i guess is a plus
