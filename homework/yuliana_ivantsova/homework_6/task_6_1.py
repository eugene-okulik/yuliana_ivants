text = (
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
    'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
)
words = text.split(' ')
words_with_int = []
for word in words:
    if word.endswith((',', '.')):
        words_with_int.append(word[:-1] + 'ing' + word[-1])
    else:
        words_with_int.append(word + 'ing')

print(' '.join(words_with_int))

