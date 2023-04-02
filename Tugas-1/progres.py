# menghitung banyaknya dokumen
# dataset
import math
import pandas as pd
data = [['kirim', 'cepat', 'tas', 'bagus', 'bahan', 'gambar', 'nyata', 'bagus', 'kayak', 'tas', 'mahal'],
        ['udah', 'langanan', 'gagal', 'cinta'],
        ['bagus', 'banget', 'sumpah', 'murah', 'banget', 'nemu', 'persis', 'gin', 'jual', 'ribu', 'alias', 'lebih', 'ekpektasi'],
        ['mantap', 'banget', 'emas', 'kasih', 'bungkus', 'gelembung', 'tolong', 'kualitas', 'emas', 'tingkat', 'khawatir', 'gencet', 'kaya', 'rada', 'gepeng'],
        ['alias', 'emang', 'kecewa', 'harga', 'murah', 'kualitas', 'murah', 'terimakasih', 'jual'],
        ['baik', 'ga', 'kecewa', 'beli'],
        ['bagus', 'banget', 'kek', 'liat', 'mahal', 'ribu', 'bagus', 'suka', 'banget', 'kirim', 'cepat', 'banget', 'kemarin', 'kirim', 'dzuhur', 'udah', 'sampe'],
        ['logo', 'foto', 'gitu', 'cuman', 'oke', 'bahan', 'oke', 'kirim', 'oke', 'bahan', 'tebal'],
        ['harga', 'ribu', 'dapet', 'tas', 'bagus', 'pesan', 'gak', 'kecewa', 'wajib', 'pesan'],
        ['asli', 'indah', 'banget', 'tas', 'suka', 'nambah', 'bingung']]

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
df = pd.DataFrame(tf_idf, columns=tf.keys(), index=["doc_" + str(i) for i in range(len(data))])

print(df.transpose())