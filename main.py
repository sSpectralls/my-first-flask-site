from flask import Flask, render_template, request

# Create a flask app
app = Flask(__name__, template_folder='templates', static_folder='static')


# Index page (now using the index.html file)
@app.route('/')
def index():
  Memes19 = ['Stonks', 'Me and the bois', 'Ultra Instinct', 'Big Chungus']
  Memes20 = [ 'Among us', 'Always has', 'Woo yeah', 'Polish cow']
  return render_template('index.html', Memes19 = Memes19, Memes20 = Memes20)

@app.route('/2019')
def Memes2019():
    return render_template('memes-2019.html')

@app.route('/2020')
def memes2020():
  return render_template('memes-2020.html')

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', debug=True, port=8080)

@app.route('/Question-Data', methods=['POST'])
def bericht_verwerken():
  Meme = request.form['Meme']
  
  return render_template('Question-Data.html', 
                         Memes = Meme)