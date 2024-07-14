from threading import Thread, Lock


class BankAccount:
    def __init__(self, balance, *args, **kwargs):
        super(BankAccount, self).__init__(*args, **kwargs)
        self.amount = None
        self.balance = balance

    def withdraw(self, amount):
        with lock:
            self.amount = amount
            self.balance -= self.amount
            print(f'Withdrew {self.amount}, new balance is {self.balance}')

    def deposit(self, amount):
        with lock:
            self.amount = amount
            self.balance += self.amount
            print(f'Deposited {self.amount}, new balance is {self.balance}')


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)


lock = Lock()
acc = BankAccount(1000)

deposit_thread = Thread(target=deposit_task, args=(acc, 100))
withdraw_thread = Thread(target=withdraw_task, args=(acc, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()