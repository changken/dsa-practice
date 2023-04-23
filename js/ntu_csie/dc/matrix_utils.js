function divideMatrix(arr) {
  /*
  let a1 = arr.slice(0, mid);
  let a2 = arr.slice(mid);
  let a11 = a1.map(i => i.slice(0, mid));
  let a12 = a1.map(i => i.slice(mid));
  let a21 = a2.map(i => i.slice(0, mid));
  let a22 = a2.map(i => i.slice(mid));
  return [a11, a12, a21, a22];
  */
  let row = arr.length;
  let col = arr[0].length;
  let row_mid = Math.floor(row / 2);
  let col_mid = Math.floor(col / 2);
  let a11 = arr.slice(0, row_mid).map(i => i.slice(0, col_mid));
  let a12 = arr.slice(0, row_mid).map(i => i.slice(col_mid));
  let a21 = arr.slice(row_mid).map(i => i.slice(0, col_mid));
  let a22 = arr.slice(row_mid).map(i => i.slice(col_mid));
  return [a11, a12, a21, a22];
}

function addMatrix(A, B) {
  /*
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
  }*/
  return A.map((x, i) => x.map((y, j) => y + B[i][j]));
}

function subtractMatrix(A, B) {
  /*
  if (n == 1) {
    return A - B;
  } else {
    let C = [];
    for (let i = 0; i < n; i++) {
      C.push([]);
      for (let j = 0; j < n; j++) {
        C[i].push(A[i][j] - B[i][j]);
      }
    }
    return C;
  }*/
  return A.map((x, i) => x.map((y, j) => y - B[i][j]));
}

function combineMatrix(C11, C12, C21, C22) {
  /*
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
  */
  let top = C11.map((x, i) => x.concat(C12[i]));
  let bottom = C21.map((x, i) => x.concat(C22[i]));
  return top.concat(bottom);
}

module.exports = {
  divideMatrix: divideMatrix,
  addMatrix: addMatrix,
  subtractMatrix: subtractMatrix,
  combineMatrix: combineMatrix,
};
