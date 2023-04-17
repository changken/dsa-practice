// please refer to the code which is in the sort folder
function MergeSort(arr) {
  //base case
  if (arr.length == 1) return arr;
  //recursive case
  //divide
  let mid = Math.floor(arr.length / 2);
  // conquer
  //combine
  return Merge(MergeSort(arr.slice(0, mid)), MergeSort(arr.slice(mid)));
}

function Merge(L, R) {
  let res = [];
  while (L.length && R.length) {
    if (L[0] < R[0]) {
      res.push(L.shift());
    } else {
      res.push(R.shift());
    }
  }
  return res.concat(L, R);
}

list = [3, 7, 9, 17, 35, 28, 21, 18, 6, 4];

console.log(MergeSort(list));
