import os
import gzip
import json
import base64
import random
from datetime import datetime


# FUNCTIONS ############################################################################################################
def make_payment_id():
    payment_id = ''.join([random.choice('0123456789abcdef') for _ in range(16)])
    return payment_id


def make_monero_subscription_code(json_data):
    # Convert the JSON data to a string
    json_str = json.dumps(json_data)

    # Compress the string using gzip compression
    compressed_data = gzip.compress(json_str.encode('utf-8'))

    # Encode the compressed data into a Base64-encoded string
    encoded_str = base64.b64encode(compressed_data).decode('ascii')

    # Add the Monero Subscription identifier
    monero_subscription = 'monero-subscription:' + encoded_str

    return monero_subscription


def clear():
    if os.name == 'nt':  # for windows
        os.system('cls')
    else:  # for mac and linux(here, os.name is 'posix')
        os.system('clear')


# CHECK FUNCTIONS ######################################################################################################
def check_name(name):
    if len(name) <= 50:
        return True
    else:
        print(f'Subscription name "{name}" is too long. Please update it to be 50 characters or less in the {filename} file.')
        return False


def check_currency(currency):
    if currency == 'USD' or currency == 'XMR':
        return True
    else:
        print(f'Currency "{currency}" is not yet supported. Please use either "XMR" or "USD". Update it in the {filename} file.')
        return False


def check_wallet(wallet_address):
    # Check if the wallet address starts with the number 4
    if wallet_address[0] != "4":
        print(f'Wallet "{wallet_address}" is not valid. It should start with a "4" Update it in the {filename} file.')
        return False

    # Check if the wallet address is exactly 95 characters long
    if len(wallet_address) != 95:
        print(f'Wallet "{wallet_address}" is not valid. It should be exactly 95 characters long. Update it in the {filename} file.')
        return False

    # Check if the wallet address contains only valid characters
    valid_chars = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    for char in wallet_address:
        if char not in valid_chars:
            print(f'Wallet "{wallet_address}" is not valid. It contains invalid characters. Update it in the {filename} file.')
            return False

    # If it passed all these checks
    return True


def check_start_date(start_date):
    try:
        datetime.strptime(start_date, '%Y-%m-%d')
        return True
    except ValueError:
        print(f'Subscription Start Date "{start_date}" is not valid. It needs to be in Year-Month-Day format. Examples: 2023-01-26, 2023-12-21, 2023-07-01. Update it in the {filename} file.')
        return False


def check_amount(amount):
    if type(amount) is float:
        return True
    else:
        print(f'Amount "{amount}" is not valid. It needs to be a number with a decimal point. For $20, instead of 20, use 20.00. Update it in the {filename} file.')
        return False


def check_billing_cycle_days(billing_cycle):
    if type(billing_cycle) is int:
        return True
    else:
        print(f'Days In Billing Cycle "{billing_cycle}" is not valid. It needs to be a whole number without any commas or decimal points. Update it in the {filename} file.')
        return False


# VARIABLES ############################################################################################################
filename = 'Add_Your_Subscription_Info_Here.txt'
save_file = 'ID_And_Code.txt'


# START PROGRAM ########################################################################################################
# Create the file if it does not exist
if not os.path.exists(filename):
    # Ask questions to build subscription
    custom_label = input('Enter the name for this subscription without quotes. \nEXAMPLE: "Wallet Developer Donation", or "Mullvad VPN"\n')
    clear()
    sellers_wallet = input('Enter the wallet address that customers should pay without quotes. \nEXAMPLE: "4At3X5rvVypTofgmueN9s9QtrzdRe5BueFrskAZi17BoYbhzysozzoMFB6zWnTKdGC6AxEAbEE5czFR3hbEEJbsm4hCeX2S"\n')
    clear()
    currency = input('Should the subscription be tied to a US dollar amount (monero amount can vary based on the exchange rate), or a fixed amount of monero (ignoring the exchange rate)? \nEnter "USD" without quotes for US dollar amount, or "XMR" without quotes for monero amount.\n').upper()
    clear()
    amount = float(input('What should the subscription cost each time it is billed? \nEXAMPLE: For $20, enter "20.00" without quotes. For 0.10 XMR enter "0.10" without quotes.\n'))
    clear()
    billing_cycle_days = input('How often (in days) should the subscription be billed? \nEXAMPLE: If you want the subscription to be billed monthly, enter "30" without quotes. "365" for yearly, "7" for weekly, etc.\n')
    clear()
    if input('Should this subscription start right away?\nEnter "Yes" or "No" without quotes.\n').strip()[0].lower() == 'y':
        start_date = datetime.now().strftime("%Y-%m-%d")
    else:
        start_date = input('Enter the start date in the format "Year-Month-Day". \nEXAMPLE: "2023-04-26" with no quotes\n')

    clear()

    with open(file=filename, mode='w', encoding='utf-8') as f:
        f.write(f'{custom_label}\n{sellers_wallet}\n{currency}\n{amount}\n{billing_cycle_days}\n{start_date}')


# Read the file
with open(file=filename, mode='r', encoding='utf-8') as f:
    lines = f.readlines()

    custom_label = lines[0].strip()
    sellers_wallet = lines[1].strip()
    currency = lines[2].strip()
    amount = float(lines[3].strip().replace(',', ''))
    billing_cycle_days = int(lines[4].strip().replace(',', ''))
    start_date = lines[5].strip()

payment_id = make_payment_id()

# Make sure all the subscription fields are valid
if check_name(custom_label):
    if check_wallet(sellers_wallet):
        if check_currency(currency):
            if check_amount(amount):
                if check_start_date(start_date):
                    if check_billing_cycle_days(billing_cycle_days):
                        json_data = {
                            "custom_label": custom_label,
                            "sellers_wallet": sellers_wallet,
                            "currency": currency,
                            "amount": amount,
                            "payment_id": payment_id,
                            "start_date": start_date,
                            "billing_cycle_days": billing_cycle_days
                        }

                        monero_subscription_code = make_monero_subscription_code(json_data)

                        with open(file=save_file, mode='w', encoding='utf-8') as f:
                            f.write(f'Payment_ID:\n\n{payment_id}\n\n\n\nMonero Subscription Code:\n\n{monero_subscription_code}')

                        print('\nGive this monero-subscription code to the customer:\n')
                        print(monero_subscription_code)
                        print(f'\n...and save this payment_id: {payment_id}')
                        print(f'\nThe customer will use payment_id {payment_id} each time they send you a payment \n(and you will need to use it to identify that they have paid).\n')
                        print(f'\nFor easier copy/pasting, this info has been saved to the text file named "{save_file}"\n')
                        input('')
                        input('')  # in case the accidentally press enter while trying to copy it or something.
