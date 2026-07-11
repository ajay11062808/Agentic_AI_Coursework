# Class Hands-on [10]

- Create a HuggingFace pipeline that summarizes large text
- Test it with some large text

HINT:
model = pipeline('summarization', model=MODEL)
text  = '''
'''
result = model(text)
print(result)

### Alternatively, use https://huggingface.co/Harsh-Gupta/t5-small-news-summarizer using 'text-generation' task
### and use max_length=30 for the summarizer

# Homework

- Create a HuggingFace pipeline that take modern English text and converts it into 
Shakespearean English text
- Test it with some samples

# Note

Make sure to install transformers module
- pip install torch
- pip install transformers

# Reference

Huggingface Documentation: https://huggingface.co/docs/transformers/en/main_classes/pipelines
