function divideMatrix(mid, arr) {
  let a1 = arr.slice(0, mid);
  let a2 = arr.slice(mid);
  let a11 = a1.map(i => i.slice(0, mid));
  let a12 = a1.map(i => i.slice(mid));
  let a21 = a2.map(i => i.slice(0, mid));
  let a22 = a2.map(i => i.slice(mid));
  return [a11, a12, a21, a22];
}

function addMatrix(n, A, B) {
  if (n == 1) {
    return A + B;
  } else {
    let C = [];
    for (let i = 0; i < n; i++) {
      C.push([]);
      for (let j = 0; j < n; j++) {
        C[i].push(A[i][j] + B[i][j]);
      }
    }
    return C;
  }
}

function CombineMatrix(n, mid, C11, C12, C21, C22) {
  let C = [];

  console.log('n, mid: ', n, mid);

  if (mid == 1) {
    C = [
      [C11, C12],
      [C21, C22],
    ];
  } else {
    for (let i = 0; i < n; i++) {
      C.push([]);
      for (let j = 0; j < n; j++) {
        console.log('i, j: ', i, j);
        if (i < mid && j < mid) {
          C[i].push(C11[i][j]);
        } else if (i >= mid && j < mid) {
          C[i].push(C21[i - mid][j]);
        } else if (i < mid && j >= mid) {
          C[i].push(C12[i][j - mid]);
        } else if (i >= mid && j >= mid) {
          C[i].push(C22[i - mid][j - mid]);
        }
      }
    }
  }
  return C;
}

function MatrixMultiply(n, A, B) {
  // base case
  if (n == 1) {
    return A[0][0] * B[0][0];
    // recursive case
  } else {
    let mid = Math.floor(n / 2);
    // divide
    // O(1)
    let [A11, A12, A21, A22] = divideMatrix(mid, A);
    let [B11, B12, B21, B22] = divideMatrix(mid, B);
    console.log(A11, A12, A21, A22);
    // conquer and combine
    // 8T(n/2)
    let C11 = addMatrix(
      mid,
      MatrixMultiply(mid, A11, B11),
      MatrixMultiply(mid, A12, B21)
    );
    let C12 = addMatrix(
      mid,
      MatrixMultiply(mid, A11, B12),
      MatrixMultiply(mid, A12, B22)
    );
    let C21 = addMatrix(
      mid,
      MatrixMultiply(mid, A21, B11),
      MatrixMultiply(mid, A22, B21)
    );
    let C22 = addMatrix(
      mid,
      MatrixMultiply(mid, A21, B12),
      MatrixMultiply(mid, A22, B22)
    );
    // 4theta((n/2)^2)=theta(n^2)
    return CombineMatrix(n, mid, C11, C12, C21, C22);
  }
}

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

console.log(MatrixMultiply(4, arrA, arrB));
