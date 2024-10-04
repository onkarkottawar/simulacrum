Enter amount to withdraw:

This is currently my code. (sorry for the messy code as I am a beginner)

pin = [123, 456, 789]
balance = [50000, 2000, 500]
name = ["name1", "name2", "name3"]


def main():
    while True:
        pin_input = input('Enter pin:')
        try:
            n = int(pin_input)
        except:
            break
        if n in pin:
            print('1 – Balance Inquiry')
            print('2 – Withdraw')
            print('3 – Deposit')
            print('X – Exit')
            choice = input('Enter your choice:')
            c = int(choice)
            if choice == 'X':
                print('Thank you for banking with us!')
                break
            else:
                pol = pin.index(n)
                if c == 1:
                    print(f'Hi {name[pol]}.')
                    print(f'Your current balance is {balance[pol]} ')
                elif c == 2:
                    print(f'Hi {name[pol]}.')
                    print(f'Your current balance is {balance[pol]} ')
                    withdraw = int(input('Enter amount to withdraw: '))
                    if withdraw > balance[pol]:
                        print('Not enough amount')
                    else:
                        difference = balance[pol] - withdraw
                        print('Transaction Successful')
                        print(f'Your current balance is {difference}')
                elif c == 3:
                    print(f'Hi {name[pol]}.')
                    print(f'Your current balance is {balance[pol]} ')
                    deposit = int(input('Enter amount to deposit: '))
                    sums = deposit + balance[pol]
                    print('')
                    print(f'Your current balance is {sums}')

main()
