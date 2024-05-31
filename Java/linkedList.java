import java.util.*;

class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

public class linkedList {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Node head = null;
        Node tail = null;
        System.out.println("Enter elements one by one, -1 to finish.");
        int data = sc.nextInt();
        while (data != -1) {
            Node newNode = new Node(data);

            if (head == null) {
                head = newNode;
                tail = newNode;
            } else {
                tail.next = newNode;
                tail = newNode;
            }
            data = sc.nextInt();
        }

        printLinkedList(head);

        head = addelementatend(head,sc);

        System.out.println("Added element at end: ");
        printLinkedList(head);

        head = addelementatstart(head,sc);

        System.out.println("Added element at start: ");
        printLinkedList(head);

        sc.close();

    }

    public static void printLinkedList(Node head) {
        Node current = head;
        while (current != null) {
            System.out.println(current.data);
            current = current.next;
        }
    }

    public static Node addelementatend(Node head,Scanner sc) {

        System.out.print("Enter the value to be added at the end of the linked list: ");
        int newNode = sc.nextInt();

        Node newNode2 = new Node(newNode);

        if (head == null) {
            head = newNode2;
        } else {
            Node current = head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode2;

        }

        return head;

    }

    public static Node addelementatstart(Node head, Scanner sc) {

        System.out.print("Enter the element to be added at the beginnin of the linked list: ");

        int newNode = sc.nextInt();

        Node newNode2 = new Node(newNode);

        if (head == null) {
            head = newNode2;
        } else {
            newNode2.next = head;
            head = newNode2;

        }
        return head;
    }
}
