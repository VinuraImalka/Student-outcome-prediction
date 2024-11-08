def largest_word(sentence):
    sentence = sentence.split()
    max_length = 0
    for word in sentence:
        word_length= len(word)
        if max_length < word_length:
            max_length = word_length
            max_length_word = word        
    return max_length_word

sentence = input("Enter a sentence:")
print(f"Largest word is {largest_word(sentence)}.")
