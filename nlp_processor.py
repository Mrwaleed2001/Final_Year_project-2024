import warnings
import string
import nltk 
from nltk.corpus import stopwords


# You only need to run this line once
nltk.download("stopwords")


class NLP_Processor():

    @staticmethod
    def preprocessor(dataframe):
        questions_preprocessed={}
        for col in dataframe.columns:
            #Initialization for each column
            pre_processed_response = []
            lower_words=[]
            lower_sentences=[]
            lower_without_punctuation=[]
            lower_without_special_characters=[]
            lower_without_stopwords = []
            lower_without_digits = []
            no_null_all_lower = []
            stopwords_english = stopwords.words('english')
            
            #responses to a question
            responses = list(dataframe[col])
            
            #lowercase responses
            lower_responses = [response.lower() for response in responses]
            
            #Breaking each response word by word
            lower_words = [response.split() for response in lower_responses]
            
            #Removing punctuations
            for i in range(len(lower_words)):
                lower_words[i] = [word for word in lower_words[i] if word not in string.punctuation]
            lower_without_punctuation= lower_words
            
            #Removing special characters
            for i in range(len(lower_without_punctuation)):
                lower_without_punctuation[i] = [''.join(c for c in word if c.isalnum()) for word in lower_without_punctuation[i]]
            lower_without_special_characters = lower_without_punctuation
            
            #Removing stopwords like the, a, and an etc.
            for i in range(len(lower_without_special_characters)):
                lower_without_special_characters[i] = [word for word in lower_without_special_characters[i] if word not in stopwords_english]
            lower_without_stopwords=lower_without_special_characters
            
            #Removing digits
            for i in range(len(lower_without_stopwords)):
                lower_without_stopwords[i] = [''.join(c for c in word if not c.isdigit()) for word in lower_without_stopwords[i]]
            lower_without_digits = lower_without_stopwords
            
            #Removing null values ""
            for i in range(len(lower_without_digits)):
                lower_without_digits[i] = [word for word in lower_without_digits[i] if word != ""]
            no_null_all_words = lower_without_digits
            
            #Combining words for each response as complete sentence for stemming or lemmatization
            pre_processed_response = [' '.join(response) for response in no_null_all_words]
            
            #Updating in dictionary for each column
            questions_preprocessed.update({col:pre_processed_response})
            
        return questions_preprocessed
    
    # Define function for tokenizing and stemming documents
    @staticmethod
    def stem(text):
        tokens = nltk.word_tokenize(text)
        stems = []
        for item in tokens:
            stems.append(nltk.PorterStemmer().stem(item))
        return stems

    # Define function for tokenizing and lemmatizing documents
    @staticmethod
    def lemmatizer(text):
        tokens = nltk.word_tokenize(text)
        lemmas = []
        for item in tokens:
            lemmas.append(nltk.stem.WordNetLemmatizer().lemmatize(item))
        return lemmas