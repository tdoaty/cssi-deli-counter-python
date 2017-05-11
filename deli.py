katz_deli = []
def line(list_of_customers):
    deli_list_string = "The line is currently: "
    for i in range(0,len(list_of_customers)):
        deli_list_string += stri(i+1) + ". " list_of_customers[i] + " "
    return deli_list_string

def take_a_number(katz_deli, name):
    katz_deli.append(name)
        print "Welcome, " + name + ". You are number" + katz_deli + " in line."
    return take_a_number

def now_serving(katz_deli):
    katz_deli.pop(0)
        print "Currently serving" + katz_deli[0]
    if len(katz_deli) == 0
        print "There is nobody waiting to be served!"
    return now_serving




def take_a_number(arg):

def now_serving():
