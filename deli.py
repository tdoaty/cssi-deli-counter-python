katz_deli = []
#1. line() function
def line():
    i = 0 +1
    if len(katz_deli) >= 1
        print "The line is currently:" katz_deli
    else:
    if len(katz_deli) ==0
    print "The line is currently empty."
    return line

#2. take_a_number function
def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print "Welcome, " name ". You are number" katz_deli " in line."
    return take_a_number

#3. now_serving() function
def now_serving(katz_deli):
    katz_deli.pop()
    print "Currently serving" katz_deli
    if len(katz_deli) == 0
        print "There is nobody waiting to be served!"
    return now_serving
    
