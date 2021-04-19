import nltk
import re
import sys
#how to compile: python3 dollar_program.py inputfile
input_file = sys.argv[1]

dollar_pattern = re.compile('|'.join([
	r'[\d]+ (cents?|dollars?)',
	r'[\$][0-9]+\.[0-9]{1,9}', #decimal [$0.05, $1.2]
	r'[\$][\d{1,3}]\,\d{1,3}', #$1,000, 10,000, 100,000, 
	r'[\$][\d{1,3}]\,\d{1,3},\d{1,3}',
	r'[\$][\d]+ (hundred|thousand|million|billion|trillion)',
	r'(one|two|three|four|five|six|seven|eight|nine|ten)\s(cents|dollars?)',
	r'(eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty)\s(cents|dollars?)',
	r'(twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)\s(one|two|three|four|five|six|seven|eight|nine)\s(cents|dollars?)',
	r'(twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)+(-)+(one|two|three|four|five|six|seven|eight|nine)\s(cents|dollars?)',
	r'(one|two|three|four|five|six|seven|eight|nine|ten)\s(hundred|thousand|million|billion|trillion)\s(cents|dollars?)',
	r'(one|two|three|four|five|six|seven|eight|nine|ten)+(-)+(hundred|thousand|million|billion|trillion)\s(cents|dollars?)',

	r'(twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)\s(one|two|three|four|five|six|seven|eight|nine)\s(hundred|thousand|million|billion|trillion)\s(cents|dollars?)',
	r'(twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)+(-)+(one|two|three|four|five|six|seven|eight|nine)+(-)+(hundred|thousand|million|billion|trillion)\s(cents|dollars?)',

	r'(one|two|three|four|five|six|seven|eight|nine|ten)\s(hundred|thousand|million|billion|trillion)\s(and)\s(twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)\s(one|two|three|four|five|six|seven|eight|nine|ten)\s(hundred|thousand|million|billion|trillion)\s(cents|dollars?)',
	r'(one|two|three|four|five|six|seven|eight|nine|ten)\s(hundred|thousand|million|billion|trillion)\s(and)\s(twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)\s(one|two|three|four|five|six|seven|eight|nine|ten)\s(hundred|thousand|million|billion|trillion)\s(cents|dollars?)',

	r'(one|two|three|four|five|six|seven|eight|nine|ten)\s(hundred|thousand|million|billion|trillion)\s(and)\s(one|two|three|four|five|six|seven|eight|nine|ten)\s(cents|dollars?)'
	r'(hundreds|thousands|millions|billions|trillions)\s(of dollars?)',
	]), re.IGNORECASE)

values = ""
cnt=0
output_file = open("dollar_output.txt", "w+")
for i, line in enumerate(open(input_file)):
	values = line
	#print(values)
	for match in re.finditer(dollar_pattern, line):
		print(match)
		#print(line)
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

