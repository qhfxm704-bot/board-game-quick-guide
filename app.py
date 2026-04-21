from flask import Flask, render_template, request, redirect

app = Flask(__name__)
messages = []

@app.route('/')
def home():
    skills = [
        "Python", "HTML", "SQL", "Bash"
    ]
    return render_template('index.html', data=skills, messages=messages)

@app.route('/send', methods=['POST'])
def send():
    skill = request.form.get('skill')
    level = request.form.get('level')
    status = request.form.get('status')

    messages.append(skill + " / " + level + " / " + status)

    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    index = int(request.form['index'])
    messages.pop(index)
    return redirect('/')

@app.route('/delete_all', methods=['post'])
def delete_all():
    messages.clear()
    return redirect('/')

@app.route('/delete_selected', methods=['post'])
def delete_selected():
    indexes = request.form.getlist('delete_indexes')
    
    indexes = [int(index) for index in indexes]
    indexes.sort(reverse=True)

    for index in indexes:
        messages.pop(index)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)