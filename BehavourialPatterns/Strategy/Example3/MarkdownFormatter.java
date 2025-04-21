// This class implements the TextFormatter interface to format text using Markdown syntax.

package Strategy;

public class MarkdownFormatter implements TextFormatter {
    
    @Override
    public String format(String text) {
        // TODO: Wrap the input text in Markdown syntax: "**" and "**".
        return "**"+text+"**";
    }
}