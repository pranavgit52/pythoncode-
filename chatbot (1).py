import random

# Course data
courses = {
    "Python": {"price": 49, "description": "Learn Python from scratch."},
    "Web Development": {"price": 59, "description": "Master HTML, CSS, and JavaScript."},
    "Data Science": {"price": 79, "description": "Become a data expert with Python & ML."},
}

# Predefined chatbot responses
responses = {
    "greeting": ["Hello! Welcome to our course platform.", "Hi there! Looking for a course?"],
    "menu": ["We offer the following courses:\n" + "\n".join(f"- {course}" for course in courses)],
    "buy": ["Great choice! Visit our website to enroll.", "You can purchase this course on our website."],
    "exit": ["Goodbye! Happy learning.", "See you soon! Keep learning."]
}

# Chatbot function
def chatbot():
    print(random.choice(responses["greeting"]))
    while True:
        user_input = input("You: ").strip().lower()
        
        if "courses" in user_input or "menu" in user_input:  # Fixed the menu issue
            print("Bot:", responses["menu"][0])
        elif any(course.lower() in user_input for course in courses):
            course_name = next(course for course in courses if course.lower() in user_input)
            print(f"Bot: {course_name} - ${courses[course_name]['price']} | {courses[course_name]['description']}")
        elif "buy" in user_input or "purchase" in user_input:
            print("Bot:", random.choice(responses["buy"]))
        elif "exit" in user_input or "bye" in user_input:
            print("Bot:", random.choice(responses["exit"]))
            break
        else:
            print("Bot: I'm here to help! Ask me about our courses.")

# Run the chatbot
chatbot()

