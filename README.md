# big_data_gen_ai_project
Multi-Model Sentiment Analysis of Tweets using Big Data & Generative AI

 Overview
This project presents a hybrid sentiment analysis framework for large-scale Twitter data, combining Big Data technologies with state-of-the-art Generative AI models.
It processes massive tweet datasets efficiently using Hadoop & Apache Spark while leveraging transformer-based NLP models and Generative AI APIs (OpenAI, Gemini, LLaMA, Grok) for context-rich sentiment classification.

By merging the strengths of distributed computing and advanced AI, this system achieves scalability, robustness, and high semantic accuracy, offering a benchmark approach for modern AI-integrated big data analytics.

Key Features
Distributed Tweet Storage & Processing with Hadoop HDFS & MapReduce

Transformer-based Sentiment Classification using Apache Spark + Hugging Face

Generative AI Sentiment Inference via APIs (OpenAI, Gemini, LLaMA, Grok)

Real-time & Batch Prediction using Puter.js integration layer

Model Agreement Analysis with Cohen’s Kappa & MCC

Scalable Architecture for millions of tweets

System Architecture
Data Storage & Preprocessing

Tweets stored in HDFS for distributed access

MapReduce jobs for cleaning, filtering, and normalization

Sentiment Classification

Spark + Hugging Face Transformers for large-scale, fast classification

Generative AI models for context-rich inference via API calls

Integration & Evaluation

Outputs merged in the Python backend

Evaluation with Accuracy, Precision, Recall, F1, Cohen’s Kappa, MCC

 Dataset
Source: Sentiment140 Dataset

Size for Experiment: 15,000 curated tweets (balanced sentiment distribution)

Scalable to: Full dataset (~1.6M tweets)

Results Summary
Model Type	Strengths	Limitations
Hugging Face Transformers: Consistent, scalable, fast batch processing, slightly less context-sensitive
Generative AI (OpenAI, Gemini, LLaMA, Grok)	High precision & nuanced understanding	API cost, slower throughput

 Tech Stack
 
Big Data:

Hadoop HDFS

MapReduce

Apache Spark

NLP Models:

Hugging Face Transformers (BERT, RoBERTa, etc.)

Spark NLP

Generative AI APIs:

OpenAI (ChatGPT)

Google Gemini

Meta LLaMA

xAI Grok

Integration & Backend:

Puter.js (JavaScript API layer)

Python (Pandas, NumPy, Scikit-learn)

Evaluation Metrics
Accuracy

Precision, Recall, F1-score

Cohen’s Kappa

Matthews Correlation Coefficient (MCC)

Confusion Matrices
