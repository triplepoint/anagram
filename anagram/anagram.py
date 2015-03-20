from collections import defaultdict


def put_word_in_anagram_dictionary(word, anagram_sets):
    """
    Given a word and a dictionary of lists of anagrams, find
    the appropriate list and add the word to it.
    """
    # Sort the word's characters, to get a hash that
    # all its anagrams would share, and append the word
    # to the appropriate list of anagrams.
    index = ''.join(sorted(word))
    anagram_sets[index].append(word)


def get_anagrams_from_file(file_path, min_word_length=1):
    """
    for each word in the given file, sort it into the dictionary
    of lists of anagrams.  Optionally, only consider words longer than
    the given minimum word length.
    """
    anagram_sets = defaultdict(list)
    with open(file_path) as dictionary_file:
        for word in dictionary_file:
            clean_word = word.strip().lower()
            if len(clean_word) >= min_word_length:
                put_word_in_anagram_dictionary(clean_word, anagram_sets)
    return anagram_sets


def main():
    """
    Display the anagram sets from the system dictionary for which the anagram
    count is equal to or larger than the lengths of the words in the set.
    Limit the word length to 4 characters or greater.
    """
    anagram_sets = get_anagrams_from_file("/usr/share/dict/words", 4)
    for index, anagram_set in anagram_sets.items():
        if len(anagram_set) >= len(index):
            anagram_set.sort()
            print ", ".join(anagram_set)


if __name__ == "__main__":
    main()
