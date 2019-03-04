# coding: utf-8
from subprocess import call
import distutils.spawn

class FliteSpeaker:        

    @classmethod
    def fliteAvaible(cls):
        return distutils.spawn.find_executable("flite")

    @classmethod
    def speak(cls, phrase):
        if cls.fliteAvaible():
            call(["flite", "-voice", "slt", "-t", phrase])
            return True
        return False

if __name__ == "__main__":
    if not FliteSpeaker.speak("Ola"):
        print("Flite is not avaible on this plateform")