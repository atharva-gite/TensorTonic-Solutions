def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    word_dict={}
    for sentence in sentences:
        for word in sentence:
            word_dict[word]=word_dict.get(word,0)+1
    return word_dict