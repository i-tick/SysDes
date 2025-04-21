// This defines an interface for collections that provide an iterator for notifications.

package Iterator;

import java.util.Iterator;

public interface NotificationCollection {
    public Iterator<Notification> createIterator();
}