
/* Structure of LinkedList
class Node
{
	int data;
	Node next;
	Node(int d)
	{
		data = d;
		next = null;
	}
}
*/
class GfG
{
    boolean isCircular(Node head)
    {
        Node Traveller = head.next;
        
        while (Traveller != null){
            if(Traveller == head){
                return true;
            }
            Traveller = Traveller.next;
        }
        return false;
    }
} 
// Question link: https://www.geeksforgeeks.org/problems/circular-linked-list/1
