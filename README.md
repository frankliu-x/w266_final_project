# Aspect-based Sentiment Analysis with Fine-tuned BERT  

### Fenghe Liu(fenghe.liu@berkeley.edu), Haoyu Zhang (haoyuzhang@berkeley.edu)
School of Information, University of California, Berkeley


## Abstract

Aspect-based sentiment analysis performs sentiment classification over multiple aspects. Apart from most recent work using graph neural networks such as relational graph attention network (R-GAT), this paper utilized the pretrained BERT to conduct classification tasks on SemEval 2014 datasets via several fine-tuning approaches. In order to achieve a comparable performance, several fine-tuning BERT approaches have been researched, which include selecting hidden states from intermediate layers, freezing various percentages of pre-trained model parameters and summing states of two hidden layers. The proposed BERT based method in this report achieves the classification accuracy of 86.61% and F1-score of 80.95%. 


## Links to Files

[Report](Aspect-based%20Sentiment%20Analysis%20with%20Fine-tuned%20BERT.pdf)\
[Model Training](ABSA_BERT_frozen.ipynb)
