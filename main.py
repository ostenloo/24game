"""
This function was shamelessly stolen from https://www.youtube.com/shorts/PNc_Ju3u-OE
I did modify it by adding the operations
"""

def solve(nums): 
    if(len(nums) <= 1): 
        return [[nums[0], ""]] 
    else: 
        for idx in range(1,len(nums)): 
            left = solve(nums[:idx])
            right = solve(nums[idx:]) 
            values = []
            for l in left: 
                for r in right: 
                    lval = l[0]
                    rval = r[0]
                    lop = l[1]
                    rop = r[1]
                    values.append([lval + rval, lop + "+" + rop])
                    values.append([lval - rval, lop + "-" + rop])
                    values.append([lval * rval, lop + "*" + rop])
                    if(rval != 0):
                        values.append([lval / rval, lop + "/" + rop])
        
        return values 

# idx = 0

def createSolutionFile(): 
    with open(f"solution241.txt", "w") as f: 
        for target in range(24,25): 
            for num1 in range(1,10): 
                for num2 in range(1,10):  
                    for num3 in range(1,10):  
                        for num4 in range(1,10):  
                            values = solve([num1,num2,num3,num4])
                            for value in values: 
                                if value[0] - 0.01 < target and value[0] + 0.01 > target: 
                                    if num1 == 9 and num2 == 1 and num3 == 9 and num4 == 6: 
                                    # idx += 1
                                    # f.write(str(idx) + ". " + str(num1) + value[1][0:1] + str(num2) + value[1][1:2] + str(num3) + value[1][2:3] + str(num4) + " = " + str(target) + "\n")
                                        f.write(str(num1)+value[1][0:1]+str(num2)+value[1][1:2]+str(num3)+value[1][2:3]+str(num4)+"\n")
                                        # f.write(str(num1)+str(num2)+str(num3)+str(num4)+"\n")
    f.close() 

def getSolutions(): 
    solutions = dict()

    with open("solution24.txt", "r") as f: 
        lines = f.readlines() 
        for line in lines: 
            num1 = int(line[0])
            num2 = int(line[2])
            num3 = int(line[4])
            num4 = int(line[6])
            key = frozenset({num1,num2,num3,num4})
            if key not in solutions.keys():
                solutions[key] = {line.strip()}
            else: 
                solutions[key].add(line.strip())

    return solutions

def computer(difficulty, answered):
    global computerAnswered 
    while not answered.is_set():
        start = time.time() 
        if difficulty == 1:
            wait = random.randint(45,60)
        elif difficulty == 2:
            wait = random.randint(30,45)
        elif difficulty == 3:
            wait = random.randint(15,30)
        elif difficulty == 4: 
            wait = random.randint(5,15) 
        for i in np.arange(0, wait, 0.1): 
            if answered.is_set():
                break
            time.sleep(0.1)
        if not answered.is_set():
            computerAnswered = True
            answered.set() 
        end = time.time()
        # print(f"Computer thread took {end - start} seconds to terminate.")
    return 

def player(answered):
    global playerAnswered 
    global playerAnswer
    while not answered.is_set():
        start = time.time() 
        rlist, _, _ = select.select([sys.stdin], [], [], 1)
        if rlist:
            attempt = input().strip()
            if attempt: 
                playerAnswered = True 
                playerAnswer = attempt 
                answered.set() 
        if answered.is_set():
            end = time.time() 
            # print(f"Player thread took {end - start} seconds to terminate.")
            break
    return

if __name__ == "__main__": 
    # run this once to create the solution file
    # createSolutionFile()

    import random
    import time 
    import threading
    import select
    import sys 
    import numpy as np 

    playerAnswered = False 
    computerAnswered = False

    print("Welcome to 24 game! Choose if you want to play against yourself or the computer. Type 1 for yourself, 2 for the computer: ")

    choice = int(input().strip())

    solutions = getSolutions() 

    continueGame = 1

    playerAnswer = None

    if choice == 1: 
        print("Great! You're playing against yourself.")
        score = 0 
        while continueGame == 1:
            playerAnswer = None 
            nums = [random.randint(1,9) for i in range(4)]
            key = frozenset({nums[0],nums[1],nums[2],nums[3]})
            print(f"Your numbers are: {nums[0]} {nums[1]} {nums[2]} {nums[3]}") 
            print("Type in your solution like this: 1+2*3-4. You can use +, -, *, and /. You can also rearrange the order of the numbers. If you don't think there's a possible solution, type NA")
            playerAnswer = input().strip()
            if key not in solutions.keys():  
                if playerAnswer == "NA": 
                    print("Correct!")
                    score += 1
                    print(f'Your score is {score}')
                    print("Would you like to continue? Type 1 for yes, 2 for no")
                    continueGame = int(input().strip())
                else:
                    print("Incorrect. There are no possible solutions.")
                    print(f'Your score is {score}')
                    print("Would you like to continue? Type 1 for yes, 2 for no")
                    continueGame = int(input().strip())
            else: 
                if playerAnswer in solutions[key]:
                    print("Correct!")
                    score += 1
                    print(f'Your score is {score}')
                    print("Would you like to continue? Type 1 for yes, 2 for no")
                    continueGame = int(input().strip())  
                else: 
                    print("Incorrect. One correct solution is: ")
                    print(next(iter(solutions[key])))
                    print(f'Your score is {score}')
                    print("Would you like to continue? Type 1 for yes, 2 for no")
                    continueGame = int(input().strip())

    elif choice == 2: 
        score = 0 
        computerScore = 0 
        answered = threading.Event()
        print("Great! You're playing against the computer. Choose your level of difficulty. Type 1 for easy, 2 for medium, 3 for hard, and 4 for insane.")
        difficulty = int(input().strip()) 
        while continueGame == 1: 
            answered.clear()
            computerAnswered = False
            playerAnswered = False
            playerAnswer = None 
            nums = [random.randint(1,9) for i in range(4)]
            key = frozenset({nums[0],nums[1],nums[2],nums[3]})
            print(f"Your numbers are: {nums[0]} {nums[1]} {nums[2]} {nums[3]}") 
            print("Type in your solution like this: 1+2*3-4. You can use +, -, *, and /. You can also rearrange the order of the numbers. If you don't think there's a possible solution, type NA")
            t1 = threading.Thread(target = computer, args = (difficulty, answered))
            t2 = threading.Thread(target = player, args = (answered,)) 
            t1.start() 
            t2.start()  
            t1.join()
            t2.join()
            if computerAnswered:
                computerScore += 1
                print("\nGah! The Computer figured it out before you did.")
                if key in solutions.keys(): 
                    print("One correct solution is: ")
                    print(next(iter(solutions[key])))
                else: 
                    print("There are no possible solutions, so NA was the correct answer.")
                print(f'Your score is {score}')
                print(f'The computer\'s score is {computerScore}')
                print("Would you like to continue? Type 1 for yes, 2 for no")
                continueGame = int(input().strip()[-1]) 
            elif playerAnswered: 
                if key not in solutions.keys():
                    if playerAnswer == "NA":
                        print("\nCorrect! There are no possible solutions.")
                        score += 1
                        print(f'Your score is {score}')
                        print(f'The computer\'s score is {computerScore}')
                        print("Would you like to continue? Type 1 for yes, 2 for no")
                        continueGame = int(input().strip())
                    else: 
                        computerScore += 1
                        print("\nIncorrect. There are no possible solutions, so NA was the correct answer. ")
                        print(f'Your score is {score}')
                        print(f'The computer\'s score is {computerScore}')
                        print("Would you like to continue? Type 1 for yes, 2 for no")
                        continueGame = int(input().strip())
                else: 
                    if playerAnswer in solutions[key]: 
                        print("\nCorrect!")
                        score += 1
                        print(f'Your score is {score}')
                        print(f'The computer\'s score is {computerScore}')
                        print("Would you like to continue? Type 1 for yes, 2 for no")
                        continueGame = int(input().strip())
                    else: 
                        computerScore += 1 
                        print("\nIncorrect. One correct solution is: ")
                        print(next(iter(solutions[key])))
                        print(f'Your score is {score}')
                        print(f'The computer\'s score is {computerScore}')
                        print("Would you like to continue? Type 1 for yes, 2 for no")
                        continueGame = int(input().strip())