from flask import Flask

app = Flask(__name__)
port = 8080

if __name__ == '__main__':
    print(f"im listening at {port}")
    app.run(port=port)
