sentence = input('Enter something:\n')
sentence_changed = sentence.split()
words_with_5_and_more_elem = ""
for i in sentence_changed:
    if len(i) > 4:
        words_with_5_and_more_elem += i+" "
print(f'Your string was: "{sentence}"\n'
      f'Words with 5 or more elements: {words_with_5_and_more_elem}')