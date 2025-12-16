import sys

def main():
	from stats import count_words, count_characters, reporting
	if len(sys.argv)<2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		path=sys.argv[1] 
	text = get_book_text(path)
	num_words=count_words(text)
	dico = count_characters(text)
	listed = reporting(dico)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for l in listed:
		if l["char"].isalpha()==False :
			continue
		else :
			print(f"{l["char"]}: {l["num"]}")
	print("============= END ===============")	
def get_book_text(path):
	with open(path) as f:
		return f.read()






main()
