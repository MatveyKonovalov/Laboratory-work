def main():
    words = input("Введите строку: ").split()
    words.sort()
    print(f"Количество слов: {len(words)}")
    print(f"Слова в алфавитном порядке: {words}")
    uniqueWords = sorted(set(words))
    print(f"Уникальные слова: {uniqueWords}")
    print("Частота слов:")
    wordsCounter = {}
    for word in words:
        wordsCounter[word] = wordsCounter.get(word, 0) + 1
    for word in sorted(wordsCounter.keys()):
        print(f"{word}: {wordsCounter[word]}")

if __name__ == "__main__":
    main()


