#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name):
	first_name = name.split('-')[0]
	lowercase = first_name.lower()
	capitalize = lowercase.capitalize()
	# sinon
	# capitalize = first_name[0].upper + first_name[1:].lower

	return capitalize

def get_random_sentence(animals, adjectives, fruits):
	rand_animals = random.choice(animals)
	rand_adj = random.choice(adjectives)
	rand_fruits = random.choice(fruits)
	sentence = ('Aujourd’hui, j’ai vu un ' + rand_animals + ' s’emparer d’un panier ' + rand_adj + ' plein de ' + rand_fruits + '.')
	return sentence

def encrypt(text, shift):
	new_str = ''
	for letter in text:
		if ord(letter.upper()) > 64:
			if ord(letter.upper()) > (ord('Z') - shift):
				new_str += chr(ord(letter.upper()) - (26 - shift))
			else:
				new_str += chr(ord(letter.upper()) + shift)
		else:
			new_str += letter
	return new_str

def decrypt(encrypted_text, shift):
	new_str = ''
	for letter in encrypted_text:
		if ord(letter) > 64:
			if ord(letter) < (ord('A') + shift):
				new_str += chr(ord(letter) + (26 - shift))
			else:
				new_str += chr(ord(letter) - shift)
		else:
			new_str += letter
	return new_str


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
