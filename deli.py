katz_deli = []
def line(katz_deli):
    deli_list_string = "The line is currently:"
    for i in range(0,len(katz_deli)):
        deli_list_string += " " + str(i+1) + ". " list_of_customers[i]
    if len(katz_deli) == 0
        return "The line is currently empty."
    return deli_list_string

def take_a_number(katz_deli, new_customer):
    katz_deli.append(new_custoemr)
    return "Welcome, " + new_customer+ ". You are number " + str(len(katz_deli)) + "in line."

def now_serving(katz_deli):
    if len(katz_deli) == 0
        return "There is nobody waiting to be served."
    current_customer = katz_deli.pop(0)
    return "Currently serving " + current_customer + "."
