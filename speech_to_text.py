# Python program to translate
# speech to text and text to speech

def speech_to_text(file):
    # Initialize recognizer class (for recognizing the speech)
    import speech_recognition as sr
    r = sr.Recognizer()

    # Reading Audio file as source
    # listening the audio file and store in audio_text variable

    with sr.AudioFile(file) as source:
        
        audio_text = r.listen(source)
        
    # recognize_() method will throw a request error if the API is unreachable, hence using exception handling

        # using google speech recognition
        r.adjust_for_ambient_noise(source)
        text = r.recognize_sphinx(audio_text)
        '''try:
            text = r.recognize_google(audio_text)
        except:
            try:
                text = r.recognize_bing(audio_text)
            except:
                try:
                    text = r.recognize_ibm(audio_text)
                except:
                    try:
                        text = r.recognize_houndify(audio_text)
                    except:
                        try:
                            text = r.recognize_sphinx(audio_text)
                        except:
                            try:
                                text = r.recognize_wit(audio_text)
                            except:
                                try:
                                    text = r.recognize_google_cloud(audio_text)
                                except:
                                    try:
                                        text = r.recognize_sphinx(audio_text)
                                    except:
                                        print("ERROR: Speech recognition failed")
                                        exit()'''
        return text
        