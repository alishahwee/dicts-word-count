from sys import argv

def count_words(filename):
    """Prints the number of shared words in a text file."""

    # Open the file
    file_data = open(filename)

    word_dict = {}

    for line in file_data:
        # Tokenize data
        tokenized_list = line.strip().split(" ")

        # Go over each word in list and add them to the word_dict with count
        for word in tokenized_list:
            word_dict[word] = word_dict.get(word, 0) + 1 

    for key, value in word_dict.items():
        print(key, value)

    file_data.close()

count_words(argv[1])
