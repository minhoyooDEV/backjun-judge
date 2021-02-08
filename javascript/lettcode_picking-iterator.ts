// This is the Iterator's API interface.
// You should not implement it, or speculate about its implementation
// class Iterator {
//   hasNext(): boolean {}

//   next(): number {}
// }


class PeekingIterator {
  iterator: Iterator;
  hasPeeked: boolean;
  peekedElement: number | undefined;
  

  constructor(iterator: Iterator) {
      this.iterator = iterator
  }

  peek(): number {
      if (!this.hasPeeked) {
          this.peekedElement = this.iterator.next();
          this.hasPeeked = true;
      }
      return this.peekedElement;
      
  }

  next(): number {
      if (!this.hasPeeked) {
          return this.iterator.next();
      }
      const result = this.peekedElement;
      this.hasPeeked = false;
      this.peekedElement = null;
      return result;
  }

  hasNext(): boolean {
     return this.hasPeeked || this.iterator.hasNext();
  }
}

/**
 * Your PeekingIterator object will be instantiated and called as such:
 * var obj = new PeekingIterator(iterator)
 * var param_1 = obj.peek()
 * var param_2 = obj.next()
 * var param_3 = obj.hasNext()
 */