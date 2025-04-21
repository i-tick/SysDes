// The State interface defines the methods for different states of the Media Player. 

package State;

public interface State {
    void pressPlay();
    void pressStop();
    void pressPause();
    void display();
}