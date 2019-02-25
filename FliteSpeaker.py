# coding: utf-8
from subprocess import call

class FliteSpeaker:

    @classmethod
    def speak(cls, phrase):
        call(["flite", "-voice", "slt", "-t", phrase])

if __name__ == "__main__":
    FliteSpeaker.speak("Ola")