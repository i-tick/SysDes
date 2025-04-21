// This factory class is responsible for creating instances of different document types.

package Factory;

public class DocumentFactory {
    
    public static Document createDocument(String type) {
        
        switch (type.toLowerCase()) {
            case "pdf":
                // TODO: Return a new instance of PDFDocument
                return new PDFDocument();
                
                
            case "word":
                // TODO: Return a new instance of WordDocument
                return new WordDocument();
                
                
            default:
                throw new IllegalArgumentException("Unknown document type: " + type);
        }
    }
}