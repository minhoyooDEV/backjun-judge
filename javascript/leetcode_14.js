var longestCommonPrefix = function (strs) {
  let result = (minStr = strs.sort((a, b) => b.length - a.length)[0]);

  while (result && result.length) {
    let resultSize = result.length;

    let allPass = true;
    for (const s of strs) {
      if (s.substr(0, resultSize) != result) {
        result = result.substr(0, result.length - 1);
        allPass = false;
        break;
      }
    }
    if (allPass) {
      return result;
    }
  }

  return "";
};
