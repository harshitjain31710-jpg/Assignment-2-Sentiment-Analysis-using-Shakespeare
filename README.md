# Assignment-2-Sentiment-Analysis-using-Shakespeare

## Assignment-2-Sentiment-Analysis-using-Shakespeare

A simple rule-based sentiment analysis system applied to Shakespeare text. 
This project uses basic NLP techniques without any machine learning models 
to classify text as positive, negative, or neutral.

## Approach:

- Removed punctuation manually (since the text file was small, punctuation was removed manually to avoid unnecessary overengineering) 

- Read text from txt file 

- Convert all text to lowercase

- Split text into words (tokenization)

- Compare each word with:

  - A list of positive words
  
    - if true add one to sentiment of sentence
  
  - A list of negative words
  
    - if true subtract one from sentiment of sentence

- Classify sentiment:

  - Positive (sentiment > 0)
  
  - Negative (sentiment < 0)
  
  - Neutral (sentiment = 0)
  
- print final result

## Limitations and Possible Improvements

1. Context-dependent meaning of words

Problem:

Some words can have different meanings depending on context. For example, a word like "fire" may represent destruction (negative) or passion (positive), but the system assigns a fixed sentiment.

Solution:

This limitation cannot be resolved in a rule-based system. It can be improved using machine learning models such as transformers, which understand context by analyzing surrounding words.

2. Limited analysis at line level (especially for plays)

Problem:

The system analyzes each line independently and cannot capture the overall meaning across multiple lines or understand character behavior in plays.

Solution:

This can be improved by introducing memory across lines or grouping dialogues by character, allowing analysis of sentiment over larger text segments instead of individual lines.

3. Limited vocabulary (word list size)

Problem:

The sentiment depends on manually created positive and negative word lists, which are limited and may miss many important words.

Solution:

This can be improved by using larger pre-built sentiment lexicons or databases. In more advanced systems, word embeddings or vector databases can be used to capture richer vocabulary.

## Sample Output

Line: not marble nor the gilded monuments  
Sentiment: Neutral  

Line: of princes shall outlive this powerful rhyme  
Sentiment: Positive  


## Key Learnings


- Importance of text preprocessing in NLP

- How tokenization works

- How rule-based systems operate

- Limitations of simple word-based sentiment analysis

- Difference between rule-based systems and machine learning models

## How to set up and run this assignment.

- Clone the repository:

      git clone https://github.com/harshitjain31710-jpg/Assignment-2-Sentiment-Analysis-using-Shakespeare.git

- Navigate to the folder:

      cd Assignment-2-Sentiment-Analysis-using-Shakespeare

- Run the script:

      python main.py

## Files

- main.py → sentiment analysis code

- sonet.txt → Shakespeare text

- README.md → project documentation

##Result
-The system successfully classifies lines into positive, negative, and neutral categories based on word-level sentiment scoring. 

-Despite the presence of negative words like "death" and "war", many lines are classified as positive due to stronger positive terms such as "shine", "bright", and "praise".

