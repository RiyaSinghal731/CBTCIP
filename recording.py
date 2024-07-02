import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wai

f = 44100
Time = 10

recording = sd.rec(int( f *Time ) , samplerate= f , channels= 2)
print("your sound is being recorded now:")
sd.wait()
wai.write("rec_1.wav" , recording , f , sampwidth = 2)
print("Your sound is recorded")
