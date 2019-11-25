import sys

from collections import Counter

data = []
tokens = []
tags = []
tokens_tags={}
unique_tags=set()

#filename='C:\\Users\\kadss\\Downloads\\NLP6320_POSTaggedTrainingSet-Windows.txt'

filename=sys.argv[1]
with open(filename, 'r') as file:
    data = file.read()

for sentence in data.split('\n'):
    for word in sentence.strip().split():
        token,tag=word.split('_')
        tokens.append(token.lower())
        tags.append(tag)
        unique_tags.add(tag)
        if token.lower() in tokens_tags:
            tokens_tags[token.lower()].append(tag)
        else:
            tokens_tags[token.lower()]=[tag]
            
        
most_probable_tags={}


for key, value in tokens_tags.items():

    counter = Counter(value)
    maxValue = counter.most_common()[0]
    most_probable_tags[key] = maxValue[0]


modifiled_t=[]
for word in tokens:
		modifiled_t.append(most_probable_tags[word])
        
        
        
def get_Brills(tags, mostProbableTags, uniqueTags):
	brillsTemplate = {}
	modTags = mostProbableTags[:]



	index = 0
    

	old_threshold = 10000
    
	threshold = 0
    
    
	while old_threshold != threshold:
        
		old_threshold = threshold
		threshold = 0
		index += 1
   
	
	
		for fromTag in uniqueTags:
			for toTag in uniqueTags:

				rule_dict = {}
				if fromTag == toTag:
					continue

				for pos in range(1,len(modTags)):
					if tags[pos] == toTag and modTags[pos] == fromTag:

						rule = (modTags[pos-1], fromTag, toTag)
						if rule in rule_dict:
							rule_dict[rule] += 1
						else:
							rule_dict[rule] = 1

					elif tags[pos] == fromTag and modTags[pos] == fromTag:

						rule = (modTags[pos-1], fromTag, toTag)
						if rule in rule_dict:
							rule_dict[rule] -= 1
						else:
							rule_dict[rule] = -1

				if bool(rule_dict):  #not empty
					maxValueKey = max(rule_dict, key=rule_dict.get)
					maxValue = rule_dict.get(maxValueKey)

					if maxValue > threshold:
						threshold = maxValue
						tupel = maxValueKey

		for i in range(len(modTags)-1):
			if modTags[i] == tupel[0] and modTags[i+1] == tupel[1]:
				modTags[i+1] = tupel[2]

		brillsTemplate[tupel] = threshold
        


	return brillsTemplate.items()
    
    
rules=get_Brills(tags,modifiled_t,unique_tags)

print(rules)


print('standard most probable tag',most_probable_tags['standard'])

print('standard possible tags',set(tokens_tags['standard']))


print('work most probable tag',most_probable_tags['work'])

print('work possible tags',set(tokens_tags['work']))



