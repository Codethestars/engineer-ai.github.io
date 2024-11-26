from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    try:
        return render_template("index.html")
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)