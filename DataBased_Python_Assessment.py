# Hello World! Thanks for exploring the opportunity to join us at DataBased.
# We wish you the best with the assessment.
# Please complete and come prepared to present your solutions to the team.

# Instructions: Solve the problems listed below.
# There are more details about the problems in the provided README, we highly
# recommend reading through the README before solving the problems.

# In order to run the program install Python if not already installed.
# Then change your current directory to the same as the file
# Run the command `python DataBased_Python_Assessment.py` or `python3 DataBased_Python_Assessment.py`
# If you see 'PASSED' that means you passed the all test cases in the test function,
# it does not mean your solution is 100% correct. There may be edge cases you
# should add tests for on your own!

# PROBLEM 1 - Least Factorial
# Given an integer n, find the minimal k such that
# k = m! (where m! = 1 * 2 * ... * m) for some integer m; k ≥n. In other
# words, find the smallest factorial which is not less than n.

def leastFactorial(n):
    # TODO: Solve problem 1 here
    i = 1

    # testing from the smallest factorial to the biggest until finding the solution
    factorial = i
    i = i + 1
    while factorial < n:
        factorial = factorial * i
        i = i + 1

    return factorial

def testLeastFactorial():
    print('-' * 20)
    print('Part 1: Least Factorial')

    assert leastFactorial(17) == 24
    assert leastFactorial(5) == 6
    # TODO: add your own test cases here
    assert leastFactorial(1) == 1
    assert leastFactorial(120) == 120

    print('PASSED PROBLEM 1!')

# PROBLEM 2 - Reclying Lipstick
# You own a lipstick business. When a lipstick container is empty, there is actu-
# ally some leftover lipstick at the bottom that cannot be used because it is not
# accessible. Being an environmentally friendly business owner, you would like to
# recycle the leftover lipstick to make more. As a business, you know you need
# ‘numberOfLeftoversNeeded‘ to make a new lipstick. You have ‘numberOfLip-
# sticks‘ in your possession. What’s the total number of lipsticks you can sell
# assuming that each of your customers return their leftovers

def getTotalNumberOfLipsticks(numberOfLipsticks, numberOfLeftoversNeeded):
    if numberOfLeftoversNeeded < 0:
        return None
    # there would be infinite number of lip sticks in this case. However, this is not realistic. 
    # Thus, the precondition should be that numberOfLeftoverNeeded must be greater than 0. 
    # We should raise an error here. 
    if numberOfLeftoversNeeded == 0:
        return "inf"

    # TODO: Solve problem 2 here
    sticks_sold = numberOfLipsticks
    leftover = numberOfLipsticks
    while leftover >= numberOfLeftoversNeeded:
        new_sticks = leftover // numberOfLeftoversNeeded
        unused_leftover = leftover % numberOfLeftoversNeeded

        sticks_sold = sticks_sold + new_sticks
        leftover = new_sticks + unused_leftover
    #print(sticks_sold)
    return sticks_sold

def testLipsticks():
    print('\n'+ '-' * 20)
    print('Part 2: Lipsticks')
    assert getTotalNumberOfLipsticks(5, 2) == 9
    assert getTotalNumberOfLipsticks(15, 5) == 18
    assert getTotalNumberOfLipsticks(2, 3) == 2
    # TODO: add your own test cases here
    assert getTotalNumberOfLipsticks(0, 2) == 0
    assert getTotalNumberOfLipsticks(10, 0) == "inf"
    assert getTotalNumberOfLipsticks(10, -1) == None

    print('PASSED PROBLEM 2!')

# PROBLEM 3 - Students and Treats
# A school teacher wants to hand out treats to his students. The teacher de-
# cides the best way to divide the treats is to have the students sit in a circle of
# sequentially numbered chairs. A chair number will be drawn from a hat. Begin-
# ning with the student in drawn chair, one treat will be handed to each student
# sequentially going around the circle until all treats have been distributed.
# The teacher wants to have the students involved in sharing treats. He decides
# that whoever gets the very last treat, will be the student who makes the treats
# for the next game. Determine the chair number occupied by the student who
# will receive the last treat.

# For example, there are 4 students and 6 treats. The students arrange them-
# selves in seats numbered 1 to 4. Let’s suppose 2 is drawn from the hat. Students
# receive treats at positions 2,3,4,1,2,3. The student who gets the last treat is in
# chair number 3

def getLastStudent(numberOfStudents, treats, startingChair):
    # TODO: Solve problem 3 here
    non_cyclic_treats = (treats-1) % numberOfStudents
    #
    result = (startingChair-1 + non_cyclic_treats) % numberOfStudents + 1
    #print(result)
    return result

def testLastStudent():
        print('\n'+ '-' * 20)
        print('Part 3: Students and Treats')
        assert getLastStudent(5,2,1) == 2
        assert getLastStudent(5,2,2) == 3
        assert getLastStudent(7,19,2) == 6
        assert getLastStudent(3,7,3) == 3

        # TODO add your own test cases here
        # boundary cases
        assert getLastStudent(10**9, 10**9, 10**9 // 2) == 10**9//2 - 1
        assert getLastStudent(10**9, 10**9, 1) == 10**9
        assert getLastStudent(10**9, 10**9, 10**9) == 10**9-1
        #
        assert getLastStudent(1, 10**9, 1) == 1
        #
        assert getLastStudent(10**9, 1, 2) == 2
        assert getLastStudent(10**9, 1, 1) == 1
        assert getLastStudent(10**9, 1, 10**9) == 10**9
        #
        assert getLastStudent(1, 1, 1) == 1

        # normal case
        assert getLastStudent(11, 31, 6) == 3


        print('PASSED PROBLEM 3!')

def getPairsOfShoes(listOfShoes):
    # TODO: Solve problem 4 here
    unique_shoes_count = {}
    for shoes in listOfShoes:
        if shoes not in unique_shoes_count:
            unique_shoes_count[shoes] = 1
        else:
            unique_shoes_count[shoes] = unique_shoes_count[shoes] + 1
    
    result = 0
    for shoes in unique_shoes_count.keys():
        result = result + unique_shoes_count[shoes] // 2

    return result

# PROBLEM 4 - Pairs of Shoes
# Given an array of strings that represent a type of shoe, return how many matching
# pairs of shoes can be made?

def testPairsOfShoes():
    print('\n'+ '-' * 20)
    print('Part 4: Pairs of Shoes')
    assert getPairsOfShoes(["red", "blue", "red", "green", "green", "red"]) == 2
    assert getPairsOfShoes(["green", "blue", "blue", "blue", "blue", "blue", "green"]) == 3
    # TODO: Add your own test cases here
    assert getPairsOfShoes([]) == 0
    assert getPairsOfShoes(["blue", "green", "black"]) == 0
    assert getPairsOfShoes(["blue", "green", "green"]) == 1
    assert getPairsOfShoes(["blue", "green", "black", "blue", "blue", "green"]) == 2
    assert getPairsOfShoes(["green", "green", "green", "green", "green", "green"]) == 3

    print('PASSED PROBLEM 4!')
    print('\n\nCongratulations!!')

# Call test functions
testLeastFactorial()
testLipsticks()
testLastStudent()
testPairsOfShoes()
