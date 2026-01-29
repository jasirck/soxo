positive_words = ["good","great","happy",'love',"excellent",'awesome']
negative_words = ["bad",'terrblr','sad','hate','poor','worst']
unwanted = ['!','@','#','$','%','^','&','*','(',')','.',',','/']

#Task 3 rule based sentiment analyzer ,find good sentence or bad sentence

input_sentence = input(str('Enter the sentence\n'))
sentence_split = input_sentence.split(' ')
positive = 0
negative = 0
for i in sentence_split:
    split_word = [x for x in i ]
    for x in split_word:
        if x in unwanted:
            split_word.remove(x)
    new_word = ''.join(split_word)
    if new_word in positive_words:
        positive += 1
    elif new_word in negative_words:
        negative += 1
print("Sentiment : ",('Positive' if (positive-negative) > 0 else  ('Negative' if (positive-negative) < 0 else "Neutral" )))


# Test Sentence

# i love this product, it's absolutely awesome!

# This is the worst experience ever, i hate it.

# The product is okay, not good but not bad either.

# Service was good, but delivery was poor.