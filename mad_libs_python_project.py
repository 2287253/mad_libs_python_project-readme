import random

def get_word(prompt, word_type):
    """Get a word from the user with validation."""
    while True:
        word = input(f"Enter a {word_type}: ").strip()
        if word:
            return word
        print(f"Please enter a valid {word_type}!")

def mad_libs():
    """Main function to run the Mad Libs game."""
    print("\nWelcome to Mad Libs!")
    print("You'll be asked to enter different types of words to create a funny story.")
    print("Let's begin!\n")

    # Story templates
    stories = [
        """One day, a {adjective} {noun} decided to {verb} to the {place}. 
Along the way, they met a {adjective2} {animal} who was {verb_ing} {adverb}. 
Together, they {verb2} all the way to the {place2} and had a {adjective3} time!""",

        """The {adjective} {noun} was {verb_ing} in the {place} when suddenly, 
a {adjective2} {animal} appeared and started {verb_ing2} {adverb}. 
Everyone was {adjective3} and started {verb2} as fast as they could!""",

        """Once upon a time, there was a {adjective} {noun} who loved to {verb} 
in the {place}. One day, they found a {adjective2} {animal} who was {verb_ing} 
{adverb}. They became best friends and lived {adjective3} ever after!"""
    ]

    # Select a random story
    story = random.choice(stories)

    # Get words from the user
    words = {
        "adjective": get_word("an adjective", "adjective"),
        "noun": get_word("a noun", "noun"),
        "verb": get_word("a verb", "verb"),
        "place": get_word("a place", "place"),
        "adjective2": get_word("another adjective", "adjective"),
        "animal": get_word("an animal", "animal"),
        "verb_ing": get_word("a verb ending in -ing", "verb"),
        "adverb": get_word("an adverb", "adverb"),
        "verb2": get_word("another verb", "verb"),
        "place2": get_word("another place", "place"),
        "adjective3": get_word("one more adjective", "adjective"),
        "verb_ing2": get_word("another verb ending in -ing", "verb")
    }

    # Fill in the story
    final_story = story.format(**words)

    # Display the result
    print("\nHere's your Mad Libs story:\n")
    print(final_story)
    print("\nThanks for playing!")

if __name__ == "__main__":
    while True:
        mad_libs()
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Goodbye!")
            break
