

#?G=gender
#?CS=case
#?P=person
#?A=adverb
#?B=adverb
#?C=adverb
#N=noun
#PrN=pronoun
#PropN=proper noun
#Det=determiner 
#ADJP=adjectival phrase
#ADVP=adverbial phrase
#adj=adjective
#adv=adverb
#VLT=Volition 
#VOL=volitive
#INVOL=involitive

# ######################
#      CASE

#NOM - Nominative
#ACC - Acusative
#DET - Dative
#GEN - Genitive
#ABL - Ablative

##################
#NUM = number

#SG - singular
#PL - plural 

##################
#GND = gender

#MA - masculin 
#FE - feminin 
#NE - neuter 

################## 
#PER = person 

#1 - first
#2 - second 
#3 - third 

##################
#ADVP = Adverbial phrase 

#place 
#time 
#manner 

##################
#VLT = volition 

#true 
#falls 

################## 

from lang_helper import sinhala
from nltk import grammar, parse

# Read the Sinhala Grammar
singram = grammar.FeatureGrammar.fromstring(sinhala)
parser = parse.FeatureEarleyChartParser(singram)

f_read = open('sentences.txt', encoding='utf-8')
f_write = open('parsedsents.txt', encoding='utf-8', mode='w')

for line in f_read:
    tokens = line.split()

    trees = parser.parse(tokens)

    for tree in trees:
        f_write.write(str(tree)+'\n')
        print(str(tree)+'\n')

''' Sample Output
(S[]
  (NP[CASE='F1', DEF=?TF, GEN='NE', NUM='pl']
    (N[CASE='F1', GEN='NE', NUM='pl'] ))
  (VP[GEN=?G, NUM='pl', PER='T', TENSE='past']
    (NP[CASE='F1', DEF=?TF, GEN='MA', NUM='pl']
      (N[CASE='F1', GEN='MA', NUM='pl'] ළමයි))
    (NP[CASE='F1', DEF=?TF, GEN='NE', NUM='pl']
      (N[CASE='F1', GEN='NE', NUM='pl'] පොත්))
    (TV[NUM='pl', PER='T', TENSE='past', +VLT] කියෙව්වෝය)))
'''

# WEB APP starts here
import flask


