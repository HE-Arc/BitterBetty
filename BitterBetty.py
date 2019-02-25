# coding: utf-8
from subprocess import call
from FliteSpeaker import FliteSpeaker

class BitterBetty:
	"""BitterBetty is a bitter bot"""

	def __init__(self):
		"""Construct Betty"""
		pass

	def speak(self, phrase):
		"""
		Make Betty speaks using FliteSpeaker

		:param phrase: text that Betty will say
		"""
		FliteSpeaker.speak(phrase)

	def ola(self):
		FliteSpeaker.speak("Ola Amiga, how are you ?")


if __name__ == "__main__":
	betty = BitterBetty()
	betty.ola()
