# phonetic_distance
This library includes methods for determining the phonetic closeness of two words, and for determining the words out of a list of words that are closest to a target word.  The default implementation uses CMUDict to obtain phonetic information of words, and ignores stress when determining phonetic distance.  It then uses the minimum edit distance algorithm to determine the difference between the phones of the given words.  This algorithm uses only the individual phones, and does not consider the relationship of neighboring phones or location in the word (for example, that the last phone of a word may be more likely to be dropped than an initial consonant.

Various metrics are phone edit-cost are provided.  The default gives an edit cost of one for phone addition and deletion, two for unrelated phone substitution, and an intermediate cost for related phone substitution.  Phones are considered related if they fall in the same class, where classes are as follows (from https://en.wikipedia.org/wiki/Arpabet):    
  * vowels = ['AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW']
  * r_colored_vowels = ['ER', 'AXR']
  *  stops = ['P', 'B', 'T', 'D', 'K', 'G']
  *  affrictaves = ['CH', 'ZH']
  *  frictaves = ['F', 'V', 'TH', 'DH', 'S', 'Z', 'SH', 'ZH', 'HH']
  *  nasals = ['M', 'EM', 'N', 'EN', 'NG', 'ENG']
  *  liquids = ['L', 'EL', 'R', 'DX', 'NX']
  *  semivowels = ['Y', 'W', 'Q']


## Prerequisites and required libraries
This package uses numpy, nltk, and pytest.  It assumes that the CMUDict corpus has been installed.  For more information, see http://www.nltk.org/data.html.
