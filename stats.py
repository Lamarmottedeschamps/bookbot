def count_words(text):
	words = text.split()
	return len(words)

def count_characters(text):
	low_text=text.lower()
	chara_counter ={}
	for l in low_text :
		if l in chara_counter :
			chara_counter[l]+=1
		else :
			chara_counter[l]=1
	return chara_counter

def sort_on(d):
	return d["num"]

def reporting(dico):
	sorted=[]
	for d in dico:
		sorted.append({"char":d, "num":dico[d]})
	sorted.sort(reverse=True, key=sort_on)
	return sorted
