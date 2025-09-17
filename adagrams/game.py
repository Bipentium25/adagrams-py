import random
from random import randint

def establish_pool():
    pool = []
    letter_counts= {
        'A': 9, 
        'B': 2, 
        'C': 2, 
        'D': 4, 
        'E': 12, 
        'F': 2, 
        'G': 3, 
        'H': 2, 
        'I': 9, 
        'J': 1, 
        'K': 1, 
        'L': 4, 
        'M': 2, 
        'N': 6, 
        'O': 8, 
        'P': 2, 
        'Q': 1, 
        'R': 6, 
        'S': 4, 
        'T': 6, 
        'U': 4, 
        'V': 2, 
        'W': 2, 
        'X': 1, 
        'Y': 2, 
        'Z': 1
    }
  
    for key, value in letter_counts.items():
        for i in range(value):
            pool.append(key)
    return pool

def draw_letters():
    pool = establish_pool()
    pool_size = len(pool)
    hand_cards = []
    # pull the cards 10 times, decreasing pool size by one by pop the card out of the pool. 
    for i in range(10):
        rand_index = random.randint(0,pool_size-1)
        hand_cards.append(pool[rand_index])
        pool.pop(rand_index)
        pool_size -= 1 # or len(pool)
    pool += hand_cards
    return hand_cards

def uses_available_letters(word, letter_bank):
    word = word.upper()
    letter_dict = {}
    for letter in letter_bank:
        # default letter_dict[letter] = 0, using the .get() method 
        # and add one each time encounter the letter, the first encouter also adds 1 
        #it's probably also workable to build a hashtable of every letter possible and count every letter into the dictionary 
        letter_dict[letter] = letter_dict.get(letter, 0) + 1
    for letter in word: 
        if letter not in letter_dict or letter_dict[letter] < 1:
            return False
        else:
            letter_dict[letter] -= 1
    return True


"""
    # I tried this at first I suppose I could use a so called shallow copy of the original list as a "bank"? but it is probably better
    # to build a dictionary for speed purpose. 
    letterbank_copy = letter_bank[:]
    if len(word) > 10:
        return False
    for letter in word:
        if letter not in letterbank_copy:
            return False
        else:
            letterbank_copy.remove(letter) # it is said that remove() will only remove the first letter encounter.

    return True
"""


def score_word(word):
    word = word.upper()
    word_point = 0
    if len(word) > 6:
        word_point += 8
    letter_score = {
    ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'): 1,
    ('D', 'G'): 2,
    ('B', 'C', 'M', 'P'): 3,
    ('F', 'H', 'V', 'W', 'Y'): 4,
    ('K',): 5,
    ('J', 'X'): 8,
    ('Q', 'Z'): 10    
    }
    for letter in word:
        for key , value in letter_score.items(): 
            if letter in key:
                word_point += value
    return word_point
    
def get_highest_word_score(word_list):
    winner_max = [word_list[0], score_word(word_list[0])]
    for word in word_list:
        current_score = score_word(word)
        if len(word) !=10 and len(winner_max[0]) != 10:
            if current_score > winner_max[1] :
                winner_max = [word, current_score]
            elif current_score == winner_max[1] and len(word) < len(winner_max[0]):
                winner_max = [word, current_score]
        elif len(word) == 10 and len(winner_max[0]) != 10:
            winner_max = [word, current_score]
            
        elif len(word) == 10 and len(winner_max[0]) == 10:
            if current_score > winner_max[1]:
                winner_max = [word, current_score]


    return winner_max[0],winner_max[1]


