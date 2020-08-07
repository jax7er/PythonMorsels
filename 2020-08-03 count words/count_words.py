def count_words(s: str) -> dict:
'''counts the number of occurrances of individual words in a string, case insensitive
    s: string to count the number of occurances of each word in
    returns: dictionary containing words as keys and numbers of occurances as values
'''
lower = s.lower()
no_punc = lower.translate(str.maketrans("", "", string.punctuation))
unique_words = set(map(str.strip, no_punc.split()))

return {word: no_punc.count(word) for word in unique_words}