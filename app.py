from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def home():
    try:
        return render_template("index.html")
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == "__main__":
    app.run(debug=True)