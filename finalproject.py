
import math

class TextModel:
    """ A data type which will serve as a blueprint for objects that model a body of text (i.e., a collection of one or more text documents).
    """
    
    # Methods
    
    def __init__(self, model_name):
        """ Constructor
        """
        
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.suffixes = {}
        self.personal_pronouns = {}
        self.simile = {}
        
    
    def __repr__(self):
      """ Return a string representation of the TextModel.
      """
      
      s = '  text model name: ' + self.name + '\n'
      s += '  number of words: ' + str(len(self.words)) + '\n'
      s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
      s += '  number of stems: ' + str(len(self.stems)) + '\n'  
      s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n' 
      s += '  number of suffixes: ' + str(len(self.suffixes)) + '\n'
      s += '  number of personal pronouns: ' + str(len(self.personal_pronouns)) + '\n'
      s += '  number of similes: ' + str(len(self.simile)) + '\n'
      
      return s
  
    
    def add_string(self, s):
        """ Analyzes the string txt and adds its pieces to all of the dictionaries in this text model.
        """
        
        # self.sentence_lengths
        wrd_list = s.split()
        count = 0 
        for x in wrd_list:
            count += 1
            if x[-1] == '.' or x[-1] == '?' or x[-1] == '!':
                if x not in self.sentence_lengths:
                    self.sentence_lengths[count] = 1
                    count = 0 
            
        
        # self.words
        word_list = clean_text(s)
        for w in word_list:
            if w not in self.words:
                self.words[w] = 1
            else:
                self.words[w] += 1
                
        
        # self.word_lengths
        count=0
        for q in self.words:
             if len(q) not in self.word_lengths:
                 self.word_lengths[len(q)] = self.words[q] 
             else:
                 count = self.word_lengths[len(q)]
                 count += self.words[q] 
                 self.word_lengths[len(q)] = count
                 
        
        # self.stems
        words = s.split()
        for x in words:
            words = x.split('"')
            for x in words:
                x = stem(x)
                if x not in self.stems:
                    self.stems[x] = 1
                else: 
                    self.stems[x] += 1 
               
                    
        # self.suffixes
        words = s.split()
        for x in words:
            words = x.split('"')
            for x in words:
                y = suffixes(x)
                if y == '':
                    self.suffixes
                elif x not in self.suffixes:
                    self.suffixes[y] = 1
                else:
                    self.suffixes[y] += 1        
                    
                    
        # self.personal_pronouns
        words = s.split()
        for x in words:
            if x == 'you' or x =='I' or x =='she' or x=='he'or x =='them' or x =='me' or x =='him' or x =='her' or x =='us' or x =='it' or x =='You' or x =='She' or x =='He' or x =='Them' or x =='Me' or x =='Him' or x =='Her' or x =='Us' or x =='It' or x =='YOU' or x =='SHE' or x =='HE' or x =='THEM' or x =='ME' or x =='HIM' or x =='HER' or x =='US' or x =='IT':
                if x not in self.personal_pronouns:
                    self.personal_pronouns[x] = 1
                else:
                    self.personal_pronouns[x] += 1
                    
                    
        # self.simile
        words = s.split()
        for x in words:
            if x == 'like' or x == 'Like' or x == 'As' or x == 'as':
                if x not in self.simile:
                    self.simile[x] = 1
                else:
                    self.simile[x] += 1
      
        
    def add_file(self, filename):
        """ Adds all of the text in the file identified by filename to the model.
        """
        
        f = open(filename, 'r', encoding='utf-8-sig', errors='ignore')
        text = f.read()
        f.close()
        self.add_string(text)
        
    
    def save_model(self):
        """ Saves the TextModel object self by writing its various feature dictionaries to files.
        """
        
        d = self.words
        f = open(self.name + '_words', 'w')
        f.write(str(d))
        f.close()
        
        b = self.word_lengths
        h = open(self.name + '_word_lengths', 'w')
        h.write(str(b))
        h.close()
        
        x = self.stems
        y = open(self.name + '_stems', 'w')
        y.write(str(x))
        y.close()
        
        w = self.sentence_lengths
        n = open(self.name + '_sentence_lengths', 'w')
        n.write(str(w))
        n.close()        

        z = self.suffixes
        k = open(self.name + '_suffixes', 'w')
        k.write(str(z))
        k.close()
        
        s = self.personal_pronouns
        j = open(self.name + '_personal_pronouns', 'w')
        j.write(str(s))
        j.close()
        
        c = self.simile
        o = open(self.name + '_simile', 'w')
        o.write(str(c))
        o.close()
        
        
    def read_model(self):
        """ Reads the stored dictionaries for the called TextModel object from their files and assigns them to the attributes of the called TextModel.
        """
        
        f = open(self.name + '_words', 'r')
        d_str = f.read()
        f.close()
        
        self.words = dict(eval(d_str))
        
        b = open(self.name + '_word_lengths', 'r')
        x_str = b.read()
        b.close()
        
        self.word_lengths = dict(eval(x_str))
        
        x = open(self.name + '_stems', 'r')
        y_str = x.read()
        x.close()
        
        self.stems = dict(eval(y_str))
        
        w = open(self.name + '_sentence_lengths', 'r')
        n_str = w.read()
        w.close()
        
        self.sentence_lengths = dict(eval(n_str))
        
        z = open(self.name + '_suffixes', 'r')
        k_str = z.read()
        z.close()
        
        self.suffixes = dict(eval(k_str)) 
        
        s = open(self.name + '_personal_pronouns', 'r')
        j_str = s.read()
        s.close()
        
        self.personal_pronouns = dict(eval(j_str))
        
        c = open(self.name + '_simile', 'r')
        o_str = c.read()
        c.close()
        
        self.simile = dict(eval(o_str))
      
    def similarity_scores(self, other):
        """ Computes and returns a list of log similarity scores measuring the similarity of self and other
        """
        
        score_list = []
        
        word_score = compare_dictionaries(other.words, self.words)
        score_list += [word_score]
        
        word_length_score = compare_dictionaries(other.word_lengths, self.word_lengths)
        score_list += [word_length_score]
        
        stem_score = compare_dictionaries(other.stems, self.stems)
        score_list += [stem_score]
        
        sentence_lengths_score = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        score_list += [sentence_lengths_score]
        
        suffixes_score = compare_dictionaries(other.suffixes, self.suffixes)
        score_list += [suffixes_score]
        
        personal_pronouns_score = compare_dictionaries(other.personal_pronouns, self.personal_pronouns)
        score_list += [personal_pronouns_score]
        
        simile_score = compare_dictionaries(other.simile, self.simile)
        score_list += [simile_score]
        
        return score_list
    
    
    def classify(self, source1, source2):
        """ Compares the called TextModel object (self) to two other “source” TextModel objects (source1 and source2) and determines which of these other TextModels is the more likely source of the called TextModel. 
        """
        
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        
        print()
        print('Is ' + self.name + ' closer to ' + 'the works of ' + source1.name +' or ' + 'to those of ' + source2.name + '?')
        print('---------------------------------------------------------------------------------------------------------------------------')
        print('Scores for' + ' ' + source1.name + ':' + ' ' + str(scores1)) 
        print('Scores for' + ' ' + source2.name + ':' + ' ' + str(scores2)) 
        
        
        weighted_sum1 = 10*scores1[0] + 10*scores1[1] + 2*scores1[2] + 15*scores1[3] + 2*scores1[4]
        weighted_sum2 = 10*scores2[0] + 10*scores2[1] + 2*scores2[2] + 15*scores2[3] + 2*scores1[4]
        
        if weighted_sum1 > weighted_sum2:
            print()
            print(self.name + ' is more alike to the works of ' + source1.name + '!')
            print()
        else:
            print()
            print(self.name + ' is more alike to the works of ' + source2.name + '!')
            print()
            
            
# Helper functions


def clean_text(txt):
    """ Takes a string of text txt as a parameter and returns a list containing the words in txt after it has been “cleaned”. 
    """
    
    for symbol in """.,?"'!;:""":
        if symbol in txt:
            txt = txt.replace(symbol,'')
    return txt.lower().split()


def stem(s):
    """ Accepts a string as a parameter. The function should then return the stem of s.
    """
    
    if s[-3:] == 'ing' or s[-3:] == 'ING':
        s = s[:-3]
    elif s[-4:] == 'ing.' or s[-4:] == 'ING.':
        s = s[:-4]
    elif s[-3:] == 'ion' or s[-3:] == 'ION':
        s = s[:-3]
    elif s[-4:] == 'ion.' or s[-4:] == 'ION.':
        s = s[:-4]
    elif s[-1:] == 's' or s[-1:] == 'S':
        s = s[:-1]
    elif s[-2:] == 's.' or s[-2:] == 'S.':
        s = s[:-2]
    elif s[-2:] == 'er' or s[-2:] == 'ER':
        s = s[:-2]
    elif s[-3:] == 'er.' or s[-3:] == 'ER.':
        s = s[:-3]
    elif s[-3:] == 'ism' or s[-3:] == 'ISM':
        s = s[:-3]
    elif s[-4:] == 'ism.' or s[-4:] == 'ISM.':
        s = s[:-4]
    elif s[-2:] == 'ly' or s[-2:] == 'LY':
        s = s[:-2]
    elif s[-3:] == 'ly.' or s[-3:] == 'LY.':
        s = s[:-3]
    elif s[-4:] == 'ment' or s[-4:] == 'MENT':
         s = s[:-4]
    elif s[-5:] == 'ment.' or s[-5:] == 'MENT.':
        s = s[:-5]
    elif s[-1:] == 'y' or s[-1:] == 'y':
        s = s[:-1]
    elif s [-2:] == 'y.' or s[-2:] == 'y':
        s = s[:-2]
    else:
        s = s
        
    return s

def suffixes(s):
    """ Accepts a string as a parameter. The function should then return the suffix of s.
    """
    
    # More specific suffixes 
    
    if s[-3:] == 'acy' or s[-3:] == 'ACY':
        s = s[-3:]
    elif s[-4:] == 'acy.' or s[-4:] == 'ACY.':
        s = s[-4:]
    elif s[-2:] == 'al' or s[-3:] == 'AL':
        s = s[-2:]
    elif s[-3:] == 'al.' or s[-4:] == 'AL.':
        s = s[-3:]    
    elif s[-3:] == 'dom' or s[-1:] == 'DOM':
        s = s[-3:]
    elif s[-4:] == 'dom.' or s[-4:] == 'DOM.':
        s = s[-4:]
    elif s[-3:] == 'ist' or s[-2:] == 'IST':
        s = s[-3:]
    elif s[-4:] == 'ist.' or s[-3:] == 'IST.':
        s = s[-4:]
    elif s[-4:] == 'ness' or s[-3:] == 'NESS':
        s = s[-4:]
    elif s[-5:] == 'ness.' or s[-4:] == 'NESS.':
        s = s[-5:]
    elif s[-4:] == 'ship' or s[-2:] == 'SHIP':
        s = s[-4:]
    elif s[-5:] == 'ship.' or s[-3:] == 'SHIP.':
        s = s[-5:]
    elif s[-3:] == 'ity' or s[-4:] == 'ITY':
         s = s[-3:]
    elif s[-4:] == 'ity.' or s[-5:] == 'ITY.':
        s = s[-4:]
    elif s[-3:] == 'ize' or s[-1:] == 'IZE':
        s = s[-3:]
    elif s [-4:] == 'ize.' or s[-2:] == 'IZE.':
        s = s[-4:]
    else:
        s = ''
        
    return s


def compare_dictionaries(d1, d2):
    """ Takes two feature dictionaries d1 and d2 as inputs, and it should compute and return their log similarity score
    """
    if d1 == {}:
        return -50
    else:
        score = 0
        
    total = 0
    for y in d1:
        if y in d1:
            total += d1[y]
    
    for x in d2:
        if x in d1:
            score += d2[x] * math.log((d1[x]/total))
        else:
            score += d2[x] * math.log((0.5/total))
    return score


# Tests


def run_tests():
    """ Compares different texts to Shakespeare and Jane Austen
    """
    
    # Complete works of Shakespeare
    source1 = TextModel('Shakespeare')
    source1.add_file('shakespeare_source_text.txt')
    source1.save_model()

    # Complete works of Jane Austen 
    source2 = TextModel('Jane Austen')
    source2.add_file('jane_austen_source_text.txt')
    source2.save_model()

    # Pride and Prejudice is more like...
    new1 = TextModel('Pride and Prejudice')
    new1.add_file('pride_and_prejudice_source_text.txt')
    new1.classify(source1, source2)
    
    # Macbeth is more like...
    new2 = TextModel('Macbeth')
    new2.add_file('macbeth_source_text.txt')
    new2.classify(source1, source2)
    
    # The Odyssey is more like...
    new3 = TextModel('The Odyssey')
    new3.add_file('The_odyssey_source_text.txt')
    new3.classify(source1, source2)
    
    # Anna Karenina is more like...
    new3 = TextModel('Anna Karenina')
    new3.add_file('anna_karenina_source_text.txt')
    new3.classify(source1, source2)
    
    
def test():
    """ your docstring goes here """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)
    
    
    


                            
