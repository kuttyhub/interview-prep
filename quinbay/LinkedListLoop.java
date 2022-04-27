public class LinkedListLoop{
    public static void main(String[] args) {

    }

    public boolean checkLoop(Node head) {

        Node first = head;
        Node second = head;

        while (first != null && first.next != null) {

            first = first.next.next;

            second = second.next;

            if (first == second) {
                return true;
            }
        }

        return false;
    }

    static class Node {
        int value;
        Node next;

        Node(int d) {
            value = d;
            next = null;
        }
    }
}
