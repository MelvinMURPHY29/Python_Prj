import pyttsx3

engine = pyttsx3.init('sapi5')
engine.startLoop(False)   # background loop start

while True:
    text = input("Say something (type 'exit' to quit): ").strip()

    if text.lower() == 'exit':
        engine.say("Bye bye, have a nice day")
        engine.iterate()   # queue process 
        break
    elif text == "":
        engine.say("try again")
        engine.iterate()
    else:
        engine.say(text)
        engine.iterate()

engine.endLoop()

