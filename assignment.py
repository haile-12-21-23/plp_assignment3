def calculate_discount(price, discount_precentage):
    if discount_precentage>=20:
        discount_amount=price*(discount_precentage/100)
        return price-discount_amount
    else:
        return price

if __name__=="__main__":
    try:
        original_price=float(input("Enter the original price of the item:"))
        discount_percentage=float(input("Enter the discount percentage:"))
        final_price=calculate_discount(original_price,discount_percentage)

        if  discount_percentage>=20:
            print(f"Discount appiled. The final price : ${final_price:.2f}")
        else:
            print(f"No dicount applied. Final price: ${final_price: .2f}")

    except Exception as e:
        print("Invlid input. Please enter numeric valus.")