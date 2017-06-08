package leetcode_206;

//Definition for singly-linked list.
class ListNode {
     int val;
     ListNode next;
     ListNode(int x) { val = x; }
}

public class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode current = head;
        ListNode last = null;
        while(current != null){
            ListNode next = current.next;
            current.next = last;
            last = current;
            current = next;
        }
        return last;
    }
    
    public static void main(String[] args){
    	// do sth.
    }
}