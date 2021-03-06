"""
File: cursor_based_list.py
Description:  Cursor-based list utilizing a header node and a trailer node.
Author:  Nick Sanford
"""

from node2way import Node2Way

class CursorBasedList(object):
    """ Linked implementation of a positional list."""
    
    def __init__(self):
        """ Creates an empty cursor-based list.
            header -> current -> trailer"""
        self._header = Node2Way(None)
        self._trailer = Node2Way(None)
        self._trailer.setPrevious(self._header)
        self._header.setNext(self._trailer)
        self._current = None
        self._size = 0

    def hasNext(self):
        """ Returns True if the current item has a next item.
            Precondition:  the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no next item")
        return self._current.getNext() != self._trailer

    def hasPrevious(self):
        """ Returns True if the current item has a previous item.
            Precondition:  the list is not empty."""
        return self._current.getPrevious() != None
    
    def first(self):
        """Moves the cursor to the first item
        if there is one.
        Precondition:  the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no first item")
        else:
            self._current = self._header.getNext()
        
    def last(self):
        """Moves the cursor to the last item
        if there is one.
        Precondition:  the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no first item")
        else:
            self._current = self._trailer.getPrevious()

    def next(self):
        """Precondition: hasNext returns True.
        Postcondition: The current item is has moved to the right one item"""
        if self.hasNext():
            self._current = self._current.getNext()
        else:
            raise AttributeError("Last item in list doesn't have a next item")

    def previous(self):
        """Precondition: hasPrevious returns True.
        Postcondition: The current item is has moved to the left one iten"""
        if self.hasPrevious():
            self._current = self._current.getPrevious()
        else:
            raise AttributeError("First item in list doesn't have a previous item")

    def insertAfter(self, item):
        """Inserts item after the current item, or
        as the only item if the list is empty.  The new item is the
        current item."""
        if self.isEmpty():
            self._current = Node2Way(item)
            self._trailer.setPrevious(self._current)
            self._header.setNext(self._current)
            self._current.setPrevious(self._header)
            self._current.setNext(self._trailer)
        else:
            new = Node2Way(item)
            new.setNext(self._current.getNext())
            new.setPrevious(self._current)
            self._current.getNext().setPrevious(new)
            self._current.setNext(new)
            self._current = new
        self._size+=1
            

    def insertBefore(self, item):
        """Inserts item before the current item, or
        as the only item if the list is empty.  The new item is the
        current item."""
        if self.isEmpty():
            self._current = Node2Way(item)
            self._header.setNext(self._current)
            self._trailer.setPrevious(self._current)
            self._current.setNext(self._trailer)
            self._current.setPrevious(self._header)
        else:
            new = Node2Way(item)
            new.setNext(self._current)
            new.setPrevious(self._current.getPrevious())
            self._current.getPrevious().setNext(new)
            self._current.setPrevious(new)
            self._current = new
        self._size+=1
        

    def getCurrent(self):
        """ Returns the current item without removing it or changing the
        current position.
        Precondition:  the list is not empty"""
        if self.isEmpty():
            raise AttributeError("Empty list has no Current item")
        else:
            return self._current.getData()

    def remove(self):
        """Removes and returns the current item. Making the next item
        the current item if one exists; otherwise the tail item in the
        list is the current item.
        Precondition: the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no items to remove")
        elif self.hasNext():
            self._current.getPrevious().setNext(self._current.getNext())
            self._current.getNext().setPrevious(self._current.getPrevious())
            item = self._current.getData()
            self._current = self._current.getNext()
            self._size -= 1
            return item
        else:
            self._current.getPrevious().setNext(self._trailer)
            item = self._current.getData()
            self._current = self._current.getPrevious()
            self._size -= 1
            return item

    def replace(self, newItemValue):
        """Replaces the current item by the newItemValue.
        Precondition: the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no Current item to replace")
        else:
            self._current.setData(newItemValue)

    def isEmpty(self):
        return self._size == 0

    def __len__(self):
        """ Returns the number of items in the list."""
        # replace below
        curr = self._header
        last = self._trailer
        num = 0
        while curr.getNext() != last:
            curr = curr.getNext()
            num += 1
        return num

    def __str__(self):
        """Includes items from first through last."""
        # replace below
        curr = self._header
        last = self._trailer
        items = ""
        while curr.getNext() != last:
            curr = curr.getNext()
            items += curr.getData()
        return items
            
            
        

