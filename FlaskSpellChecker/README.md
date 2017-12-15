## Prerequisite
* nltk
* flask
* request

## Dependencies
* lang_sinhala.py
* sentences.txt

## Execute
`python sinhala_grammar_checker.py`

## Output
* `parsedsents.txt` file will create after executing the sinhala_grammar_checker.py


(S[]
    (NP[CASE='F3', NUM='sg']
        (PropN[CASE='F3', GEN='MA', NUM='sg'] )
    )
    (VP[GEN='MA', NUM='sg', PER='T', TENSE='Npast']
        (NP[CASE='F1', DEF=?TF, GEN='NE', NUM='sg']
          (N[CASE='F1', DEF='TRue', GEN='NE', NUM='sg'] ඉර)
         )
        (NP[CASE='F3', NUM='sg']
           (PropN[CASE='F3', GEN='MA', NUM='sg'] )
         )
        (IV[GEN='MA', NUM='sg', PER='T', TENSE='Npast', +VLT] පායයි)
    )
 )