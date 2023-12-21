public class SortedLinkedList implements SortedList {
    private Node head;
    private Node tail;

    @Override
    public int size() {
        int counter = 0;
        Node n = head;
        while (n.getNext()!=null){
            n = n.getNext();
            counter++;
        };
        return counter+1;
    }
    @Override
    public void add(String string) {
        if (!isPresent(string)) {
            Node node = new Node(string);
            if (head == null) {
                head = node;
                tail = node;
            } else {
                Node n = head;
                while (n.getNext() != null) {
                    n = n.getNext();
                }
                n.setNext(node);
                node.setPrev(n);
            }
        }
    }
    @Override
    public void add(Node node) {
        if (!isPresent(node.getString())) {
            if (head == null) {
                head = node;
                node.setNext(null);
                node.setPrev(null);
                return;
            }
            Node n = head;
            while (n != null && node.getString().compareTo(n.getString()) > 0) {
                n = n.getNext();
            }
            if (n == null) {
                tail.setNext(node);
                node.setPrev(tail);
                tail = node;
            } else {
                Node prev = n.getPrev();
                node.setNext(n);
                node.setPrev(prev);
                n.setPrev(node);

                if (prev != null) {
                    prev.setNext(node);
                } else {
                    head = node;
                }
            }
        }
    }


    @Override
    public Node getFirst(){
        if (head==null){
            return null;
        }
        return head;
    }
    @Override
    public Node getLast() {
        if (head == null) {
            return null;
        } else {

            Node current = head;
            while (current.getNext() != null) {
                current = current.getNext();
            }
            return current;
        }
    }
    @Override
    public Node get(int index) {
        Node n = head;
        if (index == 0) {
            getFirst();
        }
        else {
            for (int i = 0; i <= index - 1; i++) {
                n = n.getNext();
            }
        }
        return n;

    }
    @Override
    public boolean isPresent(String string){
        Node n = head;
        while(n!=null){
            if(n.getString().equalsIgnoreCase(string)){
                return true;
            }
            n = n.getNext();
        }
        return false;
    }
    @Override
    public boolean removeFirst() {
        Node n = head;
        if (head == null) {
            return false;
        } else {
            head = head.getNext();
            return true;
        }
    }
    @Override // need to be done
    public boolean removeLast(){
        Node n = head;
        Node n1 = null;
        if (head==null){
            return false;
        }
        if (head.getNext()==null) {
            head = null;
            return true;
        }
        else {
           while (n.getNext()!=null){
               n = n.getNext();
           }
           n1 = n.getPrev();
           n1.setNext(null);
           n = null;
            }
        return true;
        }
    @Override
    public boolean remove(int index){
        boolean rmi;
        rmi = false;
        if (index==0){
            head = head.getNext();
            rmi = true;
        }
        else{
            Node n = head;
            Node n1 = null;
            for(int i=0;i<index-1;i++){
                n = n.getNext();
            }
            n1 = n.getNext();
            n.setNext(n1.getNext());
            n1 = null;
            rmi = true;
        }
        return rmi;
    }
    @Override
    public boolean remove(String string){
        Node n = head;
        Node n1 = null;
        if (n != null && n.getString().equals(string)){
            head = n.getNext();
            return true;
        }
        while (n.getNext()!=null){
            if (n.getString().equals(string)){

                    n1 = n.getPrev();
                    n1.setNext(n.getNext());
                    return true;
            }
            n = n.getNext();
            if (n.getNext()==null && n.getString().equals(string)){
                removeLast();
            }
        }
        return false;
    }
    @Override
    public void orderAscending() {
        Node current = head, index = null;
        String temp;

        if (head == null) {
            return;
        } else {
            while (current != null) {
                index = current.getNext();
                while (index != null) {
                    if (current.getString().compareTo(index.getString()) > 0) {
                        temp = current.getString();
                        current.setString(index.getString());
                        index.setString(temp);
                    }
                    index = index.getNext();
                }
                current = current.getNext();
            }
        }
    }
    @Override
    public void orderDescending(){
        Node current = head, index = null;

        String temp;

        if (head == null) {
            return;
        } else {
            while (current != null) {
                index = current.getNext();
                while (index != null) {
                    if (current.getString().compareTo(index.getString()) < 0) {
                        temp = current.getString();
                        current.setString(index.getString());
                        index.setString(temp);
                    }
                    index = index.getNext();
                }
                current = current.getNext();
            }
        }
    }
    @Override
    public void print(){
        Node node = head;
        for(int i = 0;i<size();i++){
            System.out.println(node.getString());
            try{
                node = node.getNext();
            }
            catch (Exception e){
                return;
            }
        }
    }
}
