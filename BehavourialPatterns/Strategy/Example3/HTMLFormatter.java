// This class implements the TextFormatter interface to format the text as HTML.

package Strategy;

public class HTMLFormatter implements TextFormatter {
    
    @Override
    public String format(String text) {
        // TODO: Wrap the input text in HTML tags: "<html><body>" and "</body></html>".
        return "<html><body>" + text + "</body></html>";
    }
}