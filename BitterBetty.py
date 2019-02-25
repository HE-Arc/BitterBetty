# coding: utf-8
from subprocess import call

class BitterBetty:
	"""BitterBetty is a bitter bot"""

	def __init__(self):
		"""Construct Betty"""
		pass

	def _speak_(self, phrase):
		"""
		Make Betty speaks using flite

		:param phrase: text that Betty will say
		"""
		call(["flite", "-voice", "slt", "-t", phrase])

	def ola(self):
		self._speak_("Ola Amiga, how are you ?")


if __name__ == "__main__":
	betty = BitterBetty()
	betty.ola()
