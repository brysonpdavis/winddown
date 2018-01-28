from flask import Flask, render_template

app = Flask(__name__)
app.config['PURECSS_RESPONSIVE_GRIDS'] = True
app.config['PURECSS_USE_CDN'] = True
app.config['PURECSS_USE_MINIFIED'] = True
Pure(app)

@app.route('/')
def hello():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(debug=True)
