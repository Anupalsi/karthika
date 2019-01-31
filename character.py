char=input()
new=char.lower()
if char in 'aeiou':
	print("Vowel")
elif char in 'bcdfghjklmnpqrstvwxyz'	:
	print("Consonant")
else:
	print("invalid")
