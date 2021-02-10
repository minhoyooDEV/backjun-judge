// hashtable, clone
// 초기val에 대해서 단순 반복을 하며 복사를 하여 맵에 저장한다.
// 이후 정보에 대해서 한번더 순회를 하며 부족한 정보를 채워준다.

// Map을 쓸 생각을 하지 못했다. 임시 공간을 사용할 생각을 하였지만 맵까지 확장하여 생각하지 못했다.

/**
 * Definition for Node.
 * class Node {
 *     val: number
 *     next: Node | null
 *     random: Node | null
 *     constructor(val?: number, next?: Node, random?: Node) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *         this.random = (random===undefined ? null : random)
 *     }
 * }
 */
class Node2 {
  val: number;
  next: Node2 | null;
  random: Node2 | null;
  constructor(val?: number, next?: Node2, random?: Node2) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
    this.random = random === undefined ? null : random;
  }
}

function copyRandomList(head: Node2 | null): Node2 | null {
  if (!head) {
    return null;
  }

  const map = new Map();
  let cur:Node2 = null;

  cur = head;
  while (cur) {
    map.set(cur, new Node2(cur.val));
    cur = cur.next;
  }

  cur = head;
  while (cur) {
    map.get(cur).next = map.get(cur.next) || null;
    map.get(cur).random = map.get(cur.random) || null;
    cur = cur.next;
  }

  return map.get(head);
}
