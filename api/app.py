from flask import Flask, render_template,flash,redirect
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = 'your_secret_key'  # 设置一个安全密钥
app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'default'


@app.route('/')
def index():
    flash("主题："+app.config['BOOTSTRAP_BOOTSWATCH_THEME'])
    return render_template('layout.html')

@app.route('/abc')
def bootswatch():
    theme_list=['default', 'cerulean', 'cosmo', 'cyborg', 'darkly', 'flatly', 'journal', 'litera', 'lumen', 'lux', 'materia', 'minty', 'morph', 'pulse', 'quartz', 'sandstone', 'simplex', 'sketchy', 'slate', 'solar', 'spacelab', 'superhero', 'united', 'vapor', 'yeti', 'zephyr']
    theme_now=app.config['BOOTSTRAP_BOOTSWATCH_THEME']
    try:
        app.config['BOOTSTRAP_BOOTSWATCH_THEME']=theme_list[theme_list.index(theme_now)+1]
    except IndexError:
        app.config['BOOTSTRAP_BOOTSWATCH_THEME']='default'
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
