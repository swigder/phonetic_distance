# phonetic_distance
This library includes methods for determining the phonetic closeness of two words, and for determining the words out of a list of words that are closest to a target word.  The default implementation uses CMUDict to obtain phonetic information of words, and ignores stress when determining phonetic distance.  It then uses the minimum edit distance algorithm to determine the difference between the phones of the given words.  This algorithm uses only the individual phones, and does not consider the relationship of neighboring phones or location in the word (for example, that the last phone of a word may be more likely to be dropped than an initial consonant.

Various metrics are phone edit-cost are provided.  The default gives an edit cost of one for phone addition and deletion, two for unrelated phone substitution, and an intermediate cost for related phone substitution.  Phones are considered related if they fall in the same class, where classes are as follows (from https://en.wikipedia.org/wiki/Arpabet):    
  * vowels = ['AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW']
  * r_colored_vowels = ['ER', 'AXR']
  * stops = ['P', 'B', 'T', 'D', 'K', 'G']
  * affrictaves = ['CH', 'ZH']
  * frictaves = ['F', 'V', 'TH', 'DH', 'S', 'Z', 'SH', 'ZH', 'HH']
  * nasals = ['M', 'EM', 'N', 'EN', 'NG', 'ENG']
  * liquids = ['L', 'EL', 'R', 'DX', 'NX']
  * semivowels = ['Y', 'W', 'Q']


## Prerequisites and required libraries
This package requires python3 to run, uses numpy, nltk, and pytest.  It assumes that the NLTK CMUDict corpus has been installed.  For more information, see http://www.nltk.org/data.html.


## How to run
There are several programs that can be run:
* minimum_phonetic_distance:  Get the phonetic distance between two words.  Run `python3 phonetic_distance.py minimum_phonetic_distance target source`, for example, `python3 phonetic_distance.py minimum_phonetic_distance MONETARY MONOTONE`.
* closest_word:  Get the words in a set of words with the smallest phonetic distance to a given target word.  There are two ways to run this program:
    * find the closest source word from a given list of words:  `python3 phonetic_distance.py closest_word target [sources [sources ...]]`, for example, `python3 phonetic_distance.py closest_word MONETARY MONOTONE COMMENTARY`.
    * find the closest source word in the dictionary that starts with a given letter:  `python3 phonetic_distance.py closest_word [-h] [-fl [FIRST_LETTER]] target`, for example, `python3 phonetic_distance.py closest_word KRYPTON --first_letter c`.
For each program, the optional parameter `-sc --similar_phone_substitution_cost` may be provided, which will override the default cost for similar phone substitutions.  If not provided, the default cost of 1 will be used.


## Included files
* cmu_dict_phonetic_dictionary.py: Facade over the NLTK CMUDict that stores the dictionary in memory for better performance.
* minimum_edit_distance.py: Implementation of the minimum edit distance algorithm using dynamic programming.
* levenshtein_cost_calculator.py: Cost calculator for edit distance using Levenshtein values, for testing the minimum edit distance code.
* minimum_phonetic_distance_calculator.py: Minimum phonetic distance calculator using the minimum edit distance, provided phonetic dictionary, and provided phonetic cost calculator.
* phonetic_cost_calculator.py: Cost calculator for cost of addition, deletion, and substitution of phones, as described above.
* phonetic_distance.py: Command line interface for the above code.
* test/*.py: Test files for the above code. 
