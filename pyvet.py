import openai
import os
from gtts import gTTS
import time
import pygame
import speech_recognition as sr


def initialize_openai_api():
    openai.api_key = "<API KEY>"
    

def get_model_engine():
    return "text-davinci-003"


def get_prompt(r):
    with sr.Microphone() as source:
        print("Você:")
        audio = r.listen(source)

    try:
        prompt = r.recognize_google(audio, language='pt-BR')
    except sr.UnknownValueError:
        prompt = "Não foi possível entender o que você disse."
    except sr.RequestError as e:
        prompt = "Erro ao chamar o serviço de reconhecimento de fala: {0}".format(
            e)

    return prompt


def get_answer(prompt, model_engine):
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return completion.choices[0].text


def save_audio_response(answer):
    if os.path.exists("tmp.mp3"):
        os.remove("tmp.mp3") 
    
    tts = gTTS(text=answer, lang='pt', slow=False, )
    tts.save("tmp.mp3")
    
    
def play_audio_response():
    pygame.init()
    pygame.mixer.music.load("tmp.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)
    pygame.quit()


def chat():
    initialize_openai_api()
    model_engine = get_model_engine()
    r = sr.Recognizer()
    
    save_audio_response("Oi, eu me chamo pivete, sua inteligência artificial, faça uma pergunta")
    play_audio_response()

    while True:
        prompt = get_prompt(r)
        if "sair do pivete" in prompt:
            break; 
        
        answer = get_answer(prompt, model_engine)
        save_audio_response(answer)
        play_audio_response()
        

if __name__ == "__main__":
    chat()
