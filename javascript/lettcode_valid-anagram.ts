// 해당 문자열을 정렬하지않고 판단을 할 공간을 만든 후 값을 조정하여 확인
// O(n)의 복잡도로 풀수있다.

function isAnagram(s: string, t: string): boolean {
  const a = s.split('').sort().join('')
  const b = t.split('').sort().join('')
  return a === b
};

// function isAnagram(s: string, t: string): boolean {
//   const alphabets:number[] = new Array(26).fill(0);

//   if (s.length != t.length)
//       return false;

//   for (let i = 0; i < s.length; i++) {
//       // console.log(`s.charCodeAt(i): ${s.charCodeAt(i)-97}`);
//       alphabets[s.charCodeAt(i)-97]++;
//   }

//   for (let i = 0; i < t.length; i++) {
//       // console.log(`t.charCodeAt(i): ${t.charCodeAt(i)-97}`);
//       alphabets[t.charCodeAt(i)-97]--;
//   }

//   for (let i = 0; i < 26; i++) {
//       // console.log(`alphabets[i]: ${alphabets[i]}`);
//       if (alphabets[i] > 0)
//           return false;
//   }

//   return true;

// };