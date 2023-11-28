from flask import Flask, render_template,flash
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = 'your_secret_key'  # 设置一个安全密钥

@app.route('/')
def index():
    print("***********************")
    return render_template('layout.html')

@app.route('/abc')
def bootswatch():
    print("1234567890")
    flash(app.config['BOOTSTRAP_BOOTSWATCH_THEME'])
    if app.config['BOOTSTRAP_BOOTSWATCH_THEME'] == 'litera':
        app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'morph'
    else:
        app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'litera'
    return render_template('layout.html')

if __name__ == '__main__':
    app.run(debug=True)
