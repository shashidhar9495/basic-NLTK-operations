#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nltk


# In[ ]:


nltk.download('punkt')


# In[ ]:


nltk.download('stopwords')


# In[ ]:


nltk.download('wordnet')


# In[ ]:


nltk.download('averaged_perceptron_tagger')


# ## Tokenizing words and sentences

# In[ ]:


from nltk.tokenize import word_tokenize,sent_tokenize


# In[ ]:


sentence="Hi there,i am trying to tokenize words and sentences using natural language tool kit. But i was unable to print sentences"
my_words=word_tokenize(sentence)
sentence_tok=sent_tokenize(sentence)


# In[ ]:


words


# In[ ]:


len(sentence_tok)


# ## filteres/stopwords

# In[ ]:


from nltk.corpus import stopwords


# In[ ]:


stop_words=stopwords.words('english')


# In[ ]:


my_stop_words=[words for words in my_words if not words in stop_words]
my_stop_words


# In[ ]:


sentence_filtered=(' ').join(my_stop_words)
sentence_filtered


# ## stemmers for filtering suffixes

# In[ ]:


from nltk.stem import PorterStemmer


# In[ ]:


ps=PorterStemmer()
for word in my_words:
    print(ps.stem(word))


# ## Lemmatizer(plural to singular and convert to positive degree)

# In[ ]:


from nltk.stem import WordNetLemmatizer


# In[ ]:


lemmatizer=WordNetLemmatizer()
print(lemmatizer.lemmatize('barks'))


# In[ ]:


## parts of speach tagger**


# In[ ]:


tagged_words=nltk.pos_tag(my_words)


# In[ ]:


tagged_words


# ## synonyms and word definitions

# In[ ]:


from nltk.corpus import wordnet as wn


# In[ ]:


print(wn.synsets('scribble'))


# In[ ]:


wn.synset('scribble.n.01').lemma_names()


# In[ ]:


wn.synset('scribble.n.01').definition()


# In[ ]:




