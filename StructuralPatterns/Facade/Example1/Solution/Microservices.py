
class APIgateway:
    def __init__(self):
        self.user_service = UserService()
        self.order_service = OrderService()
        self.payment_service = PayementService()
    
    def get_full_details(self, user_id, order_id, payment_id):
        user_details = self.user_service.getuserdetails(user_id)
        order_details = self.order_service.getorderdetails(order_id)
        payment_details = self.payment_service.getpaymentdetails(payment_id)
        
        return {
            "user": user_details,
            "order": order_details,
            "payment": payment_details
        }

class UserService:
    
    def getuserdetails(self, user_id):
        # Simulate fetching user details from a database
        return {
            "user_id": user_id,
        }
    
class OrderService:
    
    def getorderdetails(self, order_id):
        # Simulate fetching order details from a database
        return {
            "order_id": order_id,
        }

class PayementService:
    
    def getpaymentdetails(self, payment_id):
        # Simulate fetching payment details from a database
        return {
            "payment_id": payment_id,
        }
    
if __name__ == "__main__":
    api_gateway = APIgateway()
    full_details = api_gateway.get_full_details(1, 1, 1)
    print(full_details)
    # This is the Facade pattern
    # It provides a simplified interface to a complex system
    # The client interacts with the APIgateway class instead of each individual service
    # This reduces the complexity of the code and makes it easier to use
    # The client does not need to know about the implementation of each class, which can change and doesnt hampers the client code
    # Centralized access point, Control over the system
    # This reduces the coupling between the client and the individual services

 