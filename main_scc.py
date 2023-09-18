from forex_python.converter import CurrencyRates

def kalkulator_walutowy():
    c = CurrencyRates()
    print("Kalkulator Walutowy")
    amount = float(input("Podaj kwotę: "))
    from_currency = input("Podaj walutę źródłową (np. USD): ").upper()
    to_currency = input("Podaj walutę docelową (np. EUR): ").upper()
    
    try:
        exchange_rate = c.get_rate(from_currency, to_currency)
        converted_amount = amount * exchange_rate
        print(f"{amount} {from_currency} = {converted_amount} {to_currency}")
    except:
        print("Nie można przeliczyć waluty. Upewnij się, że wprowadziłeś poprawne kody walut.")

def lista_walut():
    print("Lista Dostępnych Walut:")
    c = CurrencyRates()
    currencies = c.get_rates('USD')  # Pobieranie kursów dla jednej waluty (może być dowolna)
    for code, rate in currencies.items():
        print(f"{code}: 1 USD = {rate} {code}")

def main():
    while True:
        print("\nMenu:")
        print("1. Kalkulator Walutowy")
        print("2. Lista Walut")
        print("3. Wyjdź")
        
        choice = input("Wybierz opcję (1/2/3): ")
        
        if choice == '1':
            kalkulator_walutowy()
        elif choice == '2':
            lista_walut()
        elif choice == '3':
            print("Dziękujemy za skorzystanie z programu. Do widzenia!")
            break
        else:
            print("Nieprawidłowy wybór. Wybierz 1, 2 lub 3.")

if __name__ == "__main__":
    main()
