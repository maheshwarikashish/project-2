import pandas as pd
from collections import Counter

def analyze_text(file_path):
    """
    Reads text from a file, analyzes the frequency of words, and
    returns a list of the most common keywords (excluding common stop words).
    """
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Simple word tokenization and normalization (lowercase)
    words = text.lower().split()

    # Basic stop word list (you can expand this)
    stop_words = set(["the", "and", "a", "is", "to", "in", "of", "it", "that", "for", "on", "with", "as", "by", "i", "you", "he", "she", "they", "we", "be", "at", "this", "from", "or", "but", "was", "are", "an"])

    # Filter out stop words
    keywords = [word for word in words if word.isalpha() and word not in stop_words]

    # Count word frequencies
    word_counts = Counter(keywords)

    # Return the 20 most common keywords
    return word_counts.most_common(20)

if __name__ == "__main__":
    scraped_data_file = "scraped_data.txt"
    common_keywords = analyze_text(scraped_data_file)
    
    print("Most common keywords:")
    for keyword, count in common_keywords:
        print(f"- {keyword}: {count}")
