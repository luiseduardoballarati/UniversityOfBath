public class NodeRunner {
    public static void main(String[] args){
        SortedLinkedList list = new SortedLinkedList();
        list.add(new Node("Charlie"));
        list.add(new Node("Alpha"));
        list.add(new Node("Bravo"));
        Node nFirst = list.getFirst();
        Node nLast = list.getLast();
        Node nMiddle = list.get(1);
        if(nFirst.getString().equals("Alpha") && nMiddle.getString().equals("Bravo") && nLast.getString().equals("Charlie")) {
            System.out.println("Well done!");
        }
        else {
            System.out.println("Adding a node has not been successful");
        }
        System.out.println("List contains " + list.size() + " items:");
        list.print();
    }
}
