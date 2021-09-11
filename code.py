#!/usr/bin/env python3

alphabet = dict(A='.-', B='-...', C='-.-.', D='-..', E='.', F='..-.', G='--.', H='....', I='..', J='.---', K='-.-', L='.-..', M='--', N='-.', O='---', P='.--.', Q='--.-', R='.-.', S='...', T='-', U='..-', V='...-', W='.--', X='-..-', Y='-.--', Z='--..', a='.-', b='-...', c='-.-.', d='-..', e='.', f='..-.', g='--.', h='....', i='..', j='.---', k='-.-', l='.-..', m='--', n='-.', o='---', p='.--.', q='--.-', r='.-.', s='...', t='-', u='..-', v='...-', w='.--', x='-..-', y='-.--', z='--..', _='\n')

def space_erasing(pt_input):
  z=0
  user_input = ""
  for z in range (len(pt_input)):#Traitement des espaces
    if(pt_input[z] == " "):
      user_input = user_input + "_"
    else:
      user_input = user_input + pt_input[z]
  return user_input

def ret_choice(letter):
  if(letter == '_'):
    return ""
  else:
    return " "

def transition_char(char):
  if (char == "."):
    return "."
  else:
    pass

def word2morse(word, alpha=None):
  if alpha is None:
   alpha = alphabet
  else:
   pass
  return "".join(alpha[c] + ret_choice(c) for c in word)

pt_input=input("Entrez une phrase ?\n> ")
user_input = space_erasing(pt_input)
print()
alpha = None
print(word2morse(user_input))