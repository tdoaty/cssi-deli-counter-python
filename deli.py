katz_
    if len(katz_deli) == 0
        print "There is nobody waiting to be served!"
    return now_serving


katz_deli = []
def line():
    i = 0 +1
    if len(katz_deli)>= 1
        print "The line is currently: " + katz_deli
    else:
    if len(katz_deli) == 0
        print "The line is currently empty."
    return line

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
