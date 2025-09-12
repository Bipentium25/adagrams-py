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
    for i in range(10):
        rand_index = random.randint(0,pool_size-1)
        hand_cards.append(pool[rand_index])
        pool.pop(rand_index)
        pool_size -= 1
    pool += hand_cards
    return hand_cards

def uses_available_letters(word, letter_bank):
    word = word.upper()
    letterbank_copy = letter_bank[:]
    if len(word) > 10:
        return False
    for letter in word:
        if letter not in letterbank_copy:
            return False
        else:
            letterbank_copy.remove(letter)

    return True

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
    for i in range(1, len(word_list)):
        current_score = score_word(word_list[i])
        ### cases where update needed
        if current_score > winner_max[1]:
            winner_max = [word_list[i], current_score]
        elif current_score == winner_max[1]:
            if len(word_list[i]) != 10 and len(winner_max[0])!= 10:
                if len(word_list[i]) < len(winner_max[0]):
                    winner_max = [word_list[i], current_score]
            elif len(word_list[i]) == 10 and len(winner_max[0])!= 10:
                winner_max = [word_list[i], current_score]
    
    return winner_max[0],winner_max[1]


