// This interface defines the contract for the mediator responsible for managing airplane communication and requests for takeoff and landing.

package Mediator;

public interface Mediator {
    void registerAirplane(Airplane airplane);
    void handleTakeoffRequest(Airplane airplane);
    void handleLandingRequest(Airplane airplane);
}