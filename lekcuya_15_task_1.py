from validate_email import validate_email

dataset = ['Valid Email '] = dataset['Email'].appy(lambda x:validate_email(x))
dataset['Verified Email'] = dataset['Email'].appy(lambda x:validate_email(x, verify = True))