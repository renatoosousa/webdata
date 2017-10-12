Description of Datasets
===================
Description of all data used to train **classifiers**.

----------

Datasets:
-------------

how the data is organized

> **URLS:**

>  **urls.csv** : For 10 different webpages, 10 positive and 10 negative ads.

>  **urls2.csv** : Like urls.csv , some positive and negative examples.

>**BAG OF WORDS:**

>  **db1.csv** : filter (special characters).

>  **db2.csv** : filter (special characters) + lowcase.

>  **db3.csv** : filter (special characters) + lowcase + stemming.

>  **db4.csv** : filter (special characters) + lowcase + NoStopwords.

>  **db5.csv** : filter (special characters and numbers) + lowcase + NoStopwords.

>  **db6.csv** : filter (special characters and numbers) + lowcase + NoStopwords + stemming.

>  **db7.csv** : filter (special characters and numbers) + lowcase + NoStopwords + stemming (best 1000 words).

>  **db8.csv** : filter (special characters and numbers) + lowcase + NoStopwords + stemming (1000 most frequent words).

Table:
------------- 
Number of words for each bag of words before and after the gain of information:


Dataset     | words   | used     
:---------: | :-----: | :---:
db1         | 24041   | No   
db2         | 20565   | Yes  
db3         | 17002   | Yes  
db4         | 20437   | Yes  
db5         | 12127   | No 
db6         | 8658    | Yes  
db7         | 1000    | Yes  
db8         | 1000    | Yes  
