# Text Summarization with Multiple Models

## Overview  
This project implements and compares various **text summarization models**, including **abstractive** and **extractive** approaches.  
It utilizes **Hugging Face's Transformers**, the **Sumy** library, and **AllenAI's PRIMERA** model to generate summaries and evaluate their effectiveness.  

## Models Used  

### 1️. facebook/bart-large-cnn (Abstractive Summarization)  
- Extracts key information from the input text.  
- Tends to use the **first few sentences** as a summary.  

### 2️. google/pegasus-xsum (Abstractive Summarization)  
- Provides a **headline-style summary**, capturing the **gist** of the text.  
- More effective for concise summarization.  

### 3️. Sumy (Extractive Summarization - LexRank Algorithm)  
- Selects and concatenates key sentences from the input text.  
- Does not generate new sentences but extracts important ones.  

### 4️. allenai/PRIMERA (Abstractive Summarization for Long Texts)  
- Designed for **long-form document summarization**.  
- Uses **transformers** to create coherent summaries.  

---

## 📂 Project Structure  

