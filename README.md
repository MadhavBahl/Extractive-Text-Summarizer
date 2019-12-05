# Extractive Text Summarizer

![Short Notes](https://user-images.githubusercontent.com/26179770/70233084-e34f4880-1783-11ea-8e33-93093263fa13.png)

This repository contains a very simple imlementation of extractive text summarization. The implemented summarizer was partially implemented from this paper (without adding a boost factor) - [https://pdfs.semanticscholar.org/2df1/595bcbee37de1147784585a097f3a2819fdf.pdf](https://pdfs.semanticscholar.org/2df1/595bcbee37de1147784585a097f3a2819fdf.pdf)

## Steps

### From the above mentioned paper

1. Read a text in and split it intoindividual tokens.
2. Remove the stop words to filter the text
3. Assign a weight value to each individual terms. The weight is calculated as:
    ```
     weight = (frequency of that term)/(total number of terms)
    ```
4. Add a boost factor to bold, italic or underlined text
5. Find the weight of each sentence (sum of individual weights)
6. Rank inidivivdual sentences according to weight
7. Extract `n` highest ranked sentences

### Things implemented

1. Read the text
2. Pre-process the data
   - Convert to lower case
   - Remove special characters
   - Remove digits
   - Remove all the extra spaces with a single space
   - return the clean text
3. Tokenize the data into sentences
4. Remove stop words 
5. Create a word-count dictionary
6. Normalize the word-frequency dictionary (weighted word count matrix/dictionary)
    ```
     weight = (frequency of that word)/(maximum frequency)
    ```
7. Rank inidivivdual sentences according to weight
8. Extract `n` highest ranked sentences