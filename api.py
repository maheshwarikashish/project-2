from flask import Flask, jsonify
from scorer import analyze_text, score_ideas

app = Flask(__name__)

@app.route('/api/ideas', methods=['GET'])
def get_ideas():
    scraped_data_file = "scraped_data.txt"
    common_keywords = analyze_text(scraped_data_file)
    ranked_ideas = score_ideas(common_keywords)
    return jsonify(ranked_ideas)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
