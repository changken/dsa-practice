function champion_2(A, i, j) {
  // base case
  if (i == j) {
    return i;
    // recursive case
  } else {
    k = Math.floor((i + j) / 2);
    if (A[k] > A[k + 1]) {
      return champion_2(A, i, k);
    }
    if (A[k] < A[k + 1]) {
      return champion_2(A, k + 1, j);
    }
  }
}
list = [3, 7, 9, 17, 35, 28, 21, 18, 6, 4];
i = champion_2(list, 0, list.length - 1);
console.log(list[i]);
