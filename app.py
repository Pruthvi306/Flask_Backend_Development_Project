from flask import Flask, render_template, request
import re

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])

def home():
    if request.method == "POST":
        test_string = request.form.get("test_string")
        regex_pattern = request.form.get("regex_pattern")
        matched_strings = perform_regex_matching(test_string,regex_pattern)
        return render_template("index.html", matched_strings=matched_strings)
    return render_template("index.html")

def perform_regex_matching(test_string, regex_pattern):
    try:

        matches = re.findall(regex_pattern, test_string)
        
        if not  matches:
            return ['Not Matched']

        return matches
    except re.error as e:
        return []

if __name__ == "__main__":
    app.run(debug=True)


#EMAIL VALIDATION


@app.route("/validate_email", methods=["GET", "POST"])
def validate_email():
    if request.method == "POST":
        email = request.form.get("email")
        is_valid = validate_email_format(email)
        return render_template("validate_email.html", email=email, is_valid=is_valid)
    return render_template("validate_email.html")

def validate_email_format(email):
    email_regex = r'[a-xA-Z0-9_.+-]+@[a-xA-Z0-9-]+\.[a-xA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None
