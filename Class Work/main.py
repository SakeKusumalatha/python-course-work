import ATMlogic as atm

atm.Welcome()

if atm.Login():
    while True:
        atm.Menu()
        ch=input("Enter the choice: ").upper()
        if ch=='C':
            atm.Check_balance()
        elif ch=='D':
            atm.Deposit()
        elif ch=='W':
            atm.Withdraw()
        elif ch=='V':
            atm.View_transaction()
        elif ch=='E':
            print("thankyou".center(50,'_'))
            break
        else:
            print("invalid Choice")

    '''#output:
    ******************Welcome to ATM******************
Enter the account number: 12345
Enter the pin: 123
Login Successful

[c]heck Balence
[D]eposit
[W]ithdraw
[V]iew Transaction History
[E]xit

Enter the choice: D
Enter the awmount to deposit: 34567789
$34567789 is successfully deposited!!!

[c]heck Balence
[D]eposit
[W]ithdraw
[V]iew Transaction History
[E]xit

Enter the choice: W
Enter the amount to withdraw: 5647
$5647 is successfully Withdraw

[c]heck Balence
[D]eposit
[W]ithdraw
[V]iew Transaction History
[E]xit

Enter the choice: C

Current balance:34567820

[c]heck Balence
[D]eposit
[W]ithdraw
[V]iew Transaction History
[E]xit

Enter the choice: V
---------------Transactions History---------------
Deposited: $34567789
Withdraw - $5647
----------------End of the history----------------

[c]heck Balence
[D]eposit
[W]ithdraw
[V]iew Transaction History
[E]xit

Enter the choice: E
_____________________thankyou_____________________'''