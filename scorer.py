import random
from collections import Counter

def analyze_text(file_path):
    """
    Reads text from a file, analyzes the frequency of words, and
    returns a list of the most common keywords (excluding common stop words).
    """
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    words = text.lower().split()
    stop_words = set(["the", "and", "a", "is", "to", "in", "of", "it", "that", "for", "on", "with", "as", "by", "i", "you", "he", "she", "they", "we", "be", "at", "this", "from", "or", "but", "was", "are", "an"])
    keywords = [word for word in words if word.isalpha() and word not in stop_words]
    word_counts = Counter(keywords)
    return word_counts.most_common(20)

def score_ideas(keywords):
    """
    Takes a list of keywords and assigns a simulated demand and competition score.
    Returns a sorted list of ideas with their scores.
    """
    scored_ideas = []
    for keyword, frequency in keywords:
        # Simulate demand (e.g., based on frequency) and competition (random)
        demand_score = frequency * 10  # Higher frequency suggests higher interest
        competition_score = random.randint(1, 100)
        
        # Calculate opportunity score
        opportunity_score = demand_score - competition_score
        
        scored_ideas.append({
            "idea": keyword,
            "demand": demand_score,
            "competition": competition_score,
            "opportunity_score": opportunity_score
        })
    
    # Sort ideas by the highest opportunity score
    return sorted(scored_ideas, key=lambda x: x["opportunity_score"], reverse=True)

if __name__ == "__main__":
    scraped_data_file = "scraped_data.txt"
    common_keywords = analyze_text(scraped_data_file)
    
    ranked_ideas = score_ideas(common_keywords)
    
    print("Ranked Software Ideas (Based on Opportunity Score):")
    print("-----------------------------------------------------")
    for idea in ranked_ideas:
        print(f"- Idea: {idea['idea']}\n  Opportunity Score: {idea['opportunity_score']}")
