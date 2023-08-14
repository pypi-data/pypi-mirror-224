import datetime


def calculate_movable_holidays(year):
    e = 10
    if year > 1600:
        year2 = year // 100
        e = 10 + year2 - 16 - (year2 - 16) // 4
    if year < 1583:
        e = 0

    a = year % 19
    b = (19 * a + 15) % 30
    c = (year + year // 4 + b) % 7
    L = b - c
    p = L + e
    day = 1 + (p + 27 + (p + 6) // 40) % 31
    month = 3 + (p + 26) // 30 - 1

    pascha = datetime.date(year, month, day)
    kathara_deftera = pascha - datetime.timedelta(days=48)
    meg_paraskevi = pascha - datetime.timedelta(days=2)
    deft_pascha = pascha + datetime.timedelta(days=1)
    agiou_pnefmatos = pascha + datetime.timedelta(days=50)

    return [
        {"date": kathara_deftera, "name": "Καθαρά Δευτέρα"},
        {"date": meg_paraskevi, "name": "Μεγάλη Παρασκευή"},
        {"date": deft_pascha, "name": "Δευτέρα του Πάσχα"},
        {"date": agiou_pnefmatos, "name": "Αγίου Πνεύματος"},
    ]


def greek_holidays(year):
    fixed_holidays = [
        {"date": datetime.date(year, 1, 1), "name": "Πρωτοχρονιά"},
        {"date": datetime.date(year, 1, 6), "name": "Θεοφάνεια"},
        {"date": datetime.date(year, 3, 25), "name": "Ευαγγελισμός της Θεοτόκου"},
        {"date": datetime.date(year, 5, 1), "name": "Εργατική Πρωτομαγιά"},
        {"date": datetime.date(year, 8, 15), "name": "Κοίμηση της Θεοτόκου"},
        {"date": datetime.date(year, 10, 28), "name": "Ημέρα του Όχι"},
        {"date": datetime.date(year, 12, 25), "name": "Χριστούγεννα"},
        {"date": datetime.date(year, 12, 26), "name": "Επόμενη των Χριστουγέννων"},
    ]

    movable_holidays = calculate_movable_holidays(year)

    all_holidays = fixed_holidays + movable_holidays
    all_holidays.sort(key=lambda x: x[0])

    return all_holidays
