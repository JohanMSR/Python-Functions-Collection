def reverse_string(text: str) -> str:
    """Reverse a string."""
    return text[::-1]

def count_vowels(text: str) -> int:
    """Count the number of vowels in a string."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word in a string."""
    return ' '.join(word.capitalize() for word in text.split()) 