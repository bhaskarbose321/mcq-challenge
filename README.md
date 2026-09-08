# Smart MCQ Solver

A web application that predicts the correct answer for multiple-choice questions using a BiLSTM model.

## Features

- Enter any MCQ question with up to 5 options (A-E)
- Get instant predictions using a trained BiLSTM model
- Clean, user-friendly interface

## How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Model

The model is a BiLSTM (Bidirectional LSTM) trained on MCQ data. It processes the question and options to predict which option is most likely correct.

## Deployment

This app is deployed on Hugging Face Spaces.
