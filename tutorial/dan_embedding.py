import pandas as pd
import numpy as np
 
df_train = pd.read_csv('../rdc-catalog-train.tsv', sep='\t', header=None)
df_test = pd.read_csv('../rdc-catalog-test.tsv', sep='\t', header=None)
 
df_train = df_train.rename(columns={0:'text', 1:'label'})
df_test = df_test.rename(columns={0:'text', 1:'label'})
 
import tensorflow as tf
import tensorflow_hub as hub
import os
 
module_url = "https://tfhub.dev/google/universal-sentence-encoder/1"
os.environ["TFHUB_CACHE_DIR"] = os.getcwd() + "/tfhub_models2/"
embed = hub.Module(module_url)
 
 
def get_embeddings(text_list):
    with tf.Session() as session:
        session.run([tf.global_variables_initializer(), tf.tables_initializer()])
        sentence_embeddings = session.run(embed(text_list))
    return sentence_embeddings
 
 
train_text = df_train['text'].tolist()
test_text = df_test['text'].tolist()
 
train_embeddings = get_embeddings(train_text)
test_embeddings = get_embeddings(test_text)
 
 
np.save('../test_dan_embedding.npy', test_embeddings)
np.save('../train_dan_embedding.npy', train_embeddings)