def record_for_time(file, time):
    # import required librariesl
    import sounddevice as sd
    import wavio as wv
    
    # Sampling frequency
    freq = 44100
    
    # Start recorder with the given values 
    # of duration and sample frequency
    recording1 = sd.rec(int(time * freq), samplerate=freq, channels=1)
    
    # Record audio for the given number of seconds
    sd.wait()

    recording2 = sd.rec(int(time * freq), samplerate=freq, channels=1)

    sd.wait()

    recording = recording1 + recording2


    
    # Convert the NumPy array to audio file
    wv.write(file, recording, freq, sampwidth=2)
