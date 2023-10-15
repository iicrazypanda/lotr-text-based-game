from tkinter import Label, Frame, Button

questions = []
current_question = 0

def start_adventure(root):
    label_frame = Frame(root)

    welcome_label = Label(label_frame, text="Welcome to The Journey in the Shire")
    welcome_label.grid(row=0, column=0, columnspan=2)

    start_button = Button(label_frame, text="Start Adventure", command=lambda: show_question(root, current_question))
    start_button.grid(row=1, column=0, columnspan=2)

    label_frame.grid()

def show_question(root, question_num):
    label_frame = Frame(root)
    question_label = Label(label_frame, text=questions[question_num]["Question"])
    question_label.grid(row=0, column=0, columnspan=2)

    answer1_button = Button(label_frame, text=questions[question_num]["Choice1"],
                            command=lambda: show_next_question(root, question_num, 1))
    answer1_button.grid(row=1, column=0)

    answer2_button = Button(label_frame, text=questions[question_num]["Choice2"],
                            command=lambda: show_next_question(root, question_num, 2))
    answer2_button.grid(row=1, column=1)

    label_frame.grid()

def show_next_question(root, question_num, choice):
    if choice == 1:
        print(f"You chose: {questions[question_num]['Choice1']}")
    else:
        print(f"You chose: {questions[question_num]['Choice2']}")

    global current_question
    if current_question < len(questions) - 1:
        current_question += 1
        show_question(root, current_question)
    else:
        print("End of the adventure!")

def initialize_adventure(root, adventure_data):
    for line in adventure_data:
        data = line.strip().split(";")
        expected_data_length = 4
        if len(data) >= expected_data_length:
            adventure_dict = {
                "Number": data[0],
                "Question": data[1],
                "Choice1": data[2],
                "Choice2": data[3]
            }

            questions.append(adventure_dict)

    start_adventure(root)











# from tkinter import Tk, Label, Frame, Button
#
# questions = []
# current_question = 0
#
# def start_adventure(root):
#     label_frame = Frame(root)
#
#     welcome_label = Label(label_frame, text="Welcome to The Journey in the Shire")
#     welcome_label.grid(row=0, column=0, columnspan=2)
#
#     start_button = Button(label_frame, text="Start Adventure", command=lambda: show_question(current_question))
#     start_button.grid(row=1, column=0, columnspan=2)
#
#     label_frame.grid()
#
# def show_question(question_num):
#     label_frame = Frame(root)
#     question_label = Label(label_frame, text=questions[question_num]["Question"])
#     question_label.grid(row=0, column=0, columnspan=2)
#
#     answer1_button = Button(label_frame, text=questions[question_num]["Choice1"],
#                             command=lambda: show_next_question(question_num, 1))
#     answer1_button.grid(row=1, column=0)
#
#     answer2_button = Button(label_frame, text=questions[question_num]["Choice2"],
#                             command=lambda: show_next_question(question_num, 2))
#     answer2_button.grid(row=1, column=1)
#
#     label_frame.grid()
#
# def show_next_question(question_num, choice):
#     if choice == 1:
#         print(f"You chose: {questions[question_num]['Choice1']}")
#     else:
#         print(f"You chose: {questions[question_num]['Choice2']}")
#
#     global current_question
#     if current_question < len(questions) - 1:
#         current_question += 1
#         show_question(current_question)
#     else:
#         print("End of the adventure!")
#
# def main():
#     global root
#     root = Tk()
#     root.geometry("800x600")
#     root.title("Journey in the Shire")
#
#     start_adventure(root)
#     root.mainloop()
#
# if __name__ == '__main__':
#     with open("avontuur1.txt", "r") as adventure_file:
#         for line in adventure_file:
#             data = line.strip().split(";")
#             expected_data_length = 4
#             if len(data) >= expected_data_length:
#                 adventure_dict = {
#                     "Number": data[0],
#                     "Question": data[1],
#                     "Choice1": data[2],
#                     "Choice2": data[3]
#                 }
#
#                 questions.append(adventure_dict)
#     main()
