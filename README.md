# GenAI 

Welcome to **GenAI**, a collection of generative AI projects covering text summarization, emoji generation from facial expressions, and more. This repository serves as a playground for experimenting with **Hugging Face models**, **transformers**, and other AI-based techniques.

---

## Projects in GenAI  

### 1️. **Text Summarization with Multiple Models**  

This project compares different **text summarization models** using **Hugging Face Transformers** and other libraries.  

#### Models Used:
- **[facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn)** (Abstractive Summarization)
- **[google/pegasus-xsum](https://huggingface.co/google/pegasus-xsum)** (Abstractive Summarization)
- **Sumy (LexRank Algorithm)** (Extractive Summarization)
- **[allenai/PRIMERA](https://huggingface.co/allenai/PRIMERA)** (Long-Document Summarization)

#### Model Comparison  

| Model                         | Type         | Summary Style                          | Strengths  | Weaknesses  |
|--------------------------------|-------------|----------------------------------------|------------|-------------|
| **BART (facebook/bart-large-cnn)**  | Abstractive | Extracts key sentences | Good for document summarization | May rely on first few sentences |
| **Pegasus (google/pegasus-xsum)**   | Abstractive | Headline-style, concise | Captures gist well | May lose finer details |
| **Sumy (LexRank Algorithm)**        | Extractive  | Concatenates key sentences | Simple and fast | Not truly abstractive |
| **PRIMERA (allenai/PRIMERA)**       | Abstractive | Summarizes long texts | Handles complex documents | Requires more computation |


