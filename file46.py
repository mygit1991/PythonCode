A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character ('\n') to insert a blank line between each word-meaning pair in your output.

glossary = {
    'array': 'Arrays a kind of data structure that can store a fixed-size sequential collection of elements of the same type.',
    'function': 'A function is a group of statements that together perform a task.',
    'pointer': 'Pointers in C are easy and fun to learn.',
    'loop': 'Work through a collection of items, one at a time.',
    'union': "A union is a special data type available in C that allows to store different data types in the same memory location.",
    }

word = 'array'
print(f"\n{word.title()}: {glossary[word]}")

word = 'function'
print(f"\n{word.title()}: {glossary[word]}")

word = 'pointer'
print(f"\n{word.title()}: {glossary[word]}")

word = 'loop'
print(f"\n{word.title()}: {glossary[word]}")

word = 'union'
print(f"\n{word.title()}: {glossary[word]}")