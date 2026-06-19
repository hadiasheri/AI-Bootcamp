



import numpy as np

from pydub import AudioSegment
from matplotlib import pyplot as plt


audio = AudioSegment.from_mp3("./data/morse.mp3")
samples = list(audio.get_array_of_samples())

samples_int16 = (np.array(samples)/2).astype(np.int16)[85000:]


audio = AudioSegment(
    samples_int16.tobytes(),
    frame_rate=44100,
    sample_width=2,
    channels=1
)

audio.export("output.mp3", format="mp3")

