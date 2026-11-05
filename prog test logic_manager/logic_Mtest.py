import pandas as pd

Emergency_Escalation = {
    'category': 'sexual_harassment', 
    'contact_type': 'physical', 
    'stated_effect': 'fear_for_safety',     
    'severity': 2, 
    'confidence': 0.98,     
    'reasoning': 
    "The text describes unwanted physical contact ('hit me on the shoulder and touching me inappropriately') and explicit emotional     impact ('I was really scared from this experience'). Inappropriate physical touching constitutes sexual harassment/physical     assault, which automatically triggers severity 2 under the rubric.", 
}

Manual_Review = {
    'category': 'misc', 
    'contact_type': 'none', 
    'stated_effect': 'none', 
    'severity': 0, 
    'confidence': 0.4, 
    'reasoning': "The user states the driver was 'kind of weird' but explicitly notes 'Not sure what happened exactly.' No specific     instance of harassment, threat, sexual comment, or physical contact is described, and no emotional distress or fear is explicitly     stated. Therefore, contact_type is 'none', stated_effect is 'none', category is 'misc', and severity is 0 under the rubric.", 
}

Default = {    
    'category': 'verbal_harassment', 
    'contact_type': 'verbal', 
    'stated_effect': 'distress', 
    'severity': 1, 
    'confidence': 0.95, 
    'reasoning': 
    'The report describes repeated screaming and shouting by the driver throughout the trip, which constitutes verbal harassment     under POHA Section 3. There was no physical contact reported and no explicit sexual elements or threats of physical violence,     placing it at severity 1 (medium).', 
}

Error = None

def getAi_output(ai_object):                # function to get data from ai output
    category = ai_object["category"]        # variable category contains the category of harrassment from ai output
    severity = ai_object["severity"]        # variable severity contains the severity rating from ai output
    confidence = ai_object["confidence"]    # variable confidence contains the confidence scalefrom ai output
    return category,severity,confidence



def validate_AIoutput(ai_object): # function to validate ai output
    if not isinstance(ai_object, dict) or not ai_object: #if output is not a dictionary or is empty dictionary
        return False
    else:
        return True




def escalation(assess_object): # parse ai output as an input
    if validate_AIoutput(assess_object) == True:
        category, severity, confidence = getAi_output(assess_object)

        emergency_categories = (
        "physical_assault",
        "sexual_harassment",
        "stalking",
        )

        # Initialize both flags to false
        emergency_escalation = False    # boolean value to indicate whether emergency escalation is required
        second_opinion = False          # boolean value to indicate whether second opinion is required

        if severity >= 2 and category in emergency_categories and confidence >= 0.5:
            emergency_escalation = True # boolean
            

        elif confidence < 0.5:
            second_opinion = True # boolean value to indicate whether second opinion is required

        assess_object.update({
        "second_opinion_required" : second_opinion, 
        "immediate_attention_required" : emergency_escalation})
        return assess_object # returns original sample with new flags raised and appended
        
    else:
        return False

result1 = escalation(Emergency_Escalation) # call the function with Emergency_Escalation as input
result2 = escalation(Manual_Review)  # call the function with Manual_Review as input
result3 = escalation(Default)  # call the function with Default as input
result4 = escalation(Error) # call the function with Error as input

def run_test():
    print('=' * 40)
    print('       Test for Logic Manager')
    print('=' * 40)
    print('1. Emergency Escalation')
    print('2. Manual Review')
    print('3. Default')
    print('4. Error (No AI output)')
    print('5. Quit')

    option = int(input('Select Option: '))
    match option:
        case 1:
            print(f'\n{result1}\n')
            run_test()
        case 2:
            print(f'\n{result2}\n')
            run_test()
        case 3:
            print(f'\n{result3}\n')
            run_test()
        case 4:
            print(f'\n{result4}\n')
            run_test()
        case 5:
            print('\nQuitting...')
            return None
        case _:
            print('\nInvalid Option\n')
            return run_test()

run_test()

    


