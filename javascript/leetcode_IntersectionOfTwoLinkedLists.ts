// Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}


function getIntersectionNode(headA: ListNode | null, headB: ListNode | null): ListNode | null {
    if (!headA || !headB) {
        return null
    }
    let aLength = 0
    let a = headA
    while (a) {
        a = a.next;
        aLength++;
    }
    
    let bLength = 0
    let b = headB
    while (b) {
        b = b.next;
        bLength++;
    }
    
    a = headA;
    b = headB;
    if (bLength > aLength) {
        for (let i = 0; i < Math.abs(bLength - aLength); i++) {
            b = b.next
        }
    } else if (aLength > bLength) {
        for (let i = 0; i < Math.abs(bLength - aLength); i++) {
            a = a.next
        }
    }
    let answer = null
    while (a) {

        if(a === b) {
            answer = a
            break;
        }
        a = a.next;
        b = b.next;
    }
    
    return a
};


// function getIntersectionNode(headA: ListNode | null, headB: ListNode | null): ListNode | null {
    // 공간 복잡도가 1이다 라기엔 뭐지....
//     let set = new Set();
    
//     while (headA !== null) {
//         set.add(headA);
//         headA = headA.next;
//     }
    
//     while (headB !== null) {
//         if (set.has(headB)) return headB;
//         headB = headB.next;
//     }
    
//     return null; 
// };

// function getIntersectionNode(headA: ListNode | null, headB: ListNode | null): ListNode | null {
//     if (headA === null || headB === null) {
//         return null;
//     }
    
//     let pointerA = headA;
//     let pointerB = headB;
    
//     while (pointerA !== pointerB) {        
//         pointerA = pointerA.next;
//         pointerB = pointerB.next;
        
//         if (pointerA === pointerB) {
//             return pointerA;
//         }
        
//         if (pointerA === null) {
//             pointerA = headB;
//         }
        
//         if (pointerB === null) {
//             pointerB = headA;
//         }
//     }
    
//     return pointerA;
// };