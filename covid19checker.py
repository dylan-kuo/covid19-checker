import json
import pandas as pd


class Screen:      
    def __init__(self):        
        self.age = ''
        self.covid_contact = False
        self.covid_exposure = False
        self.new_cough = False
        self.fever = False
        self.shortness_breath = False
        self.sore_throat = False
        self.muscle_ache = False
        self.nurse_facility = False
        self.heart_conditions = False
        self.immunocompromised = False    


def load_dialog_data():
    with open('covid19-dialog.JSON') as json_file:
        json_data = json.load(json_file)
    return json_data


def load_testing_facilities_data():
    with open('mass-covid19-testing-sites.JSON') as json_file:
        facilities = json.load(json_file)        
    df = pd.DataFrame(facilities['testing facilities'], columns=['name', 'contact'])  
    
    return df


def start_diagnoser():    
    question_1()


def get_valid_input():
    while True:
        try:
            option = int(input("1-Yes  2-No  3-Not sure   >> "))
            if option == 1 or option == 2 or option == 3:
                return option
        except:
            pass
        print("\nIncorrect input, try again")


def ask_user_to_do_covid_test():
    print("\n" + data["7"]['dialog']) 
    print('\nCOVID-19 Testing Sites in Massachusetts')
    print(df_mass_test_facilities)


def ask_user_to_confinue_monitor():
    print("\n" + data["15"]['dialog'])
    print('\nCOVID-19 Testing Sites in Massachusetts')
    print(df_mass_test_facilities)


def question_1():
    print("\n" + data["1"]["dialog"])
    option = get_valid_input()
    if option == 1:
        print(data["1"]['yes_injection'])
        question_3()
        
    elif option == 2:
        print(data["1"]['no_injection'])
        print("\n" + data["2"]['dialog'])
    
    else:
        print(data["1"]['not_sure_injection'])
        question_3()


def question_3():
    print("\n" + data["3"]["dialog"])
    option = get_valid_input()
    if option == 1:
        screen.age = "60+"
        print(data["3"]['yes_injection'])               
    
    elif option == 2:
        screen.age = "18-60"
        print(data["3"]['no_injection'])        
    
    else:
        screen.age = "60+"
        print(data["3"]['not_sure_injection'])            
        
    question_4()


def question_4():
    print("\n" + data["4"]["dialog"])
    option = get_valid_input()
    if option == 1:
        screen.covid_contact = True
        print(data["4"]['yes_injection'])
    
    elif option == 2:
        screen.covid_contact = False
        print(data["4"]['no_injection'])    
        
    else:
        screen.covid_contact = True
        print(data["4"]['not_sure_injection'])        
    
    question_5()


def question_5():
    print("\n" + data["5"]["dialog"])
    option = get_valid_input()
    if option == 1:
        screen.covid_exposure = True        
        if screen.age == "60+" and screen.covid_exposure is True:
            ask_user_to_do_covid_test()
            
        else:
            print(data["5"]['yes_injection'])
            question_6()                  
    
    elif option == 2:
        screen.covid_exposure = False        
        print(data["5"]['no_injection'])  
        question_6() 
        
    else:
        screen.covid_exposure = True         
        if screen.age == "60+" and screen.covid_exposure is True:
            ask_user_to_do_covid_test()
            
        else:
            print(data["5"]['not_sure_inje1ction'])
            question_6() 


def question_6():
    print("\n" + data["6"]["dialog"])
    option = get_valid_input()    
    if option == 1:
        screen.new_cough = True
        ask_user_to_do_covid_test()
        
    elif option == 2:
        screen.new_cough = False
        question_8()
        
    else:
        screen.new_cough = True
        ask_user_to_do_covid_test()


def question_8():
    print("\n" + data["8"]["dialog"])
    option = get_valid_input()
    if option == 1:
        screen.fever = True
        if screen.new_cough is True and screen.fever is True:
            ask_user_to_do_covid_test()
            
        else:
            question_9()        
        
    elif option == 2:
        screen.fever = False
        question_9()
        
    else:
        screen.fever = True
        if screen.new_cough is True and screen.fever is True:
            ask_user_to_do_covid_test()


def question_9():
    print("\n" + data["9"]["dialog"])
    option = get_valid_input()
    if option == 1:
        screen.shortness_breath = True
        if ((screen.shortness_breath is True and screen.fever is True) or
                (screen.shortness_breath is True and screen.age == "60+")):
            ask_user_to_do_covid_test()
        else:
            question_10()
    
    elif option == 2:
        screen.shortness_breath = False
        question_10()
        
    else:
        screen.shortness_breath = True
        if ((screen.shortness_breath is True and screen.fever is True) or
                (screen.shortness_breath is True and screen.age == "60+")):
            ask_user_to_do_covid_test()
                
        else:
            question_10()


def question_10():
    print("\n" + data["10"]["dialog"])
    option = get_valid_input()   
    if option == 1:
        screen.sore_throat = True
        if screen.sore_throat is True and screen.fever is True:
            ask_user_to_do_covid_test()
        
        else:
            print(data["10"]['yes_injection'])
            question_11()
    
    elif option == 2:
        screen.sore_throat = False
        print(data["10"]['no_injection'])
        question_11()
    
    else:
        screen.sore_throat = True
        if screen.sore_throat is True and screen.fever is True:
            ask_user_to_do_covid_test()
        
        else:
            print(data["10"]['not_sure_injection'])
            question_11()


def question_11():
    print("\n" + data["11"]["dialog"])
    option = get_valid_input()
    if option == 1:
        screen.muscle_ache = True
        if screen.muscle_ache is True and screen.fever is True:
            ask_user_to_do_covid_test()
        
        else:            
            question_12()
    
    elif option == 2:
        screen.muscle_ache = False        
        question_12()
    
    else:
        screen.muscle_ache = True
        if screen.muscle_ache is True and screen.fever is True:
            ask_user_to_do_covid_test()
        
        else:            
            question_12()    


def question_12():
    print("\n" + data["12"]["dialog"])
    option = get_valid_input()
    if option == 1:
        screen.nurse_facility = True
        if (screen.nurse_facility is True and
                (screen.new_cough is True or screen.fever is True or
                 screen.shortness_breath is True or screen.sore_throat is True or screen.muscle_ache is True)):
            ask_user_to_do_covid_test()
        
        else:         
            print(data["12"]['yes_injection'])
            question_13()
    
    elif option == 2:
        screen.nurse_facility = False        
        print(data["12"]['no_injection'])
        question_13()
    
    else:
        screen.muscle_ache = True
        if (screen.nurse_facility is True and
                (screen.new_cough is True or screen.fever is True or
                 screen.shortness_breath is True or screen.sore_throat is True or screen.muscle_ache is True)):
            ask_user_to_do_covid_test()
        
        else:         
            print(data["12"]['not_sure_injection'])
            question_13()   


def question_13():
    print("\n" + data["13"]["dialog"])
    option = get_valid_input()
    if option == 1:
        screen.heart_conditions = True
        if (screen.heart_conditions is True and
                (screen.new_cough is True or screen.fever is True or
                 screen.shortness_breath is True or screen.sore_throat is True or screen.muscle_ache is True)):
            ask_user_to_do_covid_test()
        
        else:            
            question_14()
    
    elif option == 2:
        screen.heart_conditions = False  
        print(data["13"]['no_injection'])
        question_14()
    
    else:
        screen.heart_conditions = True
        if (screen.heart_conditions is True and
                (screen.new_cough is True or screen.fever is True or
                 screen.shortness_breath is True or screen.sore_throat is True or screen.muscle_ache is True)):
            ask_user_to_do_covid_test()
        
        else:            
            question_14()  


def question_14():
    print("\n" + data["14"]["dialog"])
    option = get_valid_input()
    if option == 1:
        screen.immunocompromised = True
        if (screen.immunocompromised is True and
                (screen.new_cough is True or screen.fever is True or
                 screen.shortness_breath is True or screen.sore_throat is True or screen.muscle_ache is True)):
            ask_user_to_do_covid_test()
        
        else:            
            ask_user_to_confinue_monitor()
    
    elif option == 2:
        screen.immunocompromised = False        
        ask_user_to_confinue_monitor()

    else:
        screen.immunocompromised = True
        if (screen.immunocompromised is True and
                (screen.new_cough is True or screen.fever is True or
                 screen.shortness_breath is True or screen.sore_throat is True or screen.muscle_ache is True)):
            ask_user_to_do_covid_test()
        
        else:            
            ask_user_to_confinue_monitor()


if __name__ == '__main__':    
    data = load_dialog_data()
    df_mass_test_facilities = load_testing_facilities_data()
    screen = Screen()
    start_diagnoser()

