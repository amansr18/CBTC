import random
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def create_receipt(receipt_data, file_name):
    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter

    # Add title
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2.0, height - 50, "Payment Receipt")

    # Add receipt details
    c.setFont("Helvetica", 12)
    line_height = 30
    start_y = height - 100

    for key, value in receipt_data.items():
        c.drawString(50, start_y, f"{key}: {value}")
        start_y -= line_height

    # Add thank you message
    c.setFont("Helvetica-Oblique", 14)
    c.setFillColor(colors.darkgreen)
    c.drawCentredString(width / 2.0, 100, "Thank you for your purchase!")

    c.save()

def get_receipt_data():
    date = datetime.now().strftime("%Y-%m-%d")
    receipt_no = str(random.randint(100000, 999999))
    customer_name = input("Enter the customer name: ")
    item_purchased = input("Enter the item purchased: ")
    quantity = int(input("Enter the quantity: "))
    price_per_item = float(input("Enter the price per item: $"))
    total_amount = quantity * price_per_item
    payment_method = input("Enter the payment method: ")

    receipt_data = {
        "Date": date,
        "Receipt No": receipt_no,
        "Customer Name": customer_name,
        "Item Purchased": item_purchased,
        "Quantity": quantity,
        "Price per Item": f"${price_per_item:.2f}",
        "Total Amount": f"${total_amount:.2f}",
        "Payment Method": payment_method
    }
    return receipt_data

if __name__ == "__main__":
    receipt_data = get_receipt_data()
    create_receipt(receipt_data, "payment_receipt.pdf")
