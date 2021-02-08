/**
 * // This is the Iterator's API interface.
 * // You should not implement it, or speculate about its implementation.
 * function Iterator() {
 *    @ return {number}
 *    this.next = function() { // return the next number of the iterator
 *       ...
 *    };
 *
 *    @return {boolean}
 *    this.hasNext = function() { // return true if it still has numbers
 *       ...
 *    };
 * };
 */

/**
 * @param {Iterator} iterator
 */
var PeekingIterator = function (iterator) {
  this.iterator = iterator;
};

/**
 * @return {number}
 */
PeekingIterator.prototype.peek = function () {
  return this.iterator[0];
};

/**
 * @return {number}
 */
PeekingIterator.prototype.next = function () {
  var value = this.iterator[0];
  this.iterator = this.iterator.substr(1, this.iterator.length - 1);
  return value;
};

/**
 * @return {boolean}
 */
PeekingIterator.prototype.hasNext = function () {
  if (this.iterator && this.iterator.length) {
    return true;
  }
  return false;
};

/**
 * Your PeekingIterator object will be instantiated and called as such:
 * var obj = new PeekingIterator(arr)
 * var param_1 = obj.peek()
 * var param_2 = obj.next()
 * var param_3 = obj.hasNext()
 */
var obj = new PeekingIterator([1, 2, 3]);
var param_1 = obj.peek();
console.log(param_1);
var param_2 = obj.next();
console.log(param_2);
var param_3 = obj.hasNext();
console.log(param_3);
