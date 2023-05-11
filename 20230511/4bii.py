def getName(first, surname, isTeacher):
    if isTeacher:
        return surname[-3:] + first[:2]
    else:
        return first[:3] + surname[:2]
