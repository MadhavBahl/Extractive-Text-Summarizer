# Extractive Text Summarizer

Tried to implement a simple extractive summarizer from this paper - [https://pdfs.semanticscholar.org/2df1/595bcbee37de1147784585a097f3a2819fdf.pdf](https://pdfs.semanticscholar.org/2df1/595bcbee37de1147784585a097f3a2819fdf.pdf)

## Steps

### From the above mentioned paper

1. Read a text in and split it intoindividual tokens.
2. Remove the stop words to filter the text
3. Assign a weight value to each individual terms. The weight is calculated as:
    weight = (frequency of that term)/(total number of terms)
4. Add a boost factor to bold, italic or underlined text
5. Rank inidivivdual sentences according to weight
6. Extract `n` highest ranked sentences


