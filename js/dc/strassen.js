const {
  addMatrix,
  subtractMatrix,
  divideMatrix,
  combineMatrix,
} = require('./matrix_utils.js');

function Strassen(n, A, B) {
  // base case
  if (n == 1) {
    return [[A[0][0] * B[0][0]]];
    // recursive case
  } else {
    let mid = Math.floor(n / 2);
    // divide
    // O(1)
    let [a, b, c, d] = divideMatrix(A);
    let [e, f, g, h] = divideMatrix(B);
    // conquer
    // 7T(n/2) + theta((n/2)^2)
    let m1 = Strassen(mid, a, subtractMatrix(f, h));
    let m2 = Strassen(mid, addMatrix(a, b), h);
    let m3 = Strassen(mid, addMatrix(c, d), e);
    let m4 = Strassen(mid, d, subtractMatrix(g, e));
    let m5 = Strassen(mid, addMatrix(a, d), addMatrix(e, h));
    let m6 = Strassen(mid, subtractMatrix(b, d), addMatrix(g, h));
    let m7 = Strassen(mid, subtractMatrix(a, c), addMatrix(e, f));
    // combine
    let c11 = addMatrix(subtractMatrix(addMatrix(m5, m4), m2), m6);
    let c12 = addMatrix(m1, m2);
    let c21 = addMatrix(m3, m4);
    let c22 = subtractMatrix(subtractMatrix(addMatrix(m1, m5), m3), m7);
    return combineMatrix(c11, c12, c21, c22);
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
];*/

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

console.log(Strassen(4, A, B));
