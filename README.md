# Monero Subscription Code Creator
![Supported OS](https://img.shields.io/badge/Supported%20OS-Windows%20/%20Mac%20/%20Linux-blueviolet.svg)
![Version 1.0.0](https://img.shields.io/badge/Version-1.0.0-blue.svg)
![Python 3.8+](https://img.shields.io/badge/Python-3.8+-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A tool for creating custom `monero-subscriptions` codes (and their matching payment_ids)


# BEFORE YOU START 
Make sure you have [Python 3.8](https://www.python.org/downloads/) or newer installed


# How To Use:
* Step #1 - [Click Here To Download The Files](https://github.com/lukeprofits/Monero_Subscription_Code_Creator/archive/refs/heads/main.zip) extract all the files from the .zip you downloaded and put them in a folder.

* Step #2 - Double click `Windows Launcher.bat` (or `Mac&Linux Launcher.sh` if you are using Mac/Linux). You will be asked a series of questions. These questions are used to help you create the subscription. After answering these questions, a text file called `Add_Your_Subscription_Info_Here.txt` will be created.

* Step #3 - A monero-subscription code and payment_id will be generated and saved in the file `ID_And_Code.txt`. Send the monero-subscription code to your customer, and store the payment_id in your database/spreadsheet of customer data (so that when you receive a payment in the future with this payment_id, you will know that it is for the customer that you gave the monero-subscription code). 
	
* Step #4 - For a new customer, if you would like to generate a new payment_id and monero-subscription code for the same subscription, simply run `Windows Launcher.bat` again. New ones will be generated and saved in the file `ID_And_Code.txt`. You do not need to re-enter the subscription information. All of this is all saved in the `Add_Your_Subscription_Info_Here.txt` file.


# Making A Different Subscription 
If you want to make an unrelated subscription, or want to make changes to the info that you used before, you can simply edit the `Add_Your_Subscription_Info_Here.txt` file.
Alternatively, you can delete the `Add_Your_Subscription_Info_Here.txt` file, and then run `Windows Launcher.bat` again (if you prefer to use the prompts rather than edit a text file).


# Modifying The File 
Here is what should go on each line of the `Add_Your_Subscription_Info_Here.txt` file (make sure to get the order correct and have NOTHING else in the file!):

* Line 1: Subscription Name - This can be any custom text 50 characters less. 
* Line 2: Sellers Wallet - This should be your main public wallet address (not a subaddress).
* Line 3: Currency (USD or XMR) - Do you want it to be tied to a US dollar amount (i.e. $25 worth of monero) or an XMR amount (i.e. 0.100000000000 monero regardless of the exchange rate).
* Line 4: Amount To Charge - Enter the amount as a number with a decimal point. For example, $25 would be 25.00. Or if you are using a monero amount, 0.103589 XMR would be 0.103589.
* Line 5: Number Of Days Per Billing Cycle (i.e. 30) - You can use 30 for monthly, 365 for yearly, 7 for weekly, or anything else custom that you would like. Just make sure it is a whole number.
* Line 6: Subscription Start Date in Year-Month-Day format (i.e. 2023-04-26) - If you want the subscription to start right away, you can use today's date, or any date in the past. 

You do not need to add a payment_id, because a random one will be used/generated for each customer. 


# Troubleshooting: 
If you ever notice the program is acting wierd, or opening and then immediatly closing, try deleting the `Add_Your_Subscription_Info_Here.txt` file and then try again.
