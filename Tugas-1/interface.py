import streamlit as st
import pandas as pd
import modul
from modul import textPreprocessing
# st.set_page_config(language='id')

process = textPreprocessing() # Deklarasi objek dari class textPreprocessing yang ada di modul
dataset = pd.read_excel("C:/Users/hp/OneDrive/Documents/Belajar Pemrograman/PPDM/dataset/Dataset C.xlsx")
datasetProces = dataset['Reviews'].iloc[20:30]

st.title(
    '''
    Program Text Pre-Processing Pengantar Pemrosesan Data Multimedia
    '''
)
st.write(
    '''
    Diberikan sebuah dataset yang bernama "Dataset C". 
    Dalam dataset, terdapat ratusan dokumen yang berisi 
    kalimat bahasa indonesia. Pada dashboard ini, akan dilakukan
    text pre-processing pada 10 dokumen dari dataset tersebut.
    '''
)

with st.expander('SAMPLING DATASET'):
    # Import Library
    st.header("Import Library")
    st.code(
        '''
        import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from translate import Translator
        '''
    )
    #Import library end

    # Read dataset
    st.subheader(' Baca dataset')
    st.code(
        '''
        df = pd.read_excel("dataset/Dataset C.xlsx")
print(df)
        '''
    )
    st.dataframe(dataset)
    st.code("dataset.shape")
    st.write(dataset.shape)
    st.write("terdapat 200 dokumen dalam dataset")
    # Read dataset end

    # Sampling dataset
    st.subheader("Ambil sepuluh dokumen dari dataset (21 s.d. 30)")
    st.code("df = df.iloc[20:30, :]\nprint(df)")
    st.write(dataset.iloc[20:30, :])
    st.write("""Setelah diambil 10 dokumen dari dataset, 
    berikutnya akan dilakukan proses lexical analysis pada 
    dataset, seperti case folding, remove emot, tanda baca, dan lain-lain""")
    # Sampling dataset end


with st.expander('LEXICAL ANALYSIS'):
    # Konversi ke lower case and remove angka
    st.subheader('Konversi ke lower case dan hilangkan angka')
    st.write("Ambil kolom Reviews pada dataset karena hanya kolom itu yang akan diolah")
    st.code("df_proces = df['Reviews']\nprint(df_proces)")
    st.write(dataset['Reviews'].iloc[20:30])
    st.write("Proses konversi ke lower case dan menghilangkan angka")
    st.code(
        '''
        lower = []
for i in df_proces:
    noDigit = ""
    for alpabet in i:
        if not alpabet.isdigit():
            noDigit += alpabet
    lower.append(noDigit.lower())
df_proces = lower
print(df_proces)'''
    )
    datasetProces = process.lowerAndNumRemover(datasetProces)
    st.dataframe(datasetProces)
    # Konversi ke lower case and remove angka end

    # REMOVE EMOJI
    st.write("Setelah melakukan konversi ke lower case, sekarang kita hilangkan emoji yang ada pada dataset")
    st.subheader("Remove Emoji")
    datasetProces = process.removeEmoji(datasetProces)
    st.code(
        '''
        # Fungsi remove emoji
def remove_emojis(data):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
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
        u"\ufe0f"
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', data)

noEmoji = []
for i in df_proces:
    noEmoji.append(remove_emojis(i))
df_proces = noEmoji
print(df_proces)
        '''
    )
    st.dataframe(datasetProces)
    # REMOVE EMOJI END

    # REMOVE TANDA BACA
    datasetProces = process.punctuationRemover(datasetProces)
    st.write("Sekarang kita akan menghilangkan tanda baca yang ada pada dataset")
    st.subheader("Remove Tanda Baca")
    st.code(
        '''removeTandaBaca = []
for i in df_proces:
    clean_text = re.sub(r'[^\w\s]', '', i)
    removeTandaBaca.append(clean_text)
df_proces = removeTandaBaca
print(df_proces)'''
    )
    st.dataframe(datasetProces)
    # REMOVE TANDA BACA END

    # NORMALISASI
    datasetProces = process.normalize(datasetProces)
    st.write("""Sekarang kita akan melakukan normalisasi pada 
    dataset, yaitu menghilangkan huruf yang berulang pada setiap
    kata, seperti kata 'bagussss' menjadi 'bagus'.""")
    st.subheader("Normalisasi Kata")
    st.code(
        '''# Menghilangkan huruf yang berulang
kalimatTidakPanjang = []
for i in df_proces:
    kalimat_normalisasi = re.sub(r'(\w)\1+', r'\1', i)
    kalimatTidakPanjang.append(kalimat_normalisasi)

df_proces = kalimatTidakPanjang
print(df_proces)'''
    )
    st.dataframe(datasetProces)
    # NORMALISASI END

    # ABBREVIATION
    for i, text in enumerate(datasetProces):
        datasetProces[i] = process.abbreviation(text)

    st.write('''Sekarang kita akan melakukan abbreviation,
     yaitu mengubah singkatan kata menjadi kata sebenarnya, 
     seperti "bgs" menjadi "bagus".''')
    st.subheader("Abbreviation")
    st.code(
        '''def expand_abbr(text):
    abbr_dict = {
        'bgs': 'bagus',
        'bgt': 'banget',
        'cpt': 'cepat',
        'gpp': 'gak apa-apa',
        'jgn': 'jangan',
        'msh': 'masih',
        'nanya': 'bertanya',
        'nggak': 'tidak',
        'pdhl': 'padahal',
        'prnh': 'pernah',
        'smua': 'semua',
        'suka2': 'suka-suka',
        'sukaaa': 'suka sekali',
        'sya': 'saya',
        'tggu': 'tunggu',
        'tokped': 'tokopedia',
        'trs': 'terus',
        'sumph':'sumpah',
        'jg':'juga',
        'murh':'murah',
        'gw':'aku',
        'prsis':'persis',
        'ngk':'tidak',
        'rb':'ribu',
        'tdi':'tadi',
        'prna':'pernah',
        'bgus':'bagus',
        'pdhal':'padahal',
        'cman':'cuma',
        'cpet':'cepat',
        'kmrin':'kemarin',
        'udh':'udah',
        'gk':'gak',
        'nggk':'tidak',
        'lgi':'lagi',
        'bangt':'banget',
        'bublewrap':'pembungkus gelembung',
        'seler':'penjual',
        'thanks':'terimakasih',
        'god':'bagus',
        'order':'pesan',
        'wahib':'wajib',
        'emg':'memang'
    }
    pattern = re.compile(r'\b(' + '|'.join(abbr_dict.keys()) + r')\b')
    text = pattern.sub(lambda x: abbr_dict[x.group()], text)
    return text

for i, text in enumerate(df_proces):
    df_proces[i] = expand_abbr(text)

print(df_proces)'''
    )
    st.dataframe(datasetProces)
    # ABBREVIATION END

    # TRANSLATE
    datasetProces = process.translate(datasetProces)
    st.write("Sekarang kita akan menerjemahkan kata yang berbahasa inggris, menjadi bahasa indonesia")
    st.subheader("Translate Setiap Kata Bahasa Inggris")
    st.code(
        '''# Translate kata yang berbahasa inggris menjadi bahasa indonesia
translator = Translator(to_lang="id")
translated = []
for i in df_proces:
    translation = translator.translate(i)
    translated.append(translation)
df_proces = translated
print(df_proces)'''
    )
    st.dataframe(datasetProces)
    st.write("Sekarang saatnya kita melakukan tokenisasi pada dataset")
    # TRANSLATE END


with st.expander("TOKENIZATION"):
    # TOKENISASI
    dataset_token = []
    for i in range(len(datasetProces)):
        token = process.tokenize(datasetProces[i])
        dataset_token.append(token)
    st.subheader("Tokenisasi")
    st.code(
        '''# Fungsi untuk melakukan tokenisasi pada setiap kalimat
def tokenisasi(kalimat):
    token = []
    for kata in kalimat.split():
        token.append(kata)
    return token

# Tokenisasi setiap kalimat dalam dataset
dataset_token = []
for i in range(len(datasetProces)):
    token = tokenisasi(datasetProces[i])
    dataset_token.append(token)

# Output hasil tokenisasi
print(dataset_token)'''
    )
    st.write(dataset_token)
    st.write("Setelah dokumen ditokenisasi, sekarang kita akan melakukan stop word, yaitu menghilangkan kata-kata yang tidak berarti")
    # TOKENISASI END


with st.expander("STOP WORD REMOVAL"):
    # STOPWORD
    dataset_token = process.stopword(dataset_token)
    st.subheader("Stop Word")
    st.code(
        '''stop_words = set(stopwords.words('indonesian'))

stopWord = []
for i in dataset_token:
    filtered_sublist = [word for word in i if word not in stop_words]
    stopWord.append(filtered_sublist)
dataset_token = stopWord
print(dataset_token)'''
    )
    st.write(dataset_token)
    # STOPWORD END


with st.expander("STEMMING"):
    # STEMMING
    dataset_token = process.stemming(dataset_token)
    st.subheader("Proses Stemming")
    st.code(
        '''stemmer_factory = StemmerFactory()
nazief_stemmer = stemmer_factory.create_stemmer('nazief')

stem = []
for data in dataset_token:
    stemmed = [nazief_stemmer.stem(word) for word in data]
    stem.append(stemmed)
dataset_token = stem
print(dataset_token)'''
    )
    st.write(dataset_token)
    # STEMMING END

## OUTPUT
st.subheader("OUTPUT")
st.write('''Setelah semua dokumen selesai dilakukan pre-processing
Sekarang kita bentuk output dari dataset tersebut. Output akan
dijabarkan dalam beberapa bentuk.''')

with st.expander("One-hot Encoding"):
    onehot = modul.oneHotEncoder(dataset_token)
    st.code(
        '''one_hot = {}
for doc in dataset_token:
    for word in doc:
        one_hot[word] = [1 if word in doc else 0 for doc in dataset_token]

df = pd.DataFrame(one_hot, index=["doc_" + str(i) for i in range(len(dataset_token))])
df.transpose()'''
    )
    st.dataframe(onehot.transpose())

with st.expander("Basic Bag-of-words"):
    bowBasic = modul.basicBow(dataset_token)
    st.code(
        '''def basicBow(data):
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
    df = pd.DataFrame(bag_of_words, columns=list(vocabulary), index=["doc_" + str(i) for i in range(len(data))])
    return df.transpose()

basicBow(dataset_token)'''
    )
    st.dataframe(bowBasic)


with st.expander("Bag-of-words TFIDF"):
    TFIDF = modul.TFIDF(dataset_token)
    st.code(
        '''n = len(dataset_token)
# membuat dictionary term frequency
tf = {}
for i in range(n):
    for term in dataset_token[i]:
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
df = pd.DataFrame(tf_idf, columns=tf.keys(), index=["doc_" + str(i) for i in range(len(dataset_token))])

print(df.transpose())'''
    )
    st.dataframe(TFIDF)