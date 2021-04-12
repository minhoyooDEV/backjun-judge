// function generateNewFolderName(existingFolders) {
//   // Write your code here
//   if (!existingFolders.length) {
//     return "New Folder"
//   }

//   let max = 1
//   for (const name of existingFolders) {
//     const find = name.match(/\((.*)\)/)
//     if (find) {
//       max = Math.max(find.pop(), max)
//     }
//   }

//   return `New Folder (${max})`
// }

// console.log(generateNewFolderName(["New Folder"]));


function numberOfItems(arr, item) {
  // Write the code that goes here
  for (const data of arr) {
    if (data === item)
  }
  if (Array.isArray(arr)) {
    return numberOfItems(arr, item)
  }
}

var arr = [
  25,
  "apple",
  ["banana", "strawberry", "apple", 25]
];
console.log(numberOfItems(arr, 25));
console.log(numberOfItems(arr, "apple"));