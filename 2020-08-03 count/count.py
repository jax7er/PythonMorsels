
def count_words(s: str) -> dict:
    '''counts the number of occurrances of individual words in a string, case insensitive
        s: string to count the number of occurances of each word in
        returns: dictionary containing words as keys and numbers of occurances as values
    '''
    lower = s.lower()

    all_words = []
    for word in lower.split():
        start_i = 0
        while not word[start_i].isalpha():
            start_i += 1
            
        end_i = len(word) - 1
        while not word[end_i].isalpha():
            end_i -= 1
        
        all_words.append(word[start_i:(end_i + 1)])
    
    unique_words = set(all_words)

    return {
        word: all_words.count(word)
        for word 
        in unique_words
    }
