# URL Summarizer

import bs4 as bs
import urllib.request
import re
import nltk
nltk.download ('stopwords')
import heapq

def summarize_webpage (url, num_sent):
    # Get the data
    dataSource = urllib.request.urlopen(url).read()

    # parse the HTML document (parser - lxml)
    soup = bs.BeautifulSoup(dataSource, 'lxml')

    # get all <p> tag data in a single string
    text = ""
    for paragraph in soup.find_all('p'):
        text += paragraph.text
        
    # Remove those reference links (wiki) eg [8]
    text = re.sub (r"\[[0-9]*\]*", " ", text)
    # Remove extra spaces
    text = re.sub (r"\s+", " ", text)
        
    # Preprocessing the text
    def preprocess (text):
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

    clean_text = preprocess (text)

    # Tokenize the data into sentences
    def tokenize (text):
        return nltk.sent_tokenize (text)

    sentences = tokenize (text)

    # Remove stop words and create a dictionary of word-count
    stop_words = nltk.corpus.stopwords.words('english')

    word_count_dict = {}

    for word in nltk.word_tokenize(clean_text):
        if word not in stop_words:
            if word not in word_count_dict.keys():
                word_count_dict[word] = 1
            else:
                word_count_dict[word] += 1

    # Normalize the word-frequency dictionary (weighted word count matrix/dictionary)
    max_value = max(word_count_dict.values())
    for key in word_count_dict.keys():
        word_count_dict[key] = word_count_dict[key]/max_value
        
    # Create sentece scores
    sentence_score_dict = {}
    for sentence in sentences:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in word_count_dict.keys():
                if len(sentence.split(' ')) < 25: # 25 taken at random, to remove very long sentences
                    if sentence not in sentence_score_dict.keys():
                        sentence_score_dict[sentence] = word_count_dict[word]
                    else:
                        sentence_score_dict[sentence] += word_count_dict[word]

    # Get the summary
    best_sentences = heapq.nlargest(num_sent, sentence_score_dict, key=sentence_score_dict.get)

    # Print the summary
    print ('/* ================================================ */')
    for sentence in best_sentences:
        print(sentence)
    return best_sentences

webpage = "https://en.wikipedia.org/wiki/Natural_language_processing"
summarize_webpage (webpage, 10)