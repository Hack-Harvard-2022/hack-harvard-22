print("hello")
# import required librariesl
import sounddevice as sd
import wavio as wv
  
# Sampling frequency
freq = 44100
  
# Recording duration
duration = int(input("Enter time duration in seconds: "))
print("Recording...")
  
# Start recorder with the given values 
# of duration and sample frequency
recording = sd.rec(int(duration * freq), 
                   samplerate=freq, channels=1)
  
# Record audio for the given number of seconds
sd.wait()
  
# Convert the NumPy array to audio file
wv.write("recording1.wav", recording, freq, sampwidth=2)

print("finished... please check your output file")
