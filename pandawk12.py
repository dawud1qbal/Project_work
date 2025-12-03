
import pandas as pd

def load_data():
    """Load Titanic dataset into a DataFrame."""
    try:
        df = pd.read_csv('titanic.csv')
        return df
    except FileNotFoundError:
        print("Error: 'titanic.csv' file not found.")
        return pd.DataFrame()

def calculate_average_age(df):
    """Calculate and return the average Age."""
    if 'Age' not in df.columns:
        print("Error: 'Age' column not found.")
        return None
    return df['Age'].dropna().mean()

def calculate_average_fare(df):
    """Calculate and return the average Fare."""
    if 'Fare' not in df.columns:
        print("Error: 'Fare' column not found.")
        return None
    return df['Fare'].dropna().mean()

def show_summary(df):
    """Show basic summary of the dataset."""
    print("\n--- Dataset Summary ---")
    print(df.describe(include='all'))

def filter_by_gender(df, gender):
    """Filter passengers by gender."""
    if 'Sex' not in df.columns:
        print("Error: 'Sex' column not found.")
        return pd.DataFrame()
    filtered = df[df['Sex'].str.lower() == gender.lower()]
    if filtered.empty:
        print(f"No passengers found for gender: {gender}")
    return filtered

def count_survivors(df):
    """Count number of survivors."""
    if 'Survived' not in df.columns:
        print("Error: 'Survived' column not found.")
        return None
    return df[df['Survived'] == 1].shape[0]

def menu():
    df = load_data()
    if df.empty:
        print("Dataset is empty. Exiting...")
        return

    while True:
        print("\nMain Menu")
        print("1. Show Average Age")
        print("2. Show Average Fare")
        print("3. Show Dataset Summary")
        print("4. Filter by Gender")
        print("5. Count Survivors")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            avg_age = calculate_average_age(df)
            if avg_age is not None:
                print(f"Average Age: {avg_age:.2f}")
        elif choice == '2':
            avg_fare = calculate_average_fare(df)
            if avg_fare is not None:
                print(f"Average Fare: {avg_fare:.2f}")
        elif choice == '3':
            show_summary(df)
        elif choice == '4':
            gender = input("Enter gender (male/female): ")
            filtered = filter_by_gender(df, gender)
            if not filtered.empty:
                print(filtered.head())
        elif choice == '5':
            survivors = count_survivors(df)
            if survivors is not None:
                print(f"Number of Survivors: {survivors}")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

menu()
