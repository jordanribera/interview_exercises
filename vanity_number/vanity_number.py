import itertools

letters_dict = {
	'2': ['a', 'b', 'c'],
	'3': ['d', 'e', 'f'],
	'4': ['g', 'h', 'i'],
	'5': ['j', 'k', 'l'],
	'6': ['m', 'n', 'o'],
	'7': ['p', 'q', 'r', 's'],
	'8': ['t', 'u', 'v'],
	'9': ['w', 'x', 'y', 'z']
}

def is_word(test_string):
	#placeholder for imaginary function
	return True

def get_permutations(number_string):
	digits = list(number_string)

	possibilities = []
	for digit in digits:
		possibilities.append(letters_dict[digit])

	permutations = [''.join(p) for p in itertools.product(*possibilities)]

	return permutations

the_number = '234'
the_perms = get_permutations(the_number)

for this_perm in the_perms:
	if is_word(this_perm) == False:
		the_perms.remove(this_perm)

print(the_perms)
print('there are ' + str(len(the_perms)) + ' permutations.')