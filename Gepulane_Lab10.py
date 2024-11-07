gradeList = []
counter = 1
passed = 0
total = 0

while True:
    grades = input(f"Student Grade {counter}: ")
    if grades == "done":
        break
    elif not grades.isdecimal():
        print("Must be a number")
        continue
    else:
        if int(grades) > 39 and int(grades) < 101:
            gradeList.append(grades)
            counter +=1
            if int(grades) >= 75:
                passed +=1
        else:
            print("Grade is not valid")
            break

for num in gradeList:
    total += int(num)

if len(gradeList) != 0:
    print("Average Grade:", round(total/len(gradeList), 2))
    print("Passed:", passed)
    print(f"Passing %: {passed/len(gradeList) * 100}%")
    print("Grades:",gradeList)