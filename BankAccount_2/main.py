from CheckingAccount import CheckingAccount
from SavingsAccount import SavingsAccount


def main ():


    #Check print info works properly

    #CheckingAccount transfer properly
    checking_account1 = CheckingAccount("John Brown",10000, 500, 10000001, 900000000, 5)

    print(f"checking account1 balance: {checking_account1.current_balance}")

    checking_account2 = CheckingAccount("Joe Smith", 1000, 100, 10000002, 900000000, 3)

    print(f"checking account2 balance: {checking_account2.current_balance}")

    checking_account1.transfer(2000, checking_account2)

    print(f"checking account1 balance: {checking_account1.current_balance}")

    print(f"checking account2 balance: {checking_account2.current_balance}")

    # Check print customer info works properly
    checking_account1.print_customer_information()

    #CheckingAccount transfers_performed is counted properly

    checking_account2.transfer(200, checking_account1)

    checking_account2.transfer(1000, checking_account1)

    checking_account2.transfer(10, checking_account1)

    checking_account2.transfer(100, checking_account1)

    #CheckingAccount withdrawal and deposit work correctly

    check_account3 = CheckingAccount("Bryan Goodyear", 1350, 600, 10000003, 900000000, 1)

    check_account3.deposit(1000)

    print(f"checking account3 balance: {check_account3.current_balance}")

    check_account3.withdraw(10)

    print(f"checking account3 balance: {check_account3.current_balance}")

    check_account3.withdraw(10000)

    print(f"checking account3 balance: {check_account3.current_balance}")


    #SavingsAccount withdrawal and deposit work correctly

    savings_test1 = SavingsAccount("Lauren Goodyear", 12000, 5000, 10000004, 900000000, .05)

    print(f"savings account balance: {savings_test1.current_balance}")

    savings_test1.withdraw(1000)

    print(f"savings account balance: {savings_test1.current_balance}")

    savings_test1.deposit(3000)

    print(f"savings account balance: {savings_test1.current_balance}")

    savings_test1.withdraw(9001)

    print(f"savings account balance: {savings_test1.current_balance}")

    #savings account interest function check
    sav_1 = SavingsAccount("Ryan Brown", 1000, 100, 10000005, 900000000, .05)

    print(f"savings account balance: {sav_1.current_balance}")

    expected_interest = 1000 * .05

    if expected_interest != sav_1.interest():
        print(f"{expected_interest} is not equal to {sav_1.interest()}, function aint working right")
        return

    print(f"Interest calculated properly")

    expected_balance = 1000 * .05 + 1000

    if expected_balance != sav_1.current_balance:
        print(f"{expected_balance} is not equal to {sav_1.current_balance}")
        print("Error in adding to balance")
        return

    print("All functions working properly")


main()

