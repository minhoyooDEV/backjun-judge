// int con = 2, count = S.length()-1, sum = 0;
// int oneCount = 0;
// for(char ele:S.toCharArray()){
//     int eleNumber = Character.getNumericValue(ele);
//     sum+=eleNumber*Math.pow(con, count--);
//     if(eleNumber==1) oneCount++;
// }

// if(oneCount>400000) return 799999;

// int div = 2, cnt = 0;
// while(sum>0){
//     if(sum%div==0) {
//         sum = sum/div;
//         cnt++;
//     }else{
//         sum -= 1;
//         cnt++;
//     }
// }

// return cnt;

function solution(S) {
  // write your code in JavaScript (Node.js 8.9.4)

  const div = 2;
  let count = S.length - 1;

  let sum = S.split("").reduce(
    (prev, s) => prev + +s * Math.pow(div, count--),
    0
  );

  let cnt = 0;
  while (sum > 0) {
    if (sum % div === 0) {
      sum = sum / div;
      cnt++;
    } else {
      sum -= 1;
      cnt++;
    }
    if (cnt > 400000) return 799999;
  }

  return cnt;
}

solution("011100");
solution("111");
solution("1111010101111");
// "123456".split("").reduce((prev, v) => {
//   console.log(v);
// }, 0);
