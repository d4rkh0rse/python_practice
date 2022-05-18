import re
import random

user_data = {}
user_acc_num = []
# get username


def user_info():
    user_first_name = input('Enter your first name: ')
    # user_last_name = input('Enter your Last name: ')
    return user_first_name

# generate user password


def user_pass_create():
    print('password requirements \nminimum 8 charactor \nmaximum 16 charactor \none uppercase \none special charactor')
    # confirm_password = input('enter password again')
    pass_chek_patt = '^[A-Za-z0-9@#$%^&+=]{8,16}$'
    while True:
        user_password = input('create your password: ')
        pass_check = re.findall(pass_chek_patt, user_password)

        if pass_check:
            print('Your password is strong')
            final_pass = pass_check
            return final_pass
            # break
        else:
            print('Your password is weak')
            continue

# for saving account


def saving_account():
    # user_info()
    # user_pass_create()
    dict_name = user_info()
    dict_pass = user_pass_create()
    user_data.update({dict_name: dict_pass})
    account_number = acc_number()
    print(
        f'Your account name is {dict_name}\nyour account number is {account_number}')

    # user_data.update({user_info: user_pass_create})


# for current account
def current_account():
    # user_info()
    # user_pass_create()

    while True:
        gst_num = input('Enter your gst number: ').upper()

        if len(gst_num) == 15:
            print('gst match.....')
            # print(gst_num)
            final_gst = gst_num
            dict_name = user_info()
            dict_pass = user_pass_create()
            user_data.update({dict_name: dict_pass})
            break

        else:
            print('wrong GST number')
            continue


def acc_number():
    middle = random.randint(1000, 9999)
    end_num = random.randint(1000, 9999)
    # print(end_num)
    account_number = '000010'+str(middle) + str(end_num)
    # temp_list = []
    # return account_number

    if account_number not in user_acc_num:
        user_acc_num.append(acc_number)
    else:
        # continue
    # temp_list.append(x)
    # print(account_number, end='')

    # if x in temp_list:
    #     print('yes')
    # print(x)
        pass

while True:
    user_in = int(input(
        '1. New Account \n2. Deposit Amount \n3. Withdraw Ammount \n4. Balance Inquiry \nEnter between (1-8): '))
    if user_in == 1:
        account_type = input(
            'which type of account you want to open [saving/current]: ')

        if account_type[0].upper() == 'S':
            print('saving account selected.')
            saving_account()
            print('please store your password secretly.')

        elif account_type[0].upper() == 'C':
            print('current account selected.')
            current_account()
            print('please store your password secretly.')
    break

# print(user_data)
