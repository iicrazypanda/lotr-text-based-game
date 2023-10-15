# from tkinter import Tk, Frame, Label, Button
#
# # Load questions from the "avontuur1.txt" file
# questions = []
# with open("avontuur1.txt", "r") as avontuur1:
#     for line in avontuur1:
#         data = line.strip().split(";")
#         if len(data) >= 4:
#             avontuur_dict = {
#                 "Vraag": data[1],
#                 "Antwoord 1": data[2],
#                 "Antwoord 2": data[3]
#             }
#             questions.append(avontuur_dict)
#
# # Initialize current_question
# current_question = 0
#
#
# def toon_keuze_moment(venster):
#     global current_question
#     if current_question < len(questions):
#         for widget in venster.winfo_children():
#             widget.destroy()
#
#         frame_verhaal = Frame(venster)
#         frame_verhaal.grid(row=1, column=0, padx=2)
#
#         label_verhaal = Label(frame_verhaal, text=questions[current_question]["Vraag"])
#         label_verhaal.pack()
#
#         frame_keuze_1 = Frame(venster)
#         frame_keuze_1.grid(row=1, column=2, padx=3, pady=50)
#
#         button_keuze_1 = Button(frame_keuze_1, text=questions[current_question]["Antwoord 1"],
#                                 command=lambda: next_question(venster, 1))
#         button_keuze_1.pack()
#
#         frame_keuze_2 = Frame(venster)
#         frame_keuze_2.grid(row=2, column=2, padx=3, pady=50)
#
#         button_keuze_2 = Button(frame_keuze_2, text=questions[current_question]["Antwoord 2"],
#                                 command=lambda: next_question(venster, 2))
#         button_keuze_2.pack()
#     else:
#         einde_dict = maak_einde_dict_1()
#         for widget in venster.winfo_children():
#             widget.destroy()
#         label_einde = Label(venster, text=einde_dict["goed_einde"])
#         label_einde.pack()
#
#
# def next_question(venster, choice):
#     global current_question
#     if choice == 1:
#         print(f"You chose {questions[current_question]['Antwoord 1']}")
#     else:
#         print(f"You chose {questions[current_question]['Antwoord 2']}")
#
#     current_question += 1
#     toon_keuze_moment(venster)
#
#
# root = Tk()
# root.geometry("2000x2000")
# toon_keuze_moment(root)
#
# root.mainloop()
