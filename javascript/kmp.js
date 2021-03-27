/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function (haystack, needle) {
  if (!needle) {
    return 0;
  }
  const table = kmp(needle);
  const haystackSize = haystack.length;
  const needleSize = needle.length;

  let j = 0;
  for (let i = 0; i < haystackSize; i++) {
    while (j > 0 && haystack[i] != needle[j]) {
      j = table[j - 1];
    }

    if (haystack[i] == needle[j]) {
      if (j == needleSize - 1) {
        return i - needleSize + 1;
      } else {
        j++;
      }
    }
  }
  return -1;
};

function kmp(pattern) {
  const size = pattern.length;
  const table = Array(size).fill(0);

  let j = 0;
  for (let i = 1; i < size; i++) {
    while (j > 0 && pattern[i] != pattern[j]) {
      j = table[j - 1];
    }
    if (pattern[i] == pattern[j]) {
      table[i] = ++j;
    }
  }
  console.log("table", table);
  return table;
}
