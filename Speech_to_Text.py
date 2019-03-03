import speech_recognition as sr

r = sr.Recognizer()


test = sr.AudioFile('welcome1.wav')
with test as source:
	audio = r.record(source)

try:
	print("output is :" + r.recognize_google(audio))
except sr.UnknownValueError:
	print("google count not understand the langauge")
except sr.RequestError as e:
	print("error is {0}".format(e))
