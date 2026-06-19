
import numpy as np
from pydub import AudioSegment
from matplotlib import pyplot as plt


def read_audio(path):
    audio = AudioSegment.from_mp3(path)
    return list(audio.get_array_of_samples())



short = read_audio("./data/short-beep.mp3")
long = read_audio("./data/long-beep.mp3")



msg = input("enter your message: ")



morse = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..'
}



full_track = []

for char in msg.upper():
    for m_code in morse[char]:
        if m_code == ".":
            # short-beep
            full_track.extend(short)
        if m_code == "-":
            # long beep
            full_track.extend(long)



samples_int16 = (np.array(full_track)/2).astype(np.int16)[85000:]

audio = AudioSegment(
    samples_int16.tobytes(),
    frame_rate=44100,
    sample_width=2,
    channels=1
)

audio.export("output.mp3", format="mp3")



        