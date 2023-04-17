from datetime import datetime
import uuid
class Payment():
    def __init__(self, amount, created_on=datetime.now(), payment_status="pending", transaction_id=uuid.uuid4()):
        self.__amount = amount
        self.__created_on = created_on
        self.__payment_status = payment_status
        self.__transaction = transaction_id

class QRCodeTransaction(Payment):
        def __init__(self, amount,qrcode_url="www.QRCODE.com", created_on=datetime.now(), payment_status="pending", transaction_id=uuid.uuid4()):
             super().__init__(amount, created_on, payment_status, transaction_id)

             self.__qrcode_url = qrcode_url

class CashTransaction(Payment):
     def __init__(self, amount, created_on=datetime.now(), payment_status="pending", transaction_id=uuid.uuid4()):
          super().__init__(amount, created_on, payment_status, transaction_id)

  
           
# payment1 = QRCodeTransaction(500, 130265, True, 1112,"www.qrcode.th")    
# payment2 = QRCodeTransaction(750, 152055, False, 1658, "www.qrcodepromptpay.th")    
# payment3 = CashTransaction(770, 158755, False, 1602)
# payment4 = CashTransaction(970, 200755, True, 9992)