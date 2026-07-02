import json
import random

QUESTION_BANK = "question_bank.json"
USED_FILE = "used_questions.json"
TODAY_FILE = "today_questions.json"


def load_question_bank():
    with open(QUESTION_BANK, "r", encoding="utf-8") as file:
        return json.load(file)


def load_used_questions():
    with open(USED_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_used_questions(data):
    with open(USED_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def save_today_questions(question_ids):
    with open(TODAY_FILE, "w", encoding="utf-8") as file:
        json.dump(
            {
                "today_questions": question_ids
            },
            file,
            indent=4
        )


def load_today_questions():
    with open(TODAY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)["today_questions"]


def select_two_questions():

    question_bank = load_question_bank()

    used = load_used_questions()["used_questions"]

    unused = [q for q in question_bank if q["id"] not in used]

    if len(unused) < 2:
        print("Question bank exhausted. Resetting...")

        used = []
        save_used_questions({"used_questions": []})

        unused = question_bank

    return random.sample(unused, 2)


def record_sent_questions(selected_questions):

    used = load_used_questions()["used_questions"]

    ids = [q["id"] for q in selected_questions]

    used.extend(ids)

    save_used_questions(
        {
            "used_questions": used
        }
    )

    save_today_questions(ids)


def get_today_questions():

    question_bank = load_question_bank()

    lookup = {
        q["id"]: q
        for q in question_bank
    }

    ids = load_today_questions()

    return [
        lookup[i]
        for i in ids
    ]