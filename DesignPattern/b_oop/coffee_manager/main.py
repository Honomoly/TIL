from presentation.Menu import *
from service.Coffee import *
from service.Account import *

def main():
    drinks = [
        Coffee("아메리카노", 2500, 1000, 25, 40, 0),
        Coffee("카페라떼", 3500, 2500, 15, 25, 0),
        Coffee("카라멜 마키아또", 4000, 3200, 10, 20, 0),
    ]
    account = Account()
    Menu(drinks, account)

if __name__ == "__main__":
    main()