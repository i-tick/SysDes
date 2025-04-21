// The MediaPlayer class manages the current state of the Media Player using the State Design Pattern.

package State;

public class MediaPlayer {
    
    private State state;
    
    public MediaPlayer() {
        // TODO: Set the initial state of the Media Player to PlayingState
        this.state = new PlayingState();
        
        
    }
    
    public void setState(State state) {
        this.state = state;
    }
    
    public void play() {
        // TODO: Implement the functionality for pressing play
        this.state.pressPlay();
        
    }

    public void stop() {
        // TODO: Implement the functionality for pressing stop
        this.state.pressStop();
        
    }

    public void pause() {
        // TODO: Implement the functionality for pressing pause
        this.state.pressPause();
        
    }

    public void displayState() {
        // TODO: Implement the functionality to display the current state
        this.state.display();
        
    }
}