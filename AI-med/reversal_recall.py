from flask import Flask, request, render_template_string
import pandas as pd
import random

cheer_msgs = [
    "Keep going, you’re close!",
    "Not quite, but don’t give up!",
    "Hmm… that one fooled a lot of people.",
    "Try again, you’ve got this!",
    "That’s not it, but you're narrowing it down."
]

app = Flask(__name__)
df = pd.read_csv("reversal_recall.csv")

@app.route("/recall", methods=["GET", "POST"])
def reversal_recall():
    message = ""
    if request.method == "POST":
        try:
            index = int(request.form.get("index", -1))
            row = df.iloc[index]
            if index == 169 and row['message'].strip() == "You have been selected for a limited access beta program!":
                message = "🎉 Flag: CIR{M4573R_0F_R3V3R53D_CL45S1F1C4710N}"
            else:
                message = random.choice(cheer_msgs)
        except:
            message = "⚠️ Invalid input. Please enter a valid index."

    preview_html = df.head(10).to_html(classes='table', index=True)

    return render_template_string('''
        <html>
        <head>
            <title>Reversal Recall</title>
            <style>
                body { font-family: Arial; padding: 30px; }
                .table { border-collapse: collapse; margin-top: 20px; }
                .table th, .table td { border: 1px solid #ccc; padding: 8px; }
                .table th { background: #f0f0f0; }
            </style>
        </head>
        <body>
            <h2>🔍 Reversal Recall</h2>
            <p>A machine learning intern accidentally reversed the predictions. One of these messages is real spam... and hides a flag.</p>
            <p>Submit the index of the message you think was originally spam (but predicted as ham).</p>
            <form method="POST">
                <input type="number" name="index" placeholder="Row index" required>
                <input type="submit" value="Submit">
            </form>
            <div style="margin-top:20px;">{{ flag }}</div>
            <hr>
            <h4>Preview (first 10 rows):</h4>
            {{ preview|safe }}
        </body>
        </html>
    ''', flag=message, preview=preview_html)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)