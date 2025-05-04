import time

start_time = time.monotonic()
score = 0
questions_answers = [
    ["In Terraria you can tame a bee as a pet.", "T"],
    ["In Expert mode, bosses have less health than in Normal mode.", "F"],
]

for question, answer in questions_answers:
    if input(f"{question}\nPlease enter T if it is true and F if it is false: ").upper() == answer:
        print("Excellent!")
        score += 1
    else:
        print("Not correct:( Maybe you will be lucky next time!")

end_time = time.monotonic()

print(f"Congratulations! Your total score is: {score}, total time ia {end_time - start_time} seconds.")
