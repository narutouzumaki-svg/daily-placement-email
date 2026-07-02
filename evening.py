from question_selector import get_today_questions
from email_sender import send_email


questions = get_today_questions()


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

<h1 style="color:#16a34a;">
📚 Today's Solutions
</h1>

<p>
Here are the detailed solutions for today's practice questions.
</p>

<hr>

"""

for i, q in enumerate(questions, start=1):

    html += f"""

<h2>Question {i}</h2>

<p><b>Topic:</b> {q["topic"]}</p>

<p><b>Difficulty:</b> {q["difficulty"]}</p>

<p style="font-size:18px;">
{q["question"]}
</p>

"""

    if q["options"]:

        html += "<ol type='A'>"

        for option in q["options"]:
            html += f"<li>{option}</li>"

        html += "</ol>"

    html += f"""

<p style="color:green;">
<b>✅ Correct Answer:</b><br>
{q["answer"]}
</p>

<p>
<b>💡 Solution</b><br>
{q["solution"]}
</p>

<hr>

"""

html += """

<p>

Hope you solved them yourself before checking the answers!

See you tomorrow for another set of questions. 🚀

</p>

</div>

</body>

</html>

"""


send_email(
    "📚 Today's Placement Solutions",
    html
)