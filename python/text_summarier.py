# Summarizer For text documents
import re
import nltk
nltk.download ('stopwords')
import heapq

def summarize_text (text, num_sent):               
    # Preprocessing the text
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
    return best_sentences

text = """Here's a term you're going to hear much more often: plug-in vehicle, and the acronym PEV. It's what you and many other people will drive to work in, ten years and more from now. At that time, before you drive off in the morning you will first unplug your car - your plug-in vehicle. Its big onboard batteries will have been fully charged overnight, with enough power for you to drive 50-100 kilometres through city traffic. When you arrive at work you'll plug in your car once again, this time into a socket that allows power to flow from your car's batteries to the electricity grid. One of the things you did when you bought your car was to sign a contract with your favourite electricity supplier, allowing them to draw a limited amount of power from your car's batteries should they need to, perhaps because of a blackout, or very high wholesale spot power prices. The price you get for the power the distributor buys form your car would not only be most attractive to you, but it would also be a good deal for them too, their alternative being very expensive power form peaking stations. If driving home or for some other reason your batteries looked like running flat, a relatively small, but quiet and efficient engine running on petrol, diesel or compressed natural gas, even bio-fuel, would automatically cut in, driving a generator that supplied the batteries so you could complete your journey. Concerns over 'peak oil', increasing greenhouse gas emissions, and the likelihood that by the middle of this century there could be five times as many motor vehicles registered worldwide as there are now, mean that the world's almost total dependence on petroleum-based fuels for transport is, in every sense of the word, unsustainable. """
summarized = summarize_text (text, 5)
print (summarized)