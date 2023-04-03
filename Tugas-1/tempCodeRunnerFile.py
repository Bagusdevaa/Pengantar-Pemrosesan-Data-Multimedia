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