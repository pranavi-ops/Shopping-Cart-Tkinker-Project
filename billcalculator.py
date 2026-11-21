import tkinter as tk

screen=tk.Tk("screen1")
screen.geometry("500x500")
screen.title("Bill Calculator")
screen.configure(bg="pink")

title=tk.Label(screen,text="Shopping Bill Calculator", bg="white", fg="black", font=("arial", 20, "bold"), borderwidth=2, border=0.5)
title.pack(pady=50)

tk.Label(screen,text="Product", bg="pink", fg="black", font=("arial", 15)).place(x=20,y=100)
tk.Label(screen,text="Price", bg="pink", fg="black", font=("arial", 15)).place(x=20,y=150)
tk.Label(screen,text="Quantity", bg="pink", fg="black", font=("arial", 15)).place(x=20,y=200)


product_input=tk.Entry(screen, width=25, justify="center")
product_input.place(x=150, y=100)

price_input=tk.Entry(screen, width=25, justify="center")
price_input.place(x=150, y=150)

quantity_input=tk.Entry(screen, width=25, justify="center")
quantity_input.place(x=150, y=200)
result_label=tk.Label(screen,text="Result: ", bg="pink", fg="green", font=("arial", 25, "bold"))
result_label.place(x=20,y=300)
def calculate_bill():
    product_name = product_input.get()
    price = price_input.get()
    quantity = quantity_input.get()
    print(product_name)
    if not product_name:
        result_label.configure(text="Missing product, please enter a product.")
    elif not price:
        result_label.configure(text="Missing price, please enter a price.")
    elif not quantity:
        result_label.configure(text="Missing quantity, please enter a quantity.")
    else:
        price=float(price)
        quantity=int(quantity)
        if price<0 or quantity <=0:
            result_label.configure("Enter Valid Values.")
        else:
            subtotal= price * quantity
            result_label.configure(text=f"Product: {product_name}\n Total Bill: ${subtotal}")
    if subtotal >= 100:
        discount=10
        discount_amount=round((discount/price)*100,2)
        total =round(subtotal-discount_amount,2)
        result_label.configure(text=f"Discount: {discount}%\nYou saved: ${discount_amount}\nFinal Bill: ${total}")               
button1 = tk.Button(screen, text="Calculate Bill", command=calculate_bill, bg="skyblue")
button1.place(x=150, y=250)

def clear_all():
    result_label.configure(text= "Result: ", fg="black")
    product_input.delete(0,tk.END)    
    price_input.delete(0,tk.END)
    quantity_input.delete(0,tk.END)
    
button2 = tk.Button(screen, text="Clear All", command=clear_all, bg="red")
button2.place(x=250, y=250)

screen.mainloop()