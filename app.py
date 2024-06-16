from flask import Flask, render_template, url_for, request, redirect, session, flash

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/value')
def value():
    return render_template('value.html', title='値の受け渡し', content='ここに内容')

@app.route('/value/<title>/<content>')
def value_query(title, content):
    return render_template('value.html', title=title, content=content)

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/form', methods=['GET'])
def form_get():
    return render_template('form.html', content='ここの文章が変わるよ')

@app.route('/form', methods=['POST'])
def form_post():
    text_input = request.form['t']
    return render_template('form.html', content=f'「{text_input}」が入力されたよ')

@app.route('/statement', methods=['GET'])
def statement_get():
    return render_template('statement.html')

@app.route('/statement', methods=['POST'])
def statement_post():
    post = True
    n = 10
    data = ["data0", "data1", "data2", "data3", "data4"]
    return render_template('statement.html', number=n, data=data, post=post)

@app.route('/flash', methods=['GET'])
def flash_get():
    return render_template('flash.html')

@app.route('/flash', methods=['POST'])
def flash_post():
    
    # 入力値受け取り
    t = request.form['t']
    n = request.form['n']
    
    # Flashの設定
    input_flg = True
    
    if not t:
        flash("テキストを入力してください")
        input_flg = False
        
    if not n:
        flash("数字を入力してください")
        input_flg = False
        
    if not input_flg:
        return redirect(url_for("flash_get"))
    
    post = True
    
    return render_template('flash.html', text=t, number=int(n), post=post)

if __name__ == '__main__':
    app.run(debug=True)