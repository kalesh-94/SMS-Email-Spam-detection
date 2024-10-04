# SMS-Email-Spam-detection

This project is a Streamlit web application that classifies whether an input message (email or SMS) is spam or not spam using a Machine Learning model trained on text data.

## Overview

The application provides a user-friendly interface where users can input a message and get instant feedback on whether the message is classified as "SPAM" or "NOT SPAM". The classification is based on a pre-trained Machine Learning model and utilizes natural language processing techniques for text preprocessing.

## Features

- **Text Preprocessing**: Converts input text to lowercase, tokenizes, removes stopwords and punctuation, and applies stemming using NLTK.
  
- **Machine Learning Model**: Utilizes a pre-trained model (saved as `model.pkl`) for predicting whether the input message is spam or not.

- **TF-IDF Vectorization**: The application uses TF-IDF vectorization (saved as `vectorizer.pkl`) to transform text data into numerical feature vectors for model prediction.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/your_repository.git
   cd your_repository
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Usage
To run the application, execute the following command:

bash
Copy code
streamlit run app.py
Open your web browser and navigate to the URL provided by Streamlit.

Files Included
app.py: Contains the Streamlit web application code.
model.pkl: Pre-trained Machine Learning model for spam classification.
vectorizer.pkl: Pickled TF-IDF vectorizer for text feature extraction.
About
This project showcases the implementation of a spam detection system using Python, Streamlit, NLTK for text preprocessing, and scikit-learn for machine learning. It serves as an educational tool and a practical example of deploying a Machine Learning model as a web application.

Feel free to explore and modify the code according to your requirements!

Credits
Developed by Your Name.
Dataset source: [available SMS spam on kaggle]
