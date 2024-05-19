from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

uploaded_files = []


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/products')
def products():
    with open('your_file.txt', 'r') as file:
        lines = file.readlines()
    first_words = [line.split()[0] for line in lines]
    return render_template('products.html', first_words=first_words, lines=lines)


@app.route('/line/<int:index>')
def show_line(index):
    with open('your_file.txt', 'r') as file:
        lines = file.readlines()
    line = lines[index - 1]
    first_word = line.split()[0]
    return render_template('line.html', line=line, image_url=url_for('static', filename=f'images/{first_word}.jpg'))


@app.route('/reviews', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file.save(f'upload_{len(uploaded_files)+1}.txt')
        uploaded_files.append(f'upload_{len(uploaded_files)+1}.txt')
        return redirect(url_for('home'))
    return render_template('reviews.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
