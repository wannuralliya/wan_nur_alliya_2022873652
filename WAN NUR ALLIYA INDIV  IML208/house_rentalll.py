
import tkinter as tk
import mysql.connector

# Connect to my MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="house_rental"
)

# creating cursor object to execute SQL queries
mycursor = mydb.cursor()

# Function to handle the calculation and database saving
def collect_data():
    global location_var  # Declare location_var as a global variable
    house_type = package_var.get()
    period_month = int(period_entry.get())
    house_location = location_var.get()  # Get house location from the dropdown
    
    # Defining the prices from the User selections
    prices = {
        "Bungalow house": 1000,
        "Terrace house": 850,
        "Flat house": 750,
    }

    # Calculating the total price. Derived from the selection (Type, Period).
    total_price = prices[house_type] * period_month
    
    # Inserting data into the database, 4 attributes.
    sql = "INSERT INTO `user` (house_type, period, total_price, house_location) VALUES (%s, %s, %s, %s)"
    val = (house_type, period_month, total_price, house_location)
    mycursor.execute(sql, val)
    mydb.commit()

    # To print back the output. It will happen in the function collect_data().
    output_label.config(text=f"House type: {house_type}, Period: {period_month}, Total Price: RM{total_price}, Location: {house_location}")

# Your Main window, You need to have the title, geometry (MUST)
root = tk.Tk()
root.title("House Rental WanNur")
root.geometry('900x800')

# Page Title
label = tk.Label(root, text='MyHome MyHeaven', font=("Cooper Black", 16, "bold"))
label.pack(ipadx=10, ipady=10)

# Prices List by using textbox
prices_text = tk.Text(root, height=15, width=45)
prices_text.pack(pady=20)

# The defined list by using pricebox
prices_text.insert(tk.END, "House Type & Prices:\n\n")
prices_text.insert(tk.END, "Bungalow house\nPrice: RM1000/1 Month\n\n")
prices_text.insert(tk.END, "Terrace House \nPrice: RM850/1 Month\n\n")
prices_text.insert(tk.END, "Flat House \nPrice: RM750/1 Month\n\n")
prices_text.configure(state='disabled')

# Trip Type Dropdown (Label)
period_label = tk.Label(root, text="Choose Your House Type")
period_label.pack()

# Trip Type Dropdown
package_var = tk.StringVar(root)
package_var.set("Bungalow house")  # Default value before your selection
trip_dropdown = tk.OptionMenu(root, package_var, "Bungalow house", "Terrace house", "Flat house")
trip_dropdown.pack(pady=10)

# Packs Entry. Label and user can insert data thru entry
period_label = tk.Label(root, text="Period(Month):")
period_label.pack()
period_entry = tk.Entry(root)
period_entry.pack()

# House Location Dropdown (Label)
location_label = tk.Label(root, text="Choose House Location")
location_label.pack()

# House Location Dropdown
location_var = tk.StringVar(root)
location_var.set("Kedah")  # Default value before your selection
location_dropdown = tk.OptionMenu(root, location_var, "Kedah", "Pahang", "Penang")
location_dropdown.pack(pady=10)

# Save Button
save_button = tk.Button(root, text="Calculate", command=collect_data)
save_button.pack(pady=10)

# Output Label & result
result_label = tk.Label(root, text='DONEE !!!', font=("Times New Romans", 12))
result_label.pack(ipadx=10, ipady=10)
output_label = tk.Label(root, text="")
output_label.pack()

# Set the background color
root.configure(bg='#B660CD')

root.mainloop()
