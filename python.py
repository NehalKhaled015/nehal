import re
from collections import Counter
from nltk.corpus import stopwords

# Download NLTK stopwords if not already downloaded
import nltk
nltk.download('stopwords')

# Define NLTK English stopwords
stop_words = set(stopwords.words('english'))

def remove_stop_words(text):
    # Split the text into words
    words = re.findall(r'\b\w+\b', text.lower())
    # Remove stop words
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words

def count_word_frequency(words):
    # Count the frequency of each word
    word_count = Counter(words)
    return word_count

def main():
    # Read the contents of the file
    with open('paragraphs.txt', 'r') as file:
        text = file.read()

    # Remove stop words
    processed_text = remove_stop_words(text)

    # Count word frequency
    word_frequency = count_word_frequency(processed_text)

    # Print word frequency
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")

if __name__ == "__main__":
    main()
