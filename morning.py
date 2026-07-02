from question_selector import (
    select_two_questions,
    record_sent_questions,
)

from email_sender import send_email


questions = select_two_questions()


html = """
<html>

<body style="font-family:Arial;background:#f5f5f5;padding:30px;">

<div style="
max-width:750px;
background:white;
margin:auto;
padding:30px;
border-radius:12px;
box-shadow:0px 0px 12px rgba(0,0,0,0.12);
">

<h1 style="color:#2563eb;">
📚 Daily Placement Practice
</h1>

<p>
Good morning!
</p>

<p>
Here are today's two practice questions.
</p>

<hr>

"""

for i, q in enumerate(questions, start=1):

    html += f"""

<h2 style="color:#1f2937;">
Question {i}
</h2>

<p>
<b>📖 Topic:</b> {q["topic"]}
</p>

<p>
<b>⭐ Difficulty:</b> {q["difficulty"]}
</p>

<p>
<b>⏱ Estimated Time:</b> {q["estimated_time_minutes"]} minute(s)
</p>

<p style="font-size:18px;">
{q["question"]}
</p>

"""

    if q["options"]:

        html += "<ol type='A'>"

        for option in q["options"]:
            html += f"<li>{option}</li>"

        html += "</ol>"

    html += "<hr>"

html += """

<p>

<b>🚫 Don't peek!</b>

The detailed solutions will arrive in your evening email.

</p>

<p>

Good luck with today's practice! 🚀

</p>

</div>

</body>

</html>

"""

# Send the email
send_email(
    "📚 Daily Placement Practice",
    html
)

# Only mark questions as used if the email was sent successfully
record_sent_questions(questions)