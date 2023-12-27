class BookReader:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def get_book_text(self):
        with open(self.path_to_file) as f:
            return f.read()

    def get_book_words(self):
        return len(self.get_book_text().split())

    def character_occurances(self):
        lowcase_text = self.get_book_text().lower()
        characters = {}

        for character in lowcase_text:
            if character in characters:
                characters[character] += 1
            else:
                characters[character] = 1
        
        return characters

    def generate_report(self):
        characters = self.character_occurances()
        words = self.get_book_words()
        sorted_list_characters = []
        for character in characters:
            sorted_list_characters.append({"character": character, "number": characters[character]})
        sorted_list_characters.sort(reverse=True, key=lambda x: x["number"])

        print("\n--- Begin report of books/frankenstein.txt ---")
        print(f"There are this many words: {words}\n\n")
        for character in sorted_list_characters:
            if character["character"].isalpha():
                print(f"The {character['character']} character was found {character['number']} times.")

        print("--- End report ---")
