import speech_recognition as sr

def transcribe_and_chunk(audio_file_path, words_per_chunk=8):
   
    recognizer = sr.Recognizer()
    
    print(f"Reading audio file: {audio_file_path}...")
    
    
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
        
        try:
            print("Transcribing audio to text...")
            # Using Google's free Web Speech API (Built into the library, no keys needed)
            full_text = recognizer.recognize_google(audio_data)
            print("\n--- Full Transcription Successful ---")
            
           
            words = full_text.split()
            chunks = []
            
       
            for i in range(0, len(words), words_per_chunk):
                chunk = " ".join(words[i:i + words_per_chunk])
                chunks.append(chunk)
            
            
            print("\n--- Formatted Subtitle Chunks ---")
            for index, chunk in enumerate(chunks, 1):
                print(f"Block [{index}]: {chunk}")
                
     
            with open("formatted_transcript.txt", "w") as f:
                for index, chunk in enumerate(chunks, 1):
                    f.write(f"Block [{index}]: {chunk}\n")
            print("\nSaved formatted text to 'formatted_transcript.txt'!")
            
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; check your internet connection. {e}")

