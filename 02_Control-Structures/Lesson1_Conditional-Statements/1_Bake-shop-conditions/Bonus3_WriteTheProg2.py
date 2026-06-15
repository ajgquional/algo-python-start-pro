allergic = input('Have an allergy: ')
allergy = input('Allergic to: ')
allergic = allergic.lower()
allergy = allergy.lower()
is_allergic = allergic == 'yes' or allergic == 'have'
suggestion = allergy != 'milk' and allergy != 'gluten'
print('Allergies:', is_allergic)
print('Offer cheesecakes:', suggestion)