# Article-Summarizer-and-image-generator

using the following libraries:
• sumy
• wand
• newspaper
• requests


The following methods are available in sumy library and can be used or nlp method can be used.
 Luhn - heurestic method
• Edmundson heurestic method with previous statistic research
• Latent Semantic Analysis, LSA 
• LexRank - Unsupervised approach inspired by algorithms PageRank and HITS
• TextRank - Unsupervised approach, also using PageRank algorithm
• SumBasic - Method that is often used as a baseline in the literature.
• KL-Sum - Method that greedily adds sentences to a summary so long as it decreases the KL Divergence. 
• Reduction - Graph-based summarization, where a sentence salience is computed as the sum of the weights of its edges to other sentences. The weight of an edge between two sentences is computed in the same manner as TextRank


 sumy lex-rank --length=10 --url=https://abc           can be used to summerize the article
  But this program is also about image generation so..
  
