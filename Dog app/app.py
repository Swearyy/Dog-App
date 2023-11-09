from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Sample dog data
dogs = {
    "whiskey": {
        "name": "Whiskey",
        "breed": "Golden Retriever",
        "description": "Whiskey is a friendly and energetic Golden Retriever.",
    },
    "cocoa": {
        "name": "Cocoa",
        "breed": "Labrador Retriever",
        "description": "Cocoa is a playful and loyal Labrador Retriever.",
    },
    "buddy": {
        "name": "Buddy",
        "breed": "German Shepherd",
        "description": "Buddy is an intelligent and protective German Shepherd.",
    }
}

# Routes
@app.route('/')
@app.route('/dogs')
def dogs_home():
    return render_template('index.html', dogs=dogs)

@app.route('/dogs/<dog_name>')
def dog_profile(dog_name):
    dog = dogs.get(dog_name)
    if dog:
        return render_template('dog.html', dog=dog)
    else:
        return redirect(url_for('dogs_home'))

if __name__ == '__main__':
    app.run(debug=True)
