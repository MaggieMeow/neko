# neko

This is a supplementary material for [our publication to SIGIR ECOM'18 workshop](https://sigir-ecom.github.io/ecom18DCPapers/ecom18DC_paper_7.pdf), where we redefine the classic product categorization task as a sequence generation task. 

This repository contains the following:

 - [PDF draft of the paper](https://github.com/MaggieMeow/neko/blob/master/unconstrained-product-categorization-seq2seq.pdf)
 - [Data Exploratory Experiments](https://github.com/MaggieMeow/neko/blob/master/Seq2Seq%20Product%20Categorization.ipynb) in a Jupyter Notebook

Abstract
====
Product categorization is a critical component of e-commerce plat- forms that enables organization and retrieval of the relevant products. Instead of following the conventional classification approaches, we consider category prediction as a sequence generation task where we allow product categorization beyond the hierarchical definition of the full taxonomy.
Our paper presents our submissions for the [Rakuten Data Challenge](https://sigir-ecom.github.io/data-task.html) at SIGIR eCom’18. The goal of the challenge is to predict the multi-level hierarchical product categories given the e-commerce product titles. We ensembled several attentional sequence-to-sequence models to generate product category labels without supervised constraints. Such unconstrained product categorization suggests possible addition to the existing category hierarchy and reveals ambiguous and repetitive category leaves.

Our system achieved a balanced F-score of 0.8256, while the organizers’ baseline system scored 0.8142, and the best performing system scored 0.8513.

Cite
====


```
Yundi Maggie Li, Liling Tan, Stanley Kok and Ewa Szymanska. 2018. Unconstrained Production Categorization with Sequence-to-Sequence Models. In Proceedings of SIGIR 2018 Workshop on eCommerce (ECOM 18).
```


**Bibtex**:

```
@inproceedings{maggie18,
author= {Yundi Maggie Li and Liling Tan and Stanley Kok and Ewa Szymanska},
title={Unconstrained Product Categorization with Sequence-to-Sequence Models},
booktitle={{SIGIR 2018 Workshop on eCommerce (ECOM 18)}},
year=2018,
}
```
