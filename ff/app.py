from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/ff.html')

def index():
    num_rows = 6  # Replace with the desired number of rows
    num_gifs = 5  # Replace with the desired number of GIFs per row
    return render_template('ff.html', num_gifs=num_gifs, num_rows=num_rows)

@app.route('/low-angle.html')
def low_angle():
    num_rows = 6  # Replace with the desired number of rows
    num_gifs = 5  # Replace with the desired number of GIFs per row
    return render_template('low-angle.html', num_gifs=num_gifs, num_rows=num_rows)


if __name__ == '__main__':
    app.run()
