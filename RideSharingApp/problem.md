# Problem Statement - Design a Ride-Sharing Application

## Overview  
You are tasked with designing and implementing a ride-sharing application where passengers can request rides, and drivers can be matched to them based on proximity. The application should handle different types of vehicles (such as cars, bikes, luxury cars) and support multiple fare calculation strategies. The system must notify both passengers and drivers about ride statuses and calculate the fare based on the type of ride and distance traveled.

## Requirements  

### Functional Requirements  
1. **Ride Request**  
    - Passengers can request a ride by providing their location and the desired destination.  
    - The system should calculate the distance between the passenger’s location and the driver’s location.  
    - The system must assign the nearest available driver to the passenger.  

2. **Vehicle Types**  
    - The system should support different vehicle types (e.g., car, bike, luxury car).  
    - Each vehicle type should have a different base fare per kilometer.  

3. **Fare Calculation**  
    - The system should use different fare strategies (e.g., standard fare, shared fare, luxury fare).  
    - The fare should be calculated based on the distance traveled and the vehicle type.  

4. **Ride Status Notifications**  
    - Both the passenger and the driver should be notified of ride statuses (e.g., ride started, ride completed).  
    - Use the **Observer Pattern** to notify users about ride status updates.  

5. **Ride Matching**  
    - Drivers should be assigned to passengers based on proximity.  
    - After a ride is completed, the driver becomes available for new ride requests.  

### Non-Functional Requirements  
1. **Scalability**  
    - The design should allow the system to easily add new types of vehicles and fare strategies without modifying core functionality.  

2. **Maintainability**  
    - Adhere to **SOLID principles** to ensure that the system is easy to maintain and extend.  
    - Ensure that future features can be added with minimal changes to the existing codebase.  

3. **Separation of Concerns**  
    - Separate the logic of fare calculation, ride matching, notifications, and user management into distinct components or classes.  

4. **Extensibility**  
    - The system should be extensible. New vehicle types (e.g., electric scooters, vans) and new fare strategies (e.g., peak-hour pricing) should be easily added without modifying the core ride-matching logic.  

## Constraints  
- The ride-matching algorithm must assign the nearest driver based on the distance between the passenger and driver.  
- You must implement at least three fare calculation strategies: **Standard**, **Shared**, and **Luxury**.  
- The system should be able to support different vehicle types: **Car** and **Bike** (with the option to extend for future vehicle types).  
- Notifications must be sent to both the passenger and driver as the ride progresses through different statuses (**pending**, **ongoing**, **completed**).  

## Expected Deliverables  
1. **Explanation**  
    - How **SOLID principles** are applied and why certain design patterns (e.g., **Strategy**, **Observer**, **Mediator**) were used.  

2. **Source Code**  
    - Clean, modular, and maintainable code for the ride-sharing application.  

3. **Test Cases**  
    - Verify correct functionality of the ride-matching system, fare calculation, and notification system.  

4. **Class Diagram**  
    - Showcases how classes and interfaces are structured, including how design patterns are applied.  

## Hints for Solution  
- Learners are expected to try the code themselves before referring to external solutions.  

### Key Design Patterns to Consider  
- **Strategy Pattern**: For implementing different fare calculation strategies.  
- **Observer Pattern**: For notifying passengers and drivers about ride status updates.  
- **Factory Pattern**: For creating instances of different vehicle types.  

### Additional Notes  
- Ensure the system is designed with **clean architecture** principles.  
- Focus on creating a **scalable**, **maintainable**, and **extensible** solution.  
