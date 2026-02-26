from http_client import http_get
from dns_lookup import dns_lookup
from ping_test import ping_test

def show_menu():
    print("\n=== Mini Network Tool ===")
    print("1. HTTP GET Request")
    print("2. DNS Lookup")
    print("3. Ping Test")
    print("4. Exit")

def main():
    while True:
        show_menu()
        choice = input("Select option: ")

        if choice == "1":
            http_get()
        elif choice == "2":
            dns_lookup()
        elif choice == "3":
            ping_test()
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()