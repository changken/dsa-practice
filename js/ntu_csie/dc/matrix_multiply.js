const { divideMatrix, addMatrix, combineMatrix } = require('./matrix_utils.js');

function MatrixMultiply(n, A, B) {
  // base case
  if (n == 1) {
    return [[A[0][0] * B[0][0]]];
    // recursive case
  } else {
    let mid = Math.floor(n / 2);
    // divide
    // O(1)
    let [A11, A12, A21, A22] = divideMatrix(A);
    let [B11, B12, B21, B22] = divideMatrix(B);
    console.log(A11, A12, A21, A22);
    // conquer and combine
    // 8T(n/2)
    let C11 = addMatrix(
      MatrixMultiply(mid, A11, B11),
      MatrixMultiply(mid, A12, B21)
    );
    let C12 = addMatrix(
      MatrixMultiply(mid, A11, B12),
      MatrixMultiply(mid, A12, B22)
    );
    let C21 = addMatrix(
      MatrixMultiply(mid, A21, B11),
      MatrixMultiply(mid, A22, B21)
    );
    let C22 = addMatrix(
      MatrixMultiply(mid, A21, B12),
      MatrixMultiply(mid, A22, B22)
    );
    // 4theta((n/2)^2)=theta(n^2)
    return combineMatrix(C11, C12, C21, C22);
  }
}

/*
let arrA = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
  [13, 14, 15, 16],
];

let arrB = [
  [2, 4, 6, 8],
  [10, 12, 14, 16],
  [18, 20, 22, 24],
  [26, 28, 30, 32],
];
*/

let A = [
  [1, 1, 1, 1],
  [2, 2, 2, 2],
  [3, 3, 3, 3],
  [2, 2, 2, 2],
];

let B = [
  [1, 1, 1, 1],
  [2, 2, 2, 2],
  [3, 3, 3, 3],
  [2, 2, 2, 2],
];

console.log(MatrixMultiply(4, A, B));
