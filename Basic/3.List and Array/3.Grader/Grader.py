report_card = {
    "Alice Johnson": {
        "Math": 85,
        "Science": 90,
        "English": 88,
        "History": 78,
        "Programming": 92,
        "Average": 86.6,
        "Letter" : "A+"
    },
    "Bob Smith": {
        "Math": 79,
        "Science": 82,
        "English": 74,
        "History": 85,
        "Programming": 80,
        "Average": 80.0,
        "Letter" : "A+"
    },
    "Catherine Lee": {
        "Math": 92,
        "Science": 89,
        "English": 91,
        "History": 87,
        "Programming": 95,
        "Average": 90.8,
        "Letter": "A+"
    },
    "David Brown": {
        "Math": 68,
        "Science": 72,
        "English": 75,
        "History": 70,
        "Programming": 65,
        "Average": 70.0,
        "Letter": "A"
    },
    "Eva Martinez": {
        "Math": 88,
        "Science": 85,
        "English": 87,
        "History": 84,
        "Programming": 90,
        "Average": 86.8,
        "Letter": "A+"
    },
    "Franklin Harris": {
        "Math": 95,
        "Science": 93,
        "English": 96,
        "History": 89,
        "Programming": 94,
        "Average": 93.4,
        "Letter": "A+"
    },
    "Grace Patel": {
        "Math": 78,
        "Science": 80,
        "English": 82,
        "History": 76,
        "Programming": 79,
        "Average": 79.0,
        "Letter": "A"
    },
}


def display_grades():
    for learner,grades in report_card.items():
        print(f"{learner}'s Report Card")
        for subject, grade in grades.items():
            print(f"{subject}: {grade}")


def main():
    pass


if __name__ == '__main__':
    main()