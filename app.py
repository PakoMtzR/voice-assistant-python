import pyttsx3
import speech_recognition as sr
import pywhatkit
import pyjokes
import webbrowser
import datetime
import wikipedia

# Nombre de los dias de la semana
week_day_dict = {
    0: "Lunes",
    1: "Martes",
    2: "Miercoles",
    3: "Jueves",
    4: "Viernes",
    5: "Sabado",
    6: "Dominguito"
}

month_dict = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

# Creamos objeto para el reconocimiento de voz
recognizer = sr.Recognizer()

wikipedia.set_lang("es")

# Funcion para escuchar audio del microfono y convertirlo a texto
def transform_audio_into_text():
    with sr.Microphone() as source:
        print("Comienza a hablar...")
        recognizer.pause_threshold = 0.8
        # recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        request = recognizer.recognize_google(audio, language="es-ES")
        return request
    except sr.UnknownValueError:
        print("[Eva]: no mames no se te entiende nada, hablas de la chingada, haz el pinche ejercicio del lapiz")
        return "Sigo escuchando"
    except sr.RequestError:
        print("[Eva]: no mames no se te entiende nada, hablas de la chingada, haz el pinche ejercicio del lapiz")
        return "Sigo escuchando"
    except:
        print("[Eva]: no mames no se te entiende nada, hablas de la chingada, haz el pinche ejercicio del lapiz")
        return "Sigo escuchando"

def speak(message):
    print("[Eva]: " + message)
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

# Funcion para saludar el usuario
def initial_greeting():
    message = "Hola soy Eva, ¿En qué te puedo ayudar?"
    speak(message)

def ask_day():
    day = datetime.date.today()     # Creamos una variable con la informacion de la fecha
    week_day = day.weekday()        # Consultamos el dia de la semana
                                    # Retorna un numero ejem. 1-->martes, 5-->sabado
    
    return f"Hoy es {week_day_dict[week_day]} {day.day} de {month_dict[day.month]}"

def ask_time():
    time = datetime.datetime.now()
    return f"Son las {time.hour} {time.minute}"

def run_assistant():
    # Hacemos el saludo inicial
    initial_greeting()

    run = True
    while run:
        my_request = transform_audio_into_text().lower()
        print("[Tú]: " + my_request)

        if "abre youtube" in my_request:
            speak("ok bastardo, abriendo youtube")
            webbrowser.open("https://www.youtube.com")
            continue

        elif "abre el navegador" in my_request:
            speak("abriendo el navegador")
            webbrowser.open("https://google.com")
            continue

        elif "a qué estamos" in my_request:
            speak(ask_day())
            continue

        elif "qué hora es" in my_request:
            speak(ask_time())
            continue

        elif "investiga" in my_request:
            my_request = my_request.replace("investiga", "")
            speak(f"De acuerdo con wikipedia: {wikipedia.summary(my_request, sentences=1)}")
            continue

        elif "busca" in my_request:
            my_request = my_request.replace("busca", "")
            pywhatkit.search(my_request)
            speak("Esto fue lo que encontre")
            continue

        elif "chiste" in my_request:
            speak(pyjokes.get_joke("es"))
            continue

        elif "reproduce" in my_request:
            pywhatkit.playonyt(my_request)
            speak("Reproduciendo")
            continue

        elif "dile algo al john" in my_request:
            speak("ese puto john solo dice mamadas, mejor que se aleje")
            continue
        
        elif "dile algo al manolo" in my_request:
            speak("que se caye ese pinche telescopio")
            continue

        elif "dile algo a la gordis" in my_request:
            speak("kúaaaass,kúass,kúass,kúass, no le sabe")

        elif "adiós" in my_request:
            break
        
run_assistant()