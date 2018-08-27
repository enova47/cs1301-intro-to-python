# Write a function called get_grade that will read a
# given .cs1301 file and return the student's grade.
# To do this, we would recommend you first pass the
# filename to your previously-written reader() function,
# then use the list that it returns to do your
# calculations. You may assume the file is well-formed.
#
# A student's grade should be 100 times the sum of each
# individual assignment's grade divided by its total,
# multiplied by its weight. So, if the .cs1301 just had
# these two lines:
#
# 1 exam_1 80 100 0.6
# 2 exam_2 30 50 0.4
#
# Then the result would be 72:
#
# (80 / 100) * 0.6 + (30 / 50) * 0.4 = 0.72 * 100 = 72


# Write your function here!
def get_grade(filename):
    outputFile = open(filename, "r")
    outputFile = outputFile.readlines()
    listTest = []
    for line in outputFile:
        line = line.strip("\n")
        splitLine = line.split(" ")
        listTest.append(splitLine)
    for item in listTest:
        for i in range(len(item)):
            item[0] = int(item[0])
            item[2] = int(item[2])
            item[3] = int(item[3])
            item[4] = float(item[4])
    sumItem = []
    for item in listTest:
        sumItem.append(100 * ((item[2] / item[3]) * item[4]))
    return sum(sumItem)

    outputFile.close()


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 91.55
print(get_grade("sample.cs1301"))
