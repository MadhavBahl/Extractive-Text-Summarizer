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
        # Remove digits
        clean_text = re.sub (r"\d", " ", clean_text)
        # Remove special characters
        clean_text = re.sub (r"\W", " ", clean_text)
        # Remove all the extra spaces with a single space
        clean_text = re.sub (r"\s+", " ", clean_text)
        # return the clean text
        return clean_text

    clean_text = preprocess (text)

    sentences = nltk.sent_tokenize (text)

    # Remove stop words and create a dictionary of word-count
    stop_words = nltk.corpus.stopwords.words('english')

    word_count_dict = {}

    for word in nltk.word_tokenize(clean_text):
        if word not in stop_words:
            if word not in word_count_dict.keys():
                word_count_dict[word] = 1
            else:
                word_count_dict[word] += 1

    # Find the total number of terms (not necessarily unique) = sum of values in the word_count_dict
    total_terms = sum(word_count_dict[term] for term in word_count_dict)

    # Normalize the word-frequency dictionary (weighted word count matrix/dictionary)
    for key in word_count_dict.keys():
        word_count_dict[key] = word_count_dict[key]/total_terms
        
    # Create sentece scores
    sentence_score_dict = {}
    for sentence in sentences:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in word_count_dict.keys():
                # Now here's a problem, very long sentences will always have high scores, so here we can ignore very long sentences
                if len(sentence.split(' ')) < 20: # ignore sentences having words more than 20
                    if sentence not in sentence_score_dict.keys():
                        sentence_score_dict[sentence] = word_count_dict[word]
                    else:
                        sentence_score_dict[sentence] += word_count_dict[word]

    # Get the summary
    summary = heapq.nlargest(num_sent, sentence_score_dict, key=sentence_score_dict.get)

    # Print the summary
    return summary

webpage = "https://en.wikipedia.org/wiki/Natural_language_processing"
summarize_webpage (webpage, 10)