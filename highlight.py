#!/usr/bin/python
# -*- coding: utf-8 -*-
import re


def highlightDoc(doc, query):
    """
    Select to display the most relevant snippet that contains all query words.
    Highlight all query words in the snippet. 
    
    Args:
        doc - String that is a document to be highlighted
        query - String that contains the search query
    
    Returns:
        The most relevant snippet with the query terms highlighted.
    """
    
    # We walk through doc and find the minimum snippet that contains all
    # query words. In general, we consider the minimum snippet the most
    # relevant one because it usually carries what the writer trying to say
    
    # convert doc into a list of words
    words = re.findall(r'\w+', doc)
    
    # init a queue of words that represent the current snippet
    sequence = list(words[0])
    
    # init start(inclusive) and end(exclusive) indexes of the min snippet
    start, end = 0, 1
    
    # total word count of doc, only compute once
    word_count = len(words)
    
    # init the minimum word count as total word count
    min = word_count
    
    # the start and end index of the min snippet queue, in a tuple
    snippet = (start, end)
    
    # find the smallest snippet because they tend to be the most relevant
    # complexity O(2n) where n is the number of words in doc
    while end < word_count:
        # move on to find next snippet if query matches the current snippet
        if inSnippet(sequence, query) and start < end:
            # maintian the first min sequence of words because usually 
            # earlier snippet tends to be more relevant
            if len(sequence) < min:
                min = len(sequence)
                # assign snippet as the result queue indexes
                snippet = (start, end)
            sequence.pop(0)
            start += 1
        # enqueue the next word to snippet
        else:
            sequence.append(words[end])
            end += 1
    
    
    # find minimal sentence(s) that contains the shortest snippet
    sentence = findSentence(doc, snippet)
    
    # highlight the query words in our sentence
    result = highlightSentence(sentence, query)
    
    return result
    
    
def inSnippet(sequence, query):
    """
    Check if all words in query are presented in a list of words
    
    Args:
        sequence - a list of words
        query - strings to match the sequence, assuming they are separated by 
                whitespaces
        
    Returns:
        True if all the words in the query string match the strings in sequence,
        case insensitive. False otherwise
    """
    text = (' ').join(sequence)
    terms = query.split()    
    match = True
    
    # O(m) where is m is number of words in query
    for term in terms:
        pattern = '(^|\s+)%s(\s+|$)' % term
        if not re.search(pattern, text, re.I):
            match = False
    return match
    
    
def findSentence(doc, snippet):
    """
    Find minimal sentences that contains words given their start and end index.
    
    Args:
        doc - the document for scanning
        snippet - tuple containing the start and end indexes of some words
    
    Returns:
        Minimal sentence(s) that contains words given their start and end index
    """
    
    # build a list to keep track of the start and end indexes of each sentence
    pattern = re.compile(r'([^\s][^\.!?]*[\.!?])', re.M)
    sentences = pattern.finditer(doc)
    sent_indexes = [sentence.span() for sentence in sentences]
    
    # build a list to keep track of the start and end indexes of each word
    words_match = re.finditer(r'[^\s]+(?=\s*)', doc)
    word_indexes = [word.span() for word in words_match]
    
    # start and end index of current sentence
    start, end = 0, 0
    
    # finds the minimum sentence or sentences that contains the snippet
    # complexity is O(n'), where n' is number of sentences in doc
    while end < len(sent_indexes):
        # if the beginning of snippet is after the end of a sentence, move
        # to next sentence
        if word_indexes[snippet[0]][0] >= sent_indexes[end][1]:
            start += 1
            end += 1
        # if the snippet is within one sentence, return
        elif word_indexes[snippet[0]][0] >= sent_indexes[start][0] and \
            word_indexes[snippet[1]][1] <= sent_indexes[end][1]:
            return doc[sent_indexes[start][0]:sent_indexes[end][1]]
        # if the beginning of snippet is larger than start of a sentence, 
        # and end of the snippet is larger than the end of the sentence,
        # expand end to next sentence
        elif word_indexes[snippet[0]][0] < sent_indexes[start][1] and \
            word_indexes[snippet[1]][1] > sent_indexes[end][1]:
            end += 1
        else:
            pass
    
    return doc[sent_indexes[start][0]:sent_indexes[end][1]]

def highlightSentence(sentence, query):
    """
    Wrap [[HIGHLIGHT]] and [[ENDHIGHLIGH]] tags around query strings
    in a sentence.
    
    Args:
        sentence - sentence to be highlighted
        query - string that contains the words to be highlighted
    
    Returns:
        sentence after wrapping highlight tags around given queries
    """
    # change query string to a|b|c where a, b, c are query words
    terms = re.sub('\s+', '|', query)
    regex = re.compile(r'(\s*)((?:\b\s*(?:%s)\b)+)' % terms, re.I)
    return regex.sub(r'\1[[HIGHLIGHT]]\2[[ENDHIGHLIGHT]]', sentence)


if __name__ == "__main__":
    # Overall complexity is approximately O(2n * m) + O(n')
    # where n is number of words in the documentm and m is number of words in
    # query string. n' is number of sentences in document. m is close to a
    # constant in a search, and 2 can be ignored as a constant. We can also drop O(n').
    # Therefore, the overall complexity is O(n)
    
    print highlightDoc("I like fish. Little star's deep dish pizza sure is fantastic. \
Dogs are funny.", "deep dish pizza")
    