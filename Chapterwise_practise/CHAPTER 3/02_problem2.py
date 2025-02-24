name=input("Enter your name:")
date=input("Enter todays date:")
letter='''
    DEAR {name}
    You are Selected.
    {date}'''
print(letter.format(name=name,date=date))