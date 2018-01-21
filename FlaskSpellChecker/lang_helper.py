sinhala = """

% start S
# ###################
# Grammar Productions
# By Tharusha Shehan Edirisooriya(Bsc)
# ###################

# S expansion productions
S -> NP[NUM=?n, GEN=?G, PER=?P, DEF=?TF] VP[NUM=?n, GEN=?G, PER=?P, CASE=?CS] 

# NP expansion productions 
NP[NUM=?n, CASE=?CS, GEN=?G, DEF=?TF] 	-> N[NUM=?n, CASE=?CS, GEN=?G] 
NP[NUM=?n, CASE=?CS, GEN=?G, PER=?P] 	-> PrN[NUM=?n, CASE=?CS, GEN=?G, PER=?P] 
NP[NUM=?n, CASE=?CS] 					-> PropN[NUM=?n, CASE=?CS] 
NP[NUM=?n, CASE=?CS, GEN=?G, DEF=?TF]  	-> Det N[NUM=?n, CASE=?CS, GEN=?G] 
NP[NUM=?n, CASE=?CS, GEN=?G, DEF=?TF]  	-> ADJP N[NUM=?n, CASE=?CS, GEN=?G] 
NP[NUM=?n, CASE=?CS, GEN=?G, DEF=?TF]  	-> Det ADJP N[NUM=?n, CASE=?CS, GEN=?G] 


# VP expansion productions
VP[TENSE=?t, NUM=?n, GEN=?G, PER=?P] -> IV[TENSE=?t, NUM=?n, GEN=?G, PER=?P]
VP[TENSE=?t, NUM=?n, GEN=?G, PER=?P] -> TV[TENSE=?t, NUM=?n, GEN=?G, PER=?P]
VP[TENSE=?t, NUM=?n, GEN=?G, PER=?P] -> NP TV[TENSE=?t, NUM=?n, GEN=?G, PER=?P]
VP[TENSE=?t, NUM=?n, GEN=?G, PER=?P] -> NP IV[TENSE=?t, NUM=?n, GEN=?G, PER=?P]
VP[TENSE=?t, NUM=?n, GEN=?G, PER=?P] -> NP  NP TV[TENSE=?t, NUM=?n, GEN=?G, PER=?P]
VP[TENSE=?t, NUM=?n, GEN=?G, PER=?P] -> NP  NP IV[TENSE=?t, NUM=?n, GEN=?G, PER=?P]
VP[TENSE=?t, NUM=?n, GEN=?G, PER=?P] -> NP NP ADVP TV[TENSE=?t, NUM=?n, GEN=?G, PER=?P]
VP[TENSE=?t, NUM=?n, GEN=?G, PER=?P] -> ADVP IV[TENSE=?t, NUM=?n, GEN=?G, PER=?P]
VP[TENSE=?t, NUM=?n, GEN=?G, PER=?P] -> ADVP TV[TENSE=?t, NUM=?n, GEN=?G, PER=?P]
VP[TENSE=?t, NUM=?n, GEN=?G, PER=?P] -> NP ADVP IV[TENSE=?t, NUM=?n, GEN=?G, PER=?P]
VP[TENSE=?t, NUM=?n, GEN=?G, PER=?P] -> NP  ADVP TV[TENSE=?t, NUM=?n, GEN=?G, PER=?P]


# ADJP expansion productions 
ADJP -> Adj 
ADJP -> Adj ADJP 
#ADJP -> Adj Adj Adj 
#ADJP -> Adj Adj Adj Adj 


# ADVP expansion productions
ADVP -> Adv[ADV=?A]
ADVP -> Adv[ADV=?A]Adv[ADV=?A]
ADVP -> Adv[ADV=?A]Adv[ADV=?A]Adv[ADV=?A]
ADVP -> Adv[ADV=?A]Adv[ADV=?B]
ADVP -> Adv[ADV=?A]Adv[ADV=?B]Adv[ADV=?C]
ADVP -> Adv[ADV=?A]Adv[ADV=?B]Adv[ADV=?A]
ADVP -> Adv[ADV=?A]Adv[ADV=?A]Adv[ADV=?B]
ADVP -> Adv[ADV=?A]Adv[ADV=?B]Adv[ADV=?B]
ADVP -> Adv[ADV=?A]Adv[ADV=?A]Adv[ADV=?B]Adv[ADV=?C]


# ###################
# Lexical Productions
# ###################

N[NUM=sg, GEN=MA, CASE=F1, DEF=TRue]   ->  'යෝධයා' | 'රජතුමා' | 'ලේනා' | 'වඩුවා' | 'වඳුරා' | 'වැඩකාරයා' | 'වැද්දා' | 'වෙළෙන්දා' | 'සමනළයා' | 'කපටියා' | 'පුතු' | 'බබා' | 'බළලා' | 'මැස්සා' | 'මිනිසා' | 'මුගටියා' | 'මොණරා' | 'බල්ලා' | 'අයියා' | 'අශ්වයා' | 'ඇතා' | 'ඉදිබුවා' | 'උපාසකයා' | 'ඌරා' | 'කුකුළා' | 'කුරුල්ලා' | 'කොල්ලා' | 'ගුරුතුමා' | 'ගොනා' | 'ගොවියා' | 'තවුසා' | 'තාත්තා' | 'දාසයා' | 'නයා' |  'පරෙවියා' | 'පියා' |  'සීයා' | 'සූර්යයා' | 'හංසයා' | 'හාවා' | 'හිඟන්නා' | 'ළදරුවා' | 'ළමයා' | 
N[NUM=sg, GEN=MA, CASE=F1, DEF=False]   -> 'බල්ලෙක්' | 'තවුසෙක්' | 'පුතෙක්' | 'වඳුරෙක්' | 'හිඟන්නෙක්' | 'හිවලෙක්' 
N[NUM=sg, GEN=MA, CASE=F2, DEF=TRue]   -> 'බල්ලා' | 'බුදුන්' 
N[NUM=sg, GEN=MA, CASE=F2, DEF=False]   -> 'බල්ලලෙකු' | 'නයකු' | 'මීයකු' | 'මුවකු' 
N[NUM=sg, GEN=MA, CASE=F3, DEF=TRue]   -> 'බල්ලාට' | 'කුකුළාට' | 'පුතුට' | 'හිඟන්නාට' | 'ළමයාට' 
N[NUM=sg, GEN=MA, CASE=F3, DEF=False]   -> 'බල්ලෙකුට' 
N[NUM=sg, GEN=MA, CASE=F4, DEF=TRue]   -> 'බල්ලාගේ' 
N[NUM=sg, GEN=MA, CASE=F4, DEF=False]   -> 'බල්ලෙකුගේ' 
N[NUM=sg, GEN=MA, CASE=F5, DEF=TRue]   -> 'බල්ලාගෙන්' 
N[NUM=sg, GEN=MA, CASE=F5, DEF=False]   -> 'බල්ලෙකුගෙන්' 
N[NUM=sg, GEN=FE, CASE=F1, DEF=TRue]   -> 'ගැහැණිය' | 'අම්මා' | 'උපාසිකාව' | 'කිරිල්ල' | 'නංගී' | 'මව' 
N[NUM=sg, GEN=FE, CASE=F1, DEF=False]   -> 'ගැහැණියක්' | 'බැළලියක්' 
N[NUM=sg, GEN=FE, CASE=F2, DEF=TRue]   -> 'ගැහැණිය' 
N[NUM=sg, GEN=FE, CASE=F2, DEF=False]   -> 'ගැහැණියක' 
N[NUM=sg, GEN=FE, CASE=F3, DEF=TRue]   -> 'ගැහැණියට' | 'ස්ත්‍රියට' 
N[NUM=sg, GEN=FE, CASE=F3, DEF=False]   -> 'ගැහැණියකට' 
N[NUM=sg, GEN=FE, CASE=F4, DEF=TRue]   -> 'ගැහැණියගේ' 
N[NUM=sg, GEN=FE, CASE=F4, DEF=False]   -> 'ගැහැණියකගේ' 
N[NUM=sg, GEN=FE, CASE=F5, DEF=TRue]   -> 'ගැහැණියගෙන්' 
N[NUM=sg, GEN=FE, CASE=F5, DEF=False]   -> 'ගැහැණියකගෙන්' 
N[NUM=sg, GEN=NE, CASE=F1, DEF=TRue]   -> 'ගස' | 'අහස' | 'ඉර' | 'ඔරුව' | 'කෙක්ක' | 'කොඩිය' | 'ගඟ' | 'ගීතය' | 'ගෙය' | 'දුම්රිය' | 'නගුල' | 'පහන' | 'පෙරහැර' | 'පොත' | 'බිම' | 'මල' | 'මුල' | 'ලියුම' | 'විල' | 'සඳ' 
N[NUM=sg, GEN=NE, CASE=F1, DEF=False]   -> 'ගසක්' | 'අම්බලමක්' | 'ගීයක්' | 'ගෙඩියක්' | 'ගෙයක්' | 'පටියක්' | 'පොතක්' | 'බොරුවක්' | 'ලියුමක්' | 'විලක්' | 'විහිළුවක්' | 'ස්වප්නයක්' | 'කඩුවක්' | 'කරමලක්' 
N[NUM=sg, GEN=NE, CASE=F3, DEF=TRue]   -> 'ගසට' | 'කුඹුරට' | 'ගඟට' | 'ගමට' | 'තුඹසට' | 'නගරයට' | 'නුවරට' | 'පන්සලට' | 'පාසලට' | 'බිමට' | 'වනයට' | 'සඳට' 
N[NUM=sg, GEN=NE, CASE=F3, DEF=False]   -> 'ගසකට' 
N[NUM=sg, GEN=NE, CASE=F4, DEF=TRue]   -> 'ගසේ' | 'ගසෙහි' | 'අම්බලමේ' | 'ආකාශයෙහි' | 'කරෙහි' | 'කුඹුරෙහි' | 'කූඩුවෙහි' | 'ගඟෙහි' | 'ගමෙහි' | 'ගෘහයෙහි' | 'දඩයමේ' | 'මිදුලෙහි' | 'විලෙහි' | 'හිසෙහි' | 'සිහසුනෙහි' 
N[NUM=sg, GEN=NE, CASE=F4, DEF=False]   -> 'ගසක' 
N[NUM=sg, GEN=NE, CASE=F5, DEF=TRue]   -> 'ගසින්' | 'ඇඳෙන්' | 'සුළඟට' 
N[NUM=sg, GEN=NE, CASE=F5, DEF=False]   -> 'ගසකින්' 
N[NUM=pl, GEN=MA, CASE=F1]   -> 'බල්ලෝ' | 'ඇත්තු' | 'උකුණෝ' | 'ගම්වැස්සෝ' | 'ගොවීහු' | 'තරුණයෝ' | 'තවුසෝ' | 'දරුවෝ' | 'පක්ෂීහු' | 'බළල්ලු' | 'මකුළුවෝ' | 'මිනිස්සු' | 'මීයෝ' | 'ලේන්නු' | 'වඳුරෝ' | 'වැද්දෝ' | 'සතුරෝ' | 'සොරු' | 'හරක්' | 'ළමයි' 
N[NUM=pl, GEN=MA, CASE=F2]   -> 'බල්ලන්' | 'ගවයන්' | 'ගොනුන්' | 'තවුසන්' | 'දරුවන්' | 'මාළුවන්' | 'මීයන්' | 'වඳුරන්' | 'සතුන්' | 'සොරුන්' 
N[NUM=pl, GEN=MA, CASE=F3]   -> 'බල්ලන්ට' | 'කුරුල්ලන්' | 'පැටවුන්ට' 
N[NUM=pl, GEN=MA, CASE=F4]   -> 'බල්ලන්ගේ' 
N[NUM=pl, GEN=MA, CASE=F5]   -> 'බල්ලන්ගෙන්' 
N[NUM=pl, GEN=FE, CASE=F1]   -> 'ගැහැණු' | 'ගෑණු' 
N[NUM=pl, GEN=FE, CASE=F2]   -> 'ගැහැණුන්' 
N[NUM=pl, GEN=FE, CASE=F3]   -> 'ගැහැණුන්ට' 
N[NUM=pl, GEN=FE, CASE=F4]   -> 'ගැහැණුන්ගේ' 
N[NUM=pl, GEN=FE, CASE=F5]   -> 'ගැහැණුන්ගෙන්' 
N[NUM=pl, GEN=NE, CASE=F1]   -> 'සහල්' | 'සිල්' | 'නිවාඩු' | 'ගස්' | 'අකුරු' | 'අඹ' | 'ඔන්චිලි' | 'ඔරු' | 'කජු' | 'කවි' | 'ආහාර' | 'කුඹුරු' | 'ගමන්' | 'ගී' | 'ගෙඩි' | 'ගොයම්' | 'තණ' | 'දඩයම්' | 'දැල්' | 'නැටුම්' |  'පව්' | 'පැණි' | 'පැන්' | 'පොත්' | 'පොල්' | 'බත්' | 'බොරු' | 'මල්' | 'රෙදි' | 'රොන්' | 'වැසි' | 
N[NUM=pl, GEN=NE, CASE=F3]   -> 'ගස්වලට' 
N[NUM=pl, GEN=NE, CASE=F4]   -> 'ගස්වල' | 'කැලෑවල' 
N[NUM=pl, GEN=NE, CASE=F5]   -> 'ගස්වලින්' | 'කෙකිවලින්' 
PropN[NUM=sg, GEN=MA, CASE=F1] -> 'අබරන්' | 'ජයසේන' 
PropN[NUM=sg, GEN=MA, CASE=F3] -> 'ජයසේනට' | 
PropN[NUM=sg, GEN=FE, CASE=F1] -> 'නන්දා' | 
PrN[NUM=sg, GEN=MA, CASE=F1, PER=T] -> 'ඔහු' | 'එයා' | 'හෙතෙම' | 'හෙතෙමේ' 
PrN[NUM=sg, GEN=MA, CASE=F2, PER=T] -> 'ඔහුව' | 'එයාව' 
PrN[NUM=sg, GEN=MA, CASE=F3, PER=T] -> 'ඔහුට' | 'එයාට'  
PrN[NUM=sg, GEN=MA, CASE=F4, PER=T] -> 'ඔහුගේ' | 'එයාගේ' 
PrN[NUM=sg, GEN=MA, CASE=F5, PER=T] -> 'ඔහුගෙන්' | 'එයාගෙන්' 
PrN[NUM=sg, GEN=FE, CASE=F1, PER=T] -> 'ඇය' | 'ඈ' 
PrN[NUM=sg, GEN=FE, CASE=F2, PER=T] -> 'ඇයව' | 'ඈව' 
PrN[NUM=sg, GEN=FE, CASE=F3, PER=T] -> 'ඇයට' | 'ඈට' 
PrN[NUM=sg, GEN=FE, CASE=F4, PER=T] -> 'ඇයගේ' | 'ඇගේ'  
PrN[NUM=sg, GEN=FE, CASE=F5, PER=T] -> 'ඇයගෙන්' | 'ඇගෙන්' 
PrN[NUM=pl, CASE=F1, PER=T] -> 'ඔවුහු' | 'ඒගොල්ලො' 
PrN[NUM=pl, CASE=F2, PER=T] -> 'ඔවුන්' | 'ඒගොල්ලන්' 
PrN[NUM=pl, CASE=F3, PER=T] -> 'ඔවුන්ට' | 'ඒගොල්ලන්ට' 
PrN[NUM=pl, CASE=F4, PER=T] -> 'ඔවුන්ගේ' | 'ඒගොල්ලන්ගේ' 
PrN[NUM=pl, CASE=F5, PER=T] -> 'ඔවුන්ගෙන්' | 'ඒගොල්ලන්ගෙන්' 
PrN[NUM=sg, CASE=F1, PER=S] -> 'ඔබ' | 'ඔයා' | 'නුඹ' | 'තෝ' 
PrN[NUM=sg, CASE=F2, PER=S] -> 'ඔබව' | 'ඔයාව' | 'නුඹව' 
PrN[NUM=sg, CASE=F3, PER=S] -> 'ඔබ‍ට' | 'ඔයාට' | 'නුඹට' 
PrN[NUM=sg, CASE=F4, PER=S] -> 'ඔබගේ' | 'ඔයාගේ' | 'නුඹගේ' 
PrN[NUM=sg, CASE=F5, PER=S] -> 'ඔබගෙන්' | 'ඔයාගෙන්' | 'නුඹගෙන්' 
PrN[NUM=pl, CASE=F1, PER=S] -> 'ඔබලා' | 'තොපි' | 'නුඹලා' | 'තෙපි' 
PrN[NUM=pl, CASE=F2, PER=S] -> 'ඔබලා' | 'තොප' | 'නුඹලා' 
PrN[NUM=pl, CASE=F3, PER=S] -> 'ඔබලාට' | 'තොපට' | 'නුඹලාට' 
PrN[NUM=pl, CASE=F4, PER=S] -> 'ඔබලාගේ' | 'තොපගේ' | 'නුඹලාගේ' 
PrN[NUM=pl, CASE=F5, PER=S] -> 'ඔබලාගෙන්' | 'තොපගෙන්' | 'නුඹලාගෙන්' 
PrN[NUM=sg, CASE=F1, PER=F] -> 'මම' 
PrN[NUM=sg, CASE=F2, PER=F] -> 'මා' 
PrN[NUM=sg, CASE=F3, PER=F] -> 'මට' 
PrN[NUM=sg, CASE=F4, PER=F] -> 'මගේ' | 'මාගේ' 
PrN[NUM=sg, CASE=F5, PER=F] -> 'මගෙන්' | 'මාගෙන්' 
PrN[NUM=pl, CASE=F1, PER=F] -> 'අපි' 
PrN[NUM=pl, CASE=F2, PER=F] -> 'අප' 
PrN[NUM=pl, CASE=F3, PER=F] -> 'අපට' 
PrN[NUM=pl, CASE=F4, PER=F] -> 'අපගේ' | 'අපේ' 
PrN[NUM=pl, CASE=F5, PER=F] -> 'අපගෙන්' | 'අපෙන්' 
Det -> 'ඒ' | 'මේ' | 'අර' | 'ඔය' | 'සමහර' | 'ඇතැම්' 
Adj -> 'අද' | 'අලංකාර' | 'ඉදුණු' | 'උණු' | 'උයන' | 'එවූ' | 'කියන' | 'ධනවත්' | 'නරක' | 'නැගුණු' | 'මිහිරි' | 'මෝඩ' | 'ලගින' | 'වල්' | 'සිටින' | 'හොඳ' | 'මහළු' | 'ලොකු' | 'කුඩා' | 'බොර' | 'පාළු'

IV[TENSE=Npast,  NUM=sg, GEN=MA, VLT=True, PER=T] -> 'යයි' | 'ඉගිළෙයි' | 'එයි' | 'කැඳවයි' | 'කියයි' | 'ගලයි' | 'ගොරවයි' | 'දුවයි' | 'නගියි' | 'නඟී' | 'නිදයි' | 'පායයි' | 'පාවෙයි' | 'පිපෙයි' | 'පීනයි' | 'බුරයි' | 'ලගියි' | 'සිටියි' | 'සිටී' | 'හඬයි' | 'හිඳියි' | 'බබළයි' | 'සෙලවේ' | 'බුරන්නේය' 
IV[TENSE=Npast,  NUM=sg, GEN=FE, VLT=True, PER=T] -> 'යන්නීය' 
IV[TENSE=Npast,  NUM=sg, GEN=MA, VLT=False, PER=T] -> 'බිරෙයි' 
IV[TENSE=Npast,  NUM=sg, GEN=NE, VLT=False, PER=T] -> 'බැබලෙයි' | 'පිපෙයි' 
IV[TENSE=Npast,  NUM=pl, VLT=True, PER=T] -> 'යති' | 'එති' | 'දුවති' | 'සිටිති' 
IV[TENSE=Npast,  NUM=sg, VLT=True, PER=S] -> 'යහි' 
IV[TENSE=Npast,  NUM=pl, VLT=True, PER=S] -> 'යහු' 
IV[TENSE=Npast,  NUM=sg, VLT=True, PER=F] -> 'යමි' 
IV[TENSE=Npast,  NUM=pl, VLT=True, PER=F] -> 'යමු' | 'ඉඳිමු' 

IV[TENSE=past,  NUM=sg, GEN=MA, VLT=True, PER=T] -> 'ඇවිද්දේය' | 'ඉගිළුණේය' | 'ගියේය' | 'පැමිණියේය' 
IV[TENSE=past,  NUM=sg, GEN=FE, VLT=True, PER=T] -> 'ඇවිද්දාය' | 'ඉගිළුණාය' | 'ගියාය' 
IV[TENSE=past,  NUM=sg, VLT=False, PER=T] -> 'වැටිණි' 
IV[TENSE=past,  NUM=pl, VLT=True, PER=T] -> 'ආවෝය' | 'ගියහ' | 'ගියෝය' 
IV[TENSE=past,  NUM=sg, VLT=True, PER=S] -> 'ඇවිද්දෙහි' | 'ගියෙහි' 
IV[TENSE=past,  NUM=pl, VLT=True, PER=S] -> 'ඇවිද්දෙහු' | 'ගියහු' 
IV[TENSE=past,  NUM=sg, VLT=True, PER=F] -> 'ගියෙමි' 
IV[TENSE=past,  NUM=pl, VLT=True, PER=F] -> 'ගියෙමු' 

TV[TENSE=Npast,  NUM=sg, GEN=MA, VLT=True, PER=T] -> 'දෙයි' | 'කයි' | 'අල්ලයි' | 'අහුලයි' | 'උයයි' | 'කඩයි' | 'කපයි' | 'කරයි' | 'කියවයි' | 'ගනියි' | 'ගයයි' | 'ගෙනෙයි' | 'දකියි' | 'නටයි' | 'නළවයි' | 'නෙළයි' | 'මරයි' | 'රකියි' | 'රවටයි' | 'වැටෙයි' | 'හාරයි' | 'කපන්නේය' | 'කරන්නේය' | 'තිබේ' | 'නාවන්නේය' | 'බොයි' | 'ලැබේ' | 'වපුරන්නේය' | 'ඇත' 
TV[TENSE=Npast,  NUM=sg, GEN=FE, VLT=True, PER=T] -> 'දෙන්නීය' 
TV[TENSE=Npast,  NUM=sg, VLT=False] -> 'ඇසෙයි' 
TV[TENSE=Npast,  NUM=pl, VLT=False] -> 'කෙරෙති' 
TV[TENSE=Npast,  NUM=pl, VLT=True, PER=T] -> 'කති' | 'උගනිති' | 'එලවති' | 'කඩති' | 'කපති' | 'කරති' | 'නාවති' | 'නෙළති' | 'පදිති' | 'පොළති' | 'බඳිති' | 'බොති' | 'මරති' | 'රකිති' | 'සෝදති' | 'කියති' | 'කියන්නෝය' | 'බසිති' 
TV[TENSE=Npast,  NUM=sg, VLT=True, PER=S] -> 'දෙන්නෙහි' | 'බලහි' 
TV[TENSE=Npast,  NUM=pl, VLT=True, PER=S] -> 'දෙන්නෙහු' 
TV[TENSE=Npast,  NUM=sg, VLT=True, PER=F] -> 'කමි' 
TV[TENSE=Npast,  NUM=pl, VLT=True, PER=F] -> 'අසමු' | 'කඩමු' | 'කමු' | 'දෙමු' | 'යවමු' 

TV[TENSE=past,  NUM=sg, GEN=MA, VLT=True, PER=T] -> 'කෑවේය' | 'කීය' | 'ගත්තේය' | 'දුටුවේය' | 'නැගුණේය' | 'මැරුවේය' | 'ලැබුණේය' | 'වික්කේය' | 'සෑදුවේය' | 'කළේය' | 'කැඩුවේය' | 'වැදුණේය' 
TV[TENSE=past,  NUM=sg, GEN=FE, VLT=True, PER=T] -> 'කෑවාය' | 'කීවාය' | 'දුටුවාය' | 'වැන්දාය' 
TV[TENSE=past,  NUM=sg, GEN=MA, VLT=False, PER=T] -> 'කැවුණි' 
TV[TENSE=past,  NUM=pl, VLT=True, PER=T] -> 'කෑවෝය' | 'කළහ' | 'කියෙව්වෝය' | 'නැංගෝය' | 'මැරුවෝය' | 'රැස්වූහ' | 'කැඩුවෝය' | 'පාළු කළහ' | 'වැදුණාහ' 
TV[TENSE=past,  NUM=sg, VLT=True, PER=S] -> 'කෑවෙහිය' 
TV[TENSE=past,  NUM=pl, VLT=True, PER=S] -> 'කෑවෙහුය' 
TV[TENSE=past,  NUM=sg, VLT=True, PER=F] -> 'කෑවෙමි' | 'දුටුවෙමි' | 'සෑදුවෙමි' 
TV[TENSE=past,  NUM=pl, VLT=True, PER=F] -> 'කෑවෙමු' | 'ගතුමු' 

Adv -> 'ඊයේ' | 'ඉක්මනින්' | 'තදින්' | 'පහසුවෙන්' | 'වේගයෙන්' | 'සෙමෙන්' | 'සුවසේ' | 'හෙට' | 'සතුටින්' | 'එතැනට' | 'එහි' | 'මෙහි' 

"""
