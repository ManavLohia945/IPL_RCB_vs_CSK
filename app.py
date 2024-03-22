from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Initialize CORS extension with default options


# Step 4: Define endpoint to generate best 11 players
@app.route('/generate-best-11-players')
def generate_best_11_players():
    # Your prediction code here
    # This is where you would include the code for generating the best 11 players

    # Sample predicted players list
    # predicted_players = [
    #     "MS Dhoni", "Ambati Rayudu", "Hardik Pandya", "Moeen Ali",
    #     "Ravindra Jadeja", "Mohit Sharma", "Rashid Khan", "Deepak Chahar"
    # ]

    # Return the predicted list of players as a JSON response
    return jsonify({'players': predicted_players_list})

if __name__ == '__main__':
    app.run(debug=True)
