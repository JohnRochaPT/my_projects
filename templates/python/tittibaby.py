"""
A function with several helpers.

The primary function in this module is str_to_seconds.  The functions get_hours, 
get_minutes, and get_seconds are all helper functions that are used to implement 
this function.  They should implemented in the order listed.

Author: John Rocha
Date: 09/20/2024
"""

import cowsay
import pyttsx3


def main():
    engine = pyttsx3.init()
    this = 'Willy willy willy WILLY, Wonka you are my ittel titi baby'
    cowsay.cow(this)
    engine.say(this)
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    engine.say('Willy willy willy WILLY, Wonka you are my ittel titi baby')
    engine.runAndWait()


    # > Call main ONLY when intended
if __name__ == '__main__':
    main()
