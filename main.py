from question_selector import get_two_questions


questions = get_two_questions()

print("\nToday's Questions\n")

for i, question in enumerate(questions, start=1):

    print("=" * 60)

    print(f"Question {i}")

    print()

    print(question["question"])

    print()

    if question["options"]:

        for option in question["options"]:
            print(option)

    print()

    print("Correct Answer:")
    print(question["answer"])

    print()

    print("Solution:")
    print(question["solution"])

    print()