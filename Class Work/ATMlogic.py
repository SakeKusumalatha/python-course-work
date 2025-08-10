data={
    12345:{'pin':123,'balance':5678,'history':[]},
    23456:{'pin':123,'balance':5678,'history':[]},
    34567:{'pin':123,'balance':5678,'history':[]},
    45678:{'pin':123,'balance':5678,'history':[]},
    56789:{'pin':123,'balance':5678,'history':[]},
    91234:{'pin':123,'balance':5678,'history':[]},
    }

def Welcome():
    print('Welcome to ATM'.center(50,'*'))
    
def Menu():
    print('\n[c]heck Balence')
    print('[D]eposit')
    print('[W]ithdraw')
    print('[V]iew Transaction History')
    print('[E]xit\n')

def Login():
    account_number=int(input("Enter the account number: "))
    pin=int(input("Enter the pin: "))
    global acc_num
    if account_number in data:
        if data[account_number]['pin']==pin:
            print("Login Successful")
            acc_num=account_number
            return True
        else:
            print("Invalid pin")
            return False
    else:
        print("Invalid account number")
        return False
def Check_balance():
    if acc_num:
        print(f'\nCurrent balance:{data[acc_num]["balance"]}')
    else:
        print("You need to login again")

def Deposit():
    if acc_num:
        amount=int(input("Enter the awmount to deposit: "))
        data[acc_num]['balance']+=amount
        data[acc_num]['history'].append(f'Deposited: ${amount}')
        print(f'${amount} is successfully deposited!!!')
    else:
        print("you need to login again")

def Withdraw():
    if acc_num:
        amount=int(input("Enter the amount to withdraw: "))
        if data[acc_num]['balance']>=amount:
            data[acc_num]['balance']-=amount
            data[acc_num]['history'].append(f'Withdraw - ${amount}')
            print(f'${amount} is successfully Withdraw')
        else:
            print("Insufficient Balance")
    else:
        print("You need to login again")


def View_transaction():
    if acc_num:
        if data[acc_num]['history']:
            print("Transactions History".center(50,'-'))
            for i in data[acc_num]['history']:
                print(i)
            else:
                print("End of the history".center(50,'-'))

        else:
            print("No Transactions")
    else:
        print("You need to login again")
   
    
