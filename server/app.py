from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import random
from backEnd import *
from main import *




app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Define a simple route
@app.route('/')
def hello():
    return 'Hello, World!'

# Define another route
@app.route('/api/data')
def get_data():
    data = {'message': 'This is some data from the server!'}
    return jsonify(data)

@app.route('/api/multiply', methods=['POST'])
def multiply_value():
    data = request.get_json()
    value = data.get('value')
    multiplied_value = value * 10
    return jsonify({'result': multiplied_value})


@app.route('/api/minmax', methods=['POST'])
def min_max():
    data = request.get_json()
    slider_values = data.get('value')

    # Extract min and max values from the slider
    slider_min, slider_max = slider_values
    
    # call a function main using slider_min and slider_min
    
    
    # Generate a list of integers between slider_min and slider_max (inclusive)
    result = list(range(slider_min, slider_max + 1))

    # Convert the list of integers to a comma-separated string
    result_string = ', '.join(str(num) for num in result)

    return jsonify({'result': result_string})


# test main.py
@app.route('/api/test', methods=['POST'])
def get_min_songs_handler():
    min_songs = get_min_Songs()  # Call get_min_Songs() from main.py
    return jsonify({'min_songs': min_songs})

@app.route('/api/singleint', methods=['POST'])
def get_specific_songs_handler():
    data = request.get_json()
    bpm = data.get('value')  
    specific_songs = get_specific_Songs(bpm) #get_specific_Songs() main.py function
    print('specific_songs:', specific_songs)
    return jsonify({'specific_songs': specific_songs})



@app.route('/api/singledemo', methods=['POST'])
def single_demo_handler():
    data = request.get_json()
    bpm = data.get('bpm')
    demo_songs = get_specific_Songs(bpm)  # main.py call

    if demo_songs:  # Check if demo_songs is not empty
        random_song = random.choice(demo_songs)
        artist = random_song['artist']
        title = random_song['name']
        return jsonify({'specific_songs': [{'artist': artist, 'title': title}]})  # Return a list containing the artist and title of the randomly selected song
    else:
        print(f"No songs found for BPM: {bpm}")
        return jsonify({'specific_songs': demo_songs})
    
    
@app.route('/api/pairint', methods=['POST'])
def get_range_Songs_handler():
    data = request.get_json()
    slider_values = data.get('value')
    slider_min, slider_max = slider_values
    range_songs = get_range_Songs(slider_min, slider_max)
    print('Range Songs:', range_songs)  # Add this line to log the range_songs
    return jsonify({'range_songs': range_songs})


@app.route('/api/pairint-descending', methods=['POST'])
def pair_int_descending_handler():
    data = request.get_json()
    start = data.get('start')
    end = data.get('end')
    range_songs_descending = get_range_songs_descending(start, end)
    print('range_songs_descending:', range_songs_descending)  
    return jsonify({'range_songs_descending': range_songs_descending})




if __name__ == '__main__':
    main()
    app.run(debug=True)
