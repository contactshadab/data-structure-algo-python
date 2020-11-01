'''
Source: AlgoExpert
Given a non-empty string of lowercase letters and a non-negative integer
representing a key, write a function that returns a new string obtained by
shifting every letter in the input string by k positions in the alphabet,
where k is the key.
Note that letters should "wrap" around the alphabet; in other words, the
letter z shifted by one returns the letter a.

Sample Input
string = "xyz"
key = 2

Sample Output
"zab"
'''

# Solution 1
# Run time Complexity: O(n), Space Complexity: O(n)


def transform_1(string, key):
    result = []
    new_key = key % 26
     ascii_a = 97
      ascii_z = 122
       for ch in string:
            new_ch = ord(ch) + new_key
            new_ch = new_ch if new_ch <= 122 else (
                ascii_a-1) + new_ch % ascii_z
            result.append(chr(new_ch))

        return ''.join(result)

# Solution 2
# Run time Complexity: O(n), Space Complexity: O(n)
def transform_2(string, key):
	result = []
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
	
	# Get the key in 0-25 range
	new_key = key % 26
	
	for ch in string:
		current_index = alphabets.index(ch)
		new_index = (current_index + key) % 26
		result.append(alphabets[new_index])
		
	return ''.join(result)


# Solution 3
# Run time Complexity: O(n), Space Complexity: O(n)
def transform_3(string, key):
    result = []
	new_key = key % 26
	
	for ch in string:
		current_index = ord(ch) - ord('a')
		new_index = (current_index + new_key) % 26
		new_ch = ord('a') + new_index
		result.append(chr(new_ch))
	
	return ''.join(result)
