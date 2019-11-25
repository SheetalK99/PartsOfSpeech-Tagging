
#Author:Sheetal Kadam
#Date: 09/22/2019
#Naive Bayesian Probabilities (40 points):

import sys
from nltk import FreqDist
from nltk.util import ngrams

filename=sys.argv[1]

prob_tag_word={}
prob_tag_tag={}

with open(filename, 'r') as file:
    data = file.read()
	
    

word_count = dict()
tag_count= dict()
for i in data.split():
    
    word=i.split('_')[0].lower()
    
    tag=i.split('_')[1]
    word_count[word] = word_count.get(word, 0) + 1    
    tag_count[tag] = tag_count.get(tag, 0) + 1
    
    


tokens_tags={}
tag_word={}
tag_tag = FreqDist()

sentences=data.split('\n')


for sentence in sentences:
    tags=[]
    words=sentence.split() 
    for word in words:
        
        word1,tag=word.split('_')
        
        
        word1=word1.lower()
        
        
        if word1.lower() in tokens_tags:
            tokens_tags[word1].append(tag)
        else:
            tokens_tags[word1]=[tag]
            
        tags.append(tag)
        if (tag,word1) in tag_word:
            tag_word[(tag,word1)]=tag_word[(tag,word1)]+1
        else:
            tag_word[(tag,word1)]=1
            
            
    bigrams = ngrams(tags, 2)
    tag_tag.update(bigrams)
        
     




for key,value in tag_word.items():
    
    prob_tag_word[key]=tag_word[key]/tag_count[key[0]]
    
    
for (t1,t2) in tag_tag.keys():
    
    prob_tag_tag[(t1,t2)]=tag_tag[(t1,t2)]/tag_count[key[0]]
    
    
    
print('Possible tags for standard',set(tokens_tags['standard']))

    
print('Possible tags for work',set(tokens_tags['work']))

print(prob_tag_word)


print(prob_tag_tag)




