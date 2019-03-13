
# coding: utf-8

# In[1]:


filename = "yes-minister.txt"
with open(filename) as f:
    mytext = f.read()


# In[2]:


mytext


# In[3]:


from wordcloud import WordCloud
wordcloud = WordCloud().generate(mytext)


# In[5]:


get_ipython().run_line_magic('pylab', 'inline')
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")


# In[6]:


from wordcloud import WordCloud
wordcloud = WordCloud().generate(mytext)
get_ipython().run_line_magic('pylab', 'inline')
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")


# In[7]:


from wordcloud import WordCloud
wordcloud = WordCloud().generate(mytext)
get_ipython().run_line_magic('pylab', 'inline')
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

