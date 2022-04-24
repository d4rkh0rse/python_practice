
contact_dict = {}

total_num_save = int(input('How many contact you want to save: '))


for num in range(total_num_save):
    name_in = input('enter name of contact:')
    number_in = int(input(f'enter mobile number of {name_in}: '))

    contact_dict.update({name_in:number_in})

    print(contact_dict)            
    search_name = input('enter the name to search')

    if search_name in contact_dict:
        print('Name:' + search_name)
        print('Number:'+ str(contact_dict[search_name]))
    else:
        print('no contact found')
