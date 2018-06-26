def updateIncome(user,type,amount):
    if type in ['f','o']: #fixed income or other
        user.cash += amount
        user.save()


    if type=='i': # interests
        # TODO: need to automate this by if this type auto list the list of interest
        user.cash += amount
        user.save()

    if type =='b': # borrow
        # TODO: need to subtract in the total asset
        user.cash += amount
        user.save()

def updateExpense(user,type,amount):
    user.cash -= amount
    user.save()
