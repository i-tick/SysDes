// This class represents the actual network service that fetches data from a remote server.

package Proxy;

public class RealNetworkService implements NetworkService {
    
    private String data;
    
    @Override
    public String fetchData(String input) {
        data = "Data fetched from remote server for input: " + input;
        return data;
    }
}