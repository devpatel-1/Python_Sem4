# Original tuple of subject marks
marks = (85, 78, 90, 72)   # Python, Java, SQL, HTML

print("Original Tuple:", marks)

# 1. Convert tuple to list
marks_list = list(marks)

# 2. Add two new subjects marks
marks_list.append(88)   # New subject 1
marks_list.append(80)   # New subject 2

# 3. Remove lowest mark
lowest = marks_list[0]
for m in marks_list:
    if m < lowest:
        lowest = m

marks_list.remove(lowest)

# 4. Convert back to tuple
final_marks = tuple(marks_list)

print("Final Tuple:", final_marks)