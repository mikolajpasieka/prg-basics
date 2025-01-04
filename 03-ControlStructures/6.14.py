facebook = True
twitter = False
instagram = True
if (facebook and instagram) or (twitter and instagram) or (facebook and twitter) or (facebook and twitter and instagram):
    print('You are a good influencer!')
else:
    print("KEEP TRYING!")
