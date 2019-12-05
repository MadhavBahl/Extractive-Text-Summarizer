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
7. Assign score to each sentence
8. Rank inidivivdual sentences according to weight and extract `n` highest ranked sentences

## Steps involved illustrated - 

1. Read the text

Read a text document, or ask input from user. Here we create a function which would take the input text and return the summarized text. The second argument to the function is the number of high scored senteces which you want to extract

```python
def summarize_text (text, num_sent):
    ...
    ...
    return summary
```

2. Pre-process the data

Steps and code as shown below - 

```python
def preprocess (text):
    # Remove those reference links (wiki) eg [8]
    text = re.sub (r"\[[0-9]*\]*", " ", text)
    # Convert to lower case
    clean_text = text.lower()
    # Remove special characters
    clean_text = re.sub (r"\W", " ", clean_text)
    # Remove digits
    clean_text = re.sub (r"\d", " ", clean_text)
    # Remove all the extra spaces with a single space
    clean_text = re.sub (r"\s+", " ", clean_text)
    # return the clean text
    return clean_text
```

3. Tokenize the data into sentences

We use `sent_tokenize()` provided by `nltk` library

```python
sentences = nltk.sent_tokenize (text)
```

4. Remove stop words

Again, we use `nltk`

```python
stop_words = nltk.corpus.stopwords.words('english')
```

5. (contd. from 4) Remove stop words and create word count dictionary

```python
word_count_dict = {}

for word in nltk.word_tokenize(clean_text):
    if word not in stop_words:
        if word not in word_count_dict.keys():
            word_count_dict[word] = 1
        else:
            word_count_dict[word] += 1
```

6. Normalize the word-frequency dictionary (weighted word count matrix/dictionary)

```python
max_value = max(word_count_dict.values())
    for key in word_count_dict.keys():
        word_count_dict[key] = word_count_dict[key]/max_value
```

7. Assign scores to each sentence

```python
sentence_score_dict = {}
for sentence in sentences:
    for word in nltk.word_tokenize(sentence.lower()):
        if word in word_count_dict.keys():
            if len(sentence.split(' ')) < 25: # 25 taken at random, to remove very long sentences
                if sentence not in sentence_score_dict.keys():
                    sentence_score_dict[sentence] = word_count_dict[word]
                else:
                    sentence_score_dict[sentence] += word_count_dict[word]
```

8. Rank inidivivdual sentences according to weight and extract `n` highest ranked sentences

```python
best_sentences = heapq.nlargest(num_sent, sentence_score_dict, key=sentence_score_dict.get)
```