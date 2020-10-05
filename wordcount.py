from sys import argv

def count_words(filename):
    """Prints the number of shared words in a text file.
    
    Usage: python3 wordcount.py <textfile.txt>
    """

    # Open the file
    file_data = open(filename)

    word_dict = {}

    punctuations = [".", ",", "?", "_", "&", ":", ";", "!", "--", "*", "[", "]"]

    for line in file_data:
        # Tokenize data
        tokenized_list = line.strip().split(" ")

        # Lowercase all the letters
        tokenized_list = [word.lower() for word in tokenized_list]

        # Strip away all punctuation
        for word in tokenized_list:
            for letter in word:
                if letter in punctuations:
                    tokenized_list[tokenized_list.index(word)] = tokenized_list[tokenized_list.index(word)].strip(letter)

        # Go over each word in list and add them to the word_dict with count
        for word in tokenized_list:
            word_dict[word] = word_dict.get(word, 0) + 1 

    for key, value in word_dict.items():
        print(key, value)

    file_data.close()

count_words(argv[1])
