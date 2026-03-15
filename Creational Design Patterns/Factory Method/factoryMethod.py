from abc import ABC, abstractmethod

class PaymentGateway(ABC):
  def __init__(self):
    pass
    
  @abstractmethod
  def Payment(self):
    pass

class CreditCard(PaymentGateway):
  def __init__(self):
    pass

  def Payment(self):
    print("Payment is successful with credit card")

class InternetBanking(PaymentGateway):
  def __init__(self):
    pass

  def Payment(self):
    print("Payment is successful with Internet Banking")


# Factory Class
class PaymentFactory:
  def get_payment_gateway(gateway: str):
    if gateway=="credit card":
      return CreditCard()
    elif gateway=="internet banking":
      return InternetBanking()
    return None

if __name__ == "__main__":
  payment_gateway = PaymentFactory.get_payment_gateway("credit card")
  payment_gateway.Payment()
