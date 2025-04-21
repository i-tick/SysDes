
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
    user_service = UserService()
    order_service = OrderService()
    payment_service = PayementService()
    
    user_details = user_service.getuserdetails(1)
    order_details = order_service.getorderdetails(1)
    payment_details = payment_service.getpaymentdetails(1)
    
    print(user_details)
    print(order_details)
    print(payment_details)

    # Problem with this approach:
    # client has to interact with each class separately
    # client has to know about the implementation of each class - exposing the implementation
    # it increaes the complexity of the code
    # tight coupling
