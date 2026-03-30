# Assignment-2-Sentiment-Analysis-using-Shakespeare

## Approach:

- Removed punctuation manually (cause given txt file was short and to not unecessarily overengineer project) 

- Read text from txt file 

- Convert all text to lowercase

- Split text into words (tokenization)

- Compare each word with:

  - A list of positive words
  
    - if true add one to sentiment of sentence
  
  - A list of negative words
  
    - if true substract one from sentiment of sentence

- Classify sentiment:

  - Positive (sentiment > 0)
  
  - Negative (sentiment < 0)
  
  - Neutral (sentiment = 0)
  
- print final result

## Possible Improvements:

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

## Output

line=not marble nor the gilded monuments

sentiment=neutral

line=of princes shall outlive this powerful rhyme

sentiment=positive

line=but you shall shine more bright in these contents

sentiment=positive

line=than unswept stone besmeared with sluttish time

sentiment=negative

line=when wasteful war shall statues overturn

sentiment=negative

line=and broils root out the work of masonry

sentiment=negative

line=nor mars his sword nor war s quick fire shall burn

sentiment=negative

line=the living record of your memory

sentiment=positive

line=gainst death and all oblivious enmity

sentiment=negative

line=shall you pace forth your praise shall still find room

sentiment=positive

line=even in the eyes of all posterity

sentiment=positive

line=that wear this world out to the ending doom

sentiment=negative

line=so till the judgement that yourself arise

sentiment=positive

## Learnings

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
