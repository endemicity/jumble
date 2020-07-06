from logic.solution import answers

if __name__ == "__main__":
    words = answers("a", words_file="test")
    for word in words:
        print(word)
