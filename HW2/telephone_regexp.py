import nltk
import re
import sys
#how to compile: python3 telephone_regexp.py inputfile
def main():
	input_file = sys.argv[1]

	phone_pattern_regex = re.compile('|'.join([
		r'(Tel.)\s+(\d{3}.\d{3}.\d{4})', #Tel 999/ 999 9999
		r'[\d]{3}-[\d]{3}-[\d]{4}',#999-999-9999
		r'[(][\d]{3}[)]\s?[\d]{3}\s[\d]{4}',#(999) 999 9999
		r'[(][\d]{3}[)]\s?[\d]{3}-[\d]{4}', #(999) 999-9999
		r'(call|dial)\s+(\d{3}.\d{3}.\d{4})', #Tel 999/ 999 9999
		r'(call|dial)\s+[2-9][1-1][1-1]', #call/dial 911 n11 code
		r'(\+1)\s+(\d{3}.\d{3}.\d{4})' #+1 999 999 9999
		]), re.IGNORECASE)

	values = ""
	cnt=0
	output_file = open("telephone_output.txt", "w+")
	for i, line in enumerate(open(input_file)):
		values = line
		#print(values)
		for match in re.finditer(phone_pattern_regex, line):
			print(match)
			cnt+=1
			output_file.write(match.group(0)+"\n")
			values = line.replace(match.group(0), "["+match.group(0)+"]")
	output_file.write(values)
	print ( str(cnt), " number of times written into:", output_file)


	#dollar, Dollars, $, hundred(s), thousand(s), etc
	#\d - digita(0-9)
	#\D - Not a Digita(0-9)
	#\w - word char
	#\W - Not a word char
	#\s - whitespace (space, tab, newline)
	#\S - Notw whitespace
	#\b - Word Boundary
	#\B - not a word boundary
	#^ beginning of a string
	#$ end of string

	#[] - matches characters in brackets
	#[^ ] - matches characters not in brackets
	#| - either or
	#( ) - group
	#dollar_regex_pattern = re.compile(r'[a-zA-Z]')

main()
