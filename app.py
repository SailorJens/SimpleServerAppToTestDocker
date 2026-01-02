from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Adder</title>
<h1>Add two numbers</h1>
<form method="post">
  Number 1: <input type="number" name="num1"><br>
  Number 2: <input type="number" name="num2"><br>
  <input type="submit" value="Add">
</form>
{% if result is not none %}
  <h2>Result: {{ result }}</h2>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            result = num1 + num2
        except ValueError:
            result = "Invalid input"
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
