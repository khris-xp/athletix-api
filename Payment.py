class Payment():
    def __init__(self, amount, created_on, payment_status, transaction_id):
        self._amount = amount
        self._created_on = created_on
        self._payment_status = payment_status
        self._transaction = transaction_id

class QRCodeTransaction(Payment):
        def __init__(self, amount, created_on, payment_status, transaction_id,qrcode_url):
             super().__init__(amount, created_on, payment_status, transaction_id)

             self._qrcode_url = qrcode_url

class CashTransaction(Payment):
     def __init__(self, amount, created_on, payment_status, transaction_id):
          super().__init__(amount, created_on, payment_status, transaction_id)

             
payment1 = QRCodeTransaction(500, 130265, True, 1112,"www.qrcode.th")    
payment2 = QRCodeTransaction(750, 152055, False, 1658, "www.qrcodepromptpay.th")    
payment3 = CashTransaction(770, 158755, False, 1602)
payment4 = CashTransaction(970, 200755, True, 9992)