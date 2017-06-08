# 206. Reverse Linked List

翻转单链表

基本思路是从前往后用两个指针current、next遍历链表，经过的结点翻转其指向，并用第三个指针last始终指向上一个被反转的结点

最后返回current即为反转后链表的表头