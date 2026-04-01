from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    my_profile = {
        "name": "이정학",
        "age": 18,
        "school": "종로산업정보학교",
        "hobby": "게임",
        "email": "qhfxm704@gmail.com",
        "phone": "010-8687-3510",
        "dream": "개발자",
    }
    return render_template('index.html', data=my_profile)

if __name__ == '__main__':
    app.run(debug=True)