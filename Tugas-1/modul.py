from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re
from translate import Translator
import pandas as pd
import math

class textPreprocessing:

    def __init__(self) -> None:
        pass
    
    # Method untuk melakukan tokenisasi pada setiap kalimat
    def tokenize(self, kalimat): 
        self.token = []
        for kata in kalimat.split():
            self.token.append(kata)
        return self.token
    
    # Method untuk melakukan stopword removal
    def stopword(self, array):
        stop_words = set(stopwords.words('indonesian'))

        self.stopWords = []
        for sentence in array:
            filtered_sublist = [word for word in sentence if word not in stop_words]
            self.stopWords.append(filtered_sublist)
        
        return self.stopWords
    
    # Method untuk melakukan stemming (nazief stemmer)
    def stemming(self, array):
        stemmer_factory = StemmerFactory()
        nazief_stemmer = stemmer_factory.create_stemmer('nazief')

        self.stem = []
        for data in array:
            stemmed = [nazief_stemmer.stem(word) for word in data]
            self.stem.append(stemmed)
        
        return self.stem
    
    # Method untuk konversi kalimat ke lower case dan menghilankan numeric
    def lowerAndNumRemover(self, array):
        self.lower = []
        for i in array:
            noDigit = ""
            for alpabet in i:
                if not alpabet.isdigit():
                    noDigit += alpabet
            self.lower.append(noDigit.lower())
        
        return self.lower
    
    # Method untuk menghilangkan tanda baca pada kalimat
    def punctuationRemover(self, array):
        self.remove = []
        for i in array:
            clean_text = re.sub(r'[^\w\s]', '', i)
            self.remove.append(clean_text)
        
        return self.remove
    
    # Method untuk menghilangkan emoji pada kalmat
    def removeEmoji(self, array):
        self.noEmoji = []
        emoj = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
            u"\U00002500-\U00002BEF"  # chinese char
            u"\U00002702-\U000027B0"
            u"\U00002702-\U000027B0"
            u"\U000024C2-\U0001F251"
            u"\U0001f926-\U0001f937"
            u"\U00010000-\U0010ffff"
            u"\u2640-\u2642" 
            u"\u2600-\u2B55"
            u"\u200d"
            u"\u23cf"
            u"\u23e9"
            u"\u231a"
            u"\ufe0f"  # dingbats
            u"\u3030"
                        "]+", re.UNICODE)
        for i in array:
            remove = re.sub(emoj, '', i)
            self.noEmoji.append(remove)

        return self.noEmoji
    
    # Method untuk mengubah kata yang memiliki banyak huruf berulang menjadi satu huruf
    def normalize(self, array):
        self.clean_text = []
        for i in array:
            normalisasi = re.sub(r'(\w)\1+', r'\1', i)
            self.clean_text.append(normalisasi)

        return self.clean_text
    
    # Method untuk merubah singkatan kata menjadi kata sebenarnnya
    def abbreviation(self, text):
        abbr_dict = {
            'bgs': 'bagus','bgt': 'banget',
            'cpt': 'cepat','gpp': 'gak apa-apa',
            'jgn': 'jangan','msh': 'masih',
            'nanya': 'bertanya','nggak': 'tidak',
            'pdhl': 'padahal','prnh': 'pernah',
            'smua': 'semua','suka2': 'suka-suka',
            'sukaaa': 'suka sekali','sya': 'saya',
            'tggu': 'tunggu','tokped': 'tokopedia',
            'trs': 'terus','sumph':'sumpah',
            'jg':'juga','murh':'murah',
            'gw':'aku','prsis':'persis',
            'ngk':'tidak','rb':'ribu',
            'tdi':'tadi','prna':'pernah',
            'bgus':'bagus','pdhal':'padahal',
            'cman':'cuma','cpet':'cepat',
            'kmrin':'kemarin','udh':'udah',
            'gk':'gak','nggk':'tidak',
            'lgi':'lagi','bangt':'banget',
            'bublewrap':'pembungkus gelembung','seler':'penjual',
            'thanks':'terimakasih', 'god':'bagus',
            'order':'pesan', 'wahib':'wajib',
            'emg':'memang', 'pengirimanya':'kirim',
            'pengiriman':'kirim', 'sebagus':'bagus',
            'gak':'tidak', 'sih':'',
            'tasnya':'tas', 'bahanya':'bahan',
            'gapernah':'tidak pernah', 'wkkk':'',
            'wk':'', 'ny':'',
            'gtu':'gitu','nya':'',
            'dibawah':'di bawah','d':'di',
            'woy':'','ngecewain':'kecewa',
            'kualitasnya':'kualias'
            
        }
        pattern = re.compile(r'\b(' + '|'.join(abbr_dict.keys()) + r')\b')
        # Replace the abbreviations with their expanded forms
        text = pattern.sub(lambda x: abbr_dict[x.group()], text)
        return text
    
    # Method untuk melakukan translate kata binggris ke indo
    def translate(self, array):
        translator = Translator(to_lang="id")
        self.translated = []
        for i in array:
            translation = translator.translate(i)
            self.translated.append(translation)
        
        return self.translated
    

def oneHotEncoder(data):
    # One-hot encoding
    one_hot = {}
    for doc in data:
        for word in doc:
            one_hot[word] = [1 if word in doc else 0 for doc in data]
    # Convert to dataframe
    df = pd.DataFrame(one_hot, index=["doc_" + str(i+1) for i in range(len(data))])

    return df

def basicBow(data):
    # inisialisasi vocabulary
    vocabulary = set()
    for d in data:
        for word in d:
            vocabulary.add(word)
            
    # inisialisasi empty array untuk menampung bag-of-words
    bag_of_words = []
    for d in data:
        row = []
        for word in vocabulary:
            count = d.count(word)
            row.append(count)
        bag_of_words.append(row)
    df = pd.DataFrame(bag_of_words, columns=list(vocabulary), 
                      index=["doc_" + str(i+1) for i in range(len(data))])
    return df.transpose()

def TFIDF(data):
    n = len(data)
    # membuat dictionary term frequency
    tf = {}
    for i in range(n):
        for term in data[i]:
            if term not in tf:
                tf[term] = [0] * n
            tf[term][i] += 1       
    # menghitung inverse document frequency
    idf = {}
    for term in tf.keys():
        df = sum([1 for freq in tf[term] if freq > 0])
        idf[term] = math.log10(n/df)     
    # menghitung term frequency - inverse document frequency (TF-IDF)
    tf_idf = {}
    for term in tf.keys():
        tf_idf[term] = [freq*idf[term] for freq in tf[term]]
    # membuat dataframe dari dictionary tf_idf
    df = pd.DataFrame(tf_idf, columns=tf.keys(), index=["doc_" + str(i+1) for i in range(len(data))])

    return df.transpose()