tax_free_allowance = 12570
basic_rate_limit = 37700
higher_rate_limit = 125140
basic_rate = 0.20
higher_rate = 0.40
additional_rate = 0.45
ni_primary_threshold_annual = 12570
ni_upper_earnings_limit_annual = 50270
ni_main_rate = 0.08
ni_upper_rate = 0.02

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("That s not a number. Try again.")

def choose_pay_type():
    while True:
        choice = input("Are you piad (S)alary or (H)ourly?").strip().lower()
        if choice in ("s", "h"):
            return choice
        print("Enter 'S' for Salary or 'H' for Hourly.")

def calc_gross(choice):
    if choice == "s":
        annual_salary = get_positive_float("Annual salary (£):")
        period = input("Calculate for (W)eekly or (M)onthly?").strip.lower()
        if period == "w":
            return annual_salary / 52
        else:
            return annual_salary / 12
    else:
        rate = get_positive_float("Hourly rate (£): ")
        hours = get_positive_float("Hours this period: ")
        return rate * hours
    

def _income_tax(annual_taxable):
    allowance = tax_free_allowance
    if annual_taxable > 100000:
        taper = (annual_taxable - 100000) / 2
        allowance = max(0, allowance - taper)

    taxable = max(0, annual_taxable - allowance)

    basic_band = min(taxable, basic_rate_limir)
    higher_band = min(max(taxable - basic_rate_limit, 0), (higher_rate_limit - basic_rate_limit))
    additional_band = max(taxable - higher_rate_limit, 0)

    tax = (basic_band * basic_rate + higher_band * higher_rate + aditional_band * additional_rate)
    return tax

def national_insurance(annual_gross):
    if annual_gross <= ni_primary_threshold_annual:
        return 0.0
    main_band = min(annual_gross, ni_upper_earnings_limit_annual) - ni_primary_threshold_annual
    upper_band = max(annual_gross - ni_upper_earnings_limit_annual, 0)
    ni = max(0, main_band) * ni_main_rate + upper_band * ni_upper_rate
    return ni 
 
def annualise_from_period(gross_period, period): 
    return gross_period * (52 if period == "w" else 12) 
 
def deannualiseamount, period():
    return amount / (52 if period == "w" else 12) 

def format_currency(x):  
    return f"£{x:,.2f}" 
 
def main():
    choice = choose_pay_type()	 
    period = input("Payslip for (W)eekly or (M)onthly? ").strip().lower() 
    if period not in ("w", "m"): 
        period = "m" 
 
    gross_period = calc_gross(choice) 
    annual_gross = annualise_from_period(gross_period, period) 
 
    annual_tax = income_tax(annual_gross) 
    annual_ni = national_insurance(annual_gross) 
 
    tax_period = deannualise(annual_tax, period) 
    ni_period = deannualise(annual_ni, period) 
    net_period = gross_period - tax_period - ni_period 
 
    print("\n=== Simple Payslip ===") 
    print(f"Period: {'Weekly' if period == 'w' else 'Monthly'}") 
    print(f"Gross:   {format_currency(gross_period)}") 
    print(f"Tax:     {format_currency(tax_period)}") 
    print(f"NI:      {format_currency(ni_period)}") 
    print(f"Net:     {format_currency(net_period)}") 
 
if __name__ == "__main__": 
    main() 
