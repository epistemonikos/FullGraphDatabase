# -*- coding: utf-8 -*-
from Levenshtein import distance as levenshtein_distance
import re
from stop_words import get_stop_words
from fuzzywuzzy import fuzz

references = ['A randomized trial of beta-blockade in heart failure. The Cardiac Insufficiency Bisoprolol Study (CIBIS). CIBIS Investigators and Committees. Circulation. 1994;90:1765–1773.',
'CIBIS Investigators and Committees. A randomized trial of beta-blockade in heart failure. The Cardiac Insufficiency Bisoprolol Study (CIBIS). CIBIS Investigators and Committees. Circulation. 1994;90(4):1765-73.',
'CIBIS Investigators and Committees. A randomized trial of beta-blockade in heart failure: the Cardiac Insufficiency Bisoprolol Study (CIBIS). Circulation 1994;90:1765-73.',
'CIBIS Investigators A randomized trial of beta blockade in heart failure: the Cardiac Insufficiency Bisoprolol Study Circulation 1994 90 1765 1773',
'Packer M, Bristow MR, Cohn JN, Colucci WS, Fowler MB, Gilbert EM, Shusterman NH. The effect of carvedilol on morbidity and mortality in patients with chronic heart failure. U.S. Carvedilol Heart Failure Study Group. N Engl J Med. 1996;334:1349–1355. doi: 10.1056/NEJM199605233342101.',
'Olsen SL, Gilbert EM, Renlund DG, Taylor DO, Yanowitz FD, Bristow MR. Carvedilol improves left ventricular function and symptoms in chronic heart failure: a double-blind randomized study. J Am Coll Cardiol. 1995;25:1225–1231. doi: 10.1016/0735-1097(95)00012-S.',
'Metra M, Nardi M, Giubbini R, Dei Cas L. Effects of short- and long-term carvedilol administration on rest and exercise hemodynamic variables, exercise capacity and clinical conditions in patients with idiopathic dilated cardiomyopathy. J Am Coll Cardiol. 1994;24:1678–1687. doi: 10.1016/0735-1097(94)90174-0. ',
'Effect of metoprolol CR/XL in chronic heart failure: Metoprolol CR/XL Randomised Intervention Trial in Congestive Heart Failure (MERIT-HF) Lancet. 1999;353:2001–2007.']

NUMERO_MAGICO = 75

def without_stop_words(raw):
    if not raw:
        return ''
    stop_words = get_stop_words('en')
    return ''.join([c for c in raw if c not in stop_words])

def get_rating(i1, i2):
  cita1 = without_stop_words(references[i1].replace('.',' ').replace(',',' ').replace(';',' ').lower()).split()
  cita2 = without_stop_words(references[i2].replace('.',' ').replace(',',' ').replace(';',' ').lower()).split()

  cita1 = [x for x in cita1 if len(x) > 2]
  cita2 = [x for x in cita2 if len(x) > 2]

  min_cita = cita1
  if len(cita1) > len(cita2):
    min_cita = cita2
  
  max_cita = cita1
  if len(cita1) < len(cita2):
    max_cita = cita2

  len_max_cita = len(max_cita)
  len_min_cita = len(min_cita)

  count = 0
  for x in min_cita:
    if x in max_cita:
      count += 1
      max_cita.remove(x)

  rating_1 = count/len_max_cita*100
  rating_2 = fuzz.token_set_ratio(references[i1],references[i2])
  rating_3 = (rating_1 + rating_2)/2
  print( "%s\t%s\t%s\t%s\t%s\n" % (i1, i2, rating_1, rating_2, rating_3) )
  print( "%s\t%s\t%s\t%s\t%s\n" % (i1, i2, rating_1 > NUMERO_MAGICO, rating_2 > NUMERO_MAGICO, rating_3 > NUMERO_MAGICO) )

funcs = [get_rating]

for func in range(len(funcs)):
  for index_x in range(len(references)):
    for index_y in range(len(references)):
      if index_x < index_y:
        funcs[func](index_x, index_y)