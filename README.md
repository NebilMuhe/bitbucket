# Implementing YayaWallet Webhook using Django

I approached the YaYa Wallet webhook solution by first verifying the payload's authenticity using YAYA-SIGNATURE. Upon confirming its origin from YaYa Wallet, I proceeded to create objects and sent a 200 response. However, testing the response posed a significant challenge as the SECRET_KEY was unavailable, hindering the thorough validation of the solution. This absence of the SECRET_KEY became the primary obstacle in ensuring the effectiveness of the implemented webhook solution for YaYa Wallet transactions

# To install the application use

1, clone the repository
2, cd bitbuckket
3, pip install -r requirment.txt
