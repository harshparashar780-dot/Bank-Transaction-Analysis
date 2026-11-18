
import numpy as np
transaction_id = []
customer_id = []
customer_name = []
transaction_type = []
amount = []
status = []

opening_balance = []
while True:

    print("\n===== BANK TRANSACTION SYSTEM =====")
    print("1. Add Customer Opening Balance")
    print("2. Add New Transaction")
    print("3. View All Transactions")
    print("4. Total Deposits")
    print("5. Total Withdrawals")
    print("6. Customer Balance")
    print("7. Highest Transaction")
    print("8. Lowest Transaction")
    print("9. Bank Summary Report")
    print("10. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":

        cid = input("Enter Customer ID: ")
        name = input("Enter Customer Name: ")
        balance = float(input("Enter Opening Balance: "))

        if cid in customer_id:
            print("Customer ID already exists!")
        elif balance < 0:
            print("Balance cannot be negative!")
        else:
            customer_id.append(cid)
            customer_name.append(name)
            opening_balance.append(balance)

            print("Customer added successfully!")

    elif choice == "2":

        tid = input("Enter Transaction ID: ")
        cid = input("Enter Customer ID: ")

        if tid in transaction_id:
            print("Transaction ID already exists!")
            continue

        if cid not in customer_id:
            print("Customer not found! Add customer first.")
            continue

        name = customer_name[customer_id.index(cid)]

        ttype = input("Enter Deposit or Withdrawal: ").capitalize()

        if ttype not in ["Deposit", "Withdrawal"]:
            print("Invalid transaction type!")
            continue

        amt = float(input("Enter Amount: "))

        if amt <= 0:
            print("Amount must be greater than zero!")
            continue

        current_balance = opening_balance[customer_id.index(cid)]

        if ttype == "Withdrawal" and amt > current_balance:
            print("Insufficient balance!")
            continue

        trans_status = input("Enter Success or Failed: ").capitalize()

        if trans_status not in ["Success", "Failed"]:
            print("Invalid status!")
            continue

        transaction_id.append(tid)
        customer_id.append(cid)
        customer_name.append(name)
        transaction_type.append(ttype)
        amount.append(amt)
        status.append(trans_status)

        if trans_status == "Success":
            if ttype == "Deposit":
                opening_balance[customer_id.index(cid)] += amt
            else:
                opening_balance[customer_id.index(cid)] -= amt

        print("Transaction recorded successfully!")

    elif choice == "3":

        print("\n===== ALL TRANSACTIONS =====")

        if len(transaction_id) == 0:
            print("No transactions available.")

        for i in range(len(transaction_id)):
            print(
                transaction_id[i],
                customer_id[i],
                customer_name[i],
                transaction_type[i],
                amount[i],
                status[i]
            )

    elif choice == "4":

        a = np.array(amount)
        t = np.array(transaction_type)
        s = np.array(status)

        deposits = a[(t == "Deposit") & (s == "Success")]

        print("Total Deposits:", np.sum(deposits))

    elif choice == "5":

        a = np.array(amount)
        t = np.array(transaction_type)
        s = np.array(status)

        withdrawals = a[(t == "Withdrawal") & (s == "Success")]

        print("Total Withdrawals:", np.sum(withdrawals))

    elif choice == "6":

        cid = input("Enter Customer ID: ")

        if cid in customer_id:
            index = customer_id.index(cid)
            print("Customer:", customer_name[index])
            print("Current Balance:", opening_balance[index])
        else:
            print("Customer not found!")

    elif choice == "7":

        a = np.array(amount)
        s = np.array(status)

        successful = np.where(s == "Success")[0]

        if len(successful) == 0:
            print("No successful transactions.")
        else:
            i = successful[np.argmax(a[successful])]
            print("Highest Transaction:", a[i])
            print("Transaction ID:", transaction_id[i])
            print("Customer:", customer_name[i])

    elif choice == "8":

        a = np.array(amount)
        s = np.array(status)

        successful = np.where(s == "Success")[0]

        if len(successful) == 0:
            print("No successful transactions.")
        else:
            i = successful[np.argmin(a[successful])]
            print("Lowest Transaction:", a[i])
            print("Transaction ID:", transaction_id[i])

    elif choice == "9":

        a = np.array(amount)
        s = np.array(status)
        t = np.array(transaction_type)

        print("\n===== BANK SUMMARY REPORT =====")

        print("Total Customers:", len(opening_balance))
        print("Total Transactions:", len(transaction_id))

        print("Successful Transactions:",
              np.sum(s == "Success"))

        print("Failed Transactions:",
              np.sum(s == "Failed"))

        print("Total Deposits:",
              np.sum(a[(t == "Deposit") & (s == "Success")]))

        print("Total Withdrawals:",
              np.sum(a[(t == "Withdrawal") & (s == "Success")]))

        if len(a) > 0:
            print("Average Transaction:", np.mean(a))

        print("Total Current Bank Balance:",
              np.sum(opening_balance))

    elif choice == "10":

        print("Thank you for using Bank System!")
        break

    else:
        print("Invalid choice! Try again.")
