print("People from begining centuare of XXI")

str_age = {}
x = int(input("Introduce please your age : "))

def compare_age(x):

    while x >= 0 and x < 120:
        if x >=0 and x < 7:
            str_age.update({"Kinder garden":x})
            return x
        elif x >= 7 and x < 18:
            str_age.update({'School age': x})
            return x
        elif x >= 18 and x < 25:
            str_age.update({'Profesinal University age': x})
        elif x >= 25 and x < 60:
            str_age.update({'Work age': x})
            return x
        elif x >= 60 and x < 120:
            str_age.update({'Your have a choose': x})
            return x
        elif x < 0 and x > 120:
            str_age.update({"Error! This program for people": x})
            return x




age_check = compare_age(x)
print(str_age)
        
