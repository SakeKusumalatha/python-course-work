#1, Function data Formation:

data={'current_balance':5000,'history':[]}

def Menu():
    print('[c]heck Balence')
    print('[D]eposit')
    print('[W]ithdraw')
    print('[V]iew Transaction History')
    print('[E]xit')

def Welcome():
    print('Welcome to ATM'.center(40,'*'))

def Check_Balance():
    print(f'Current Balance: ${data["current_balance"]}')

def Withdraw():
    amount=int(input("Enter the amount to withdraw: "))
    if amount<=data['current_balance']:
        data['current_balance']-=amount
        data['history'].append(f'Withdraw: ${amount}')
        print(f'${amount} is successfully Withdraw!!!')
    else:
        print('Insufficient Balence')
        
def Deposit():
    amount=int(input("Enter the awmount to deposit:"))
    data['current_balance']+=amount
    data['history'].append(f'Deposited: ${amount}')
    print(f'${amount} is successfully deposited!!!')

def View_History():
    if data['history']:
        print('Transaction History'.center(40,'-'))
        for i in data['history']:
            print(i)
        else:
            print("No Transaction")

def Flow_Check(ch):
    if ch=='C':
        Check_Balance()
    elif ch=='D':
        Deposit()
    elif ch=='W':
        Withdraw()
    elif ch=='V':
        View_History()
   
Welcome()
while True:
    Menu()
    ch=input("Enter the char[CDWVE]: ").upper()
    Flow_Check(ch)
    if ch=='E':
        print("Thankyou".center(40,'.'))
        break
else:
    print("Invalid Choice")