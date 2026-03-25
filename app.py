from flask import Flask

app = Flask(__name__)


@app.route('/')
def my_profile():
    return {
        "name": "홍길동",
        "role": "초보 서버 개발자",
        "status": "로컬 환경 통제 완료!",
        "skills": ["Ubuntu", "VS Code", "Python", "Flask"]
    }

if __name__ == '__main__':
    app.run(debug=True)