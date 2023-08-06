def reverse(word):
    if len(word) == 1:
        return word
    else:
        return reverse( word[len(word)-1]) + reverse(word[:len(word)-1])


word_input = input("Enter a String to check it is palindrome or not")
reverse_word = reverse(word_input)
if word_input.casefold() == reverse_word.casefold():
    print("Palindrome")
else:
    print("Not palindrome")