function MaxCrossSubarray(A, i, k, j) {
  let left_sum = 99999999 * -1;
  let sum = 0;
  let max_left;
  // O(k-i+1)
  for (let p = k; p >= i; p--) {
    sum += A[p];
    if (left_sum < sum) {
      left_sum = sum;
      max_left = p;
    }
  }

  let right_sum = 99999999 * -1;
  sum = 0;
  let max_right;
  // O(j-k)
  for (let q = k + 1; q <= j; q++) {
    sum += A[q];
    if (right_sum < sum) {
      right_sum = sum;
      max_right = q;
    }
  }

  return [max_left, max_right, left_sum + right_sum];
}

function MaxSubarray(A, i, j) {
  // base case
  if (i == j) {
    //O(1)
    console.log(i, j, A[i]);
    return [i, j, A[i]];
    //recursive case
  } else {
    let k = Math.floor((i + j) / 2);
    // divide and conquer
    let [left_low, left_high, left_sum] = MaxSubarray(A, i, k); //T(k-i+1)
    let [right_low, right_high, right_sum] = MaxSubarray(A, k + 1, j); //T(j-k)
    let [cross_low, cross_high, cross_sum] = MaxCrossSubarray(A, i, k, j); //O(j-i+1)

    //combine
    if (left_sum >= right_sum && left_sum >= cross_sum) {
      //O(1)
      console.log(left_low, left_high, left_sum);
      return [left_low, left_high, left_sum]; // case 1
    } else if (right_sum >= left_sum && right_sum >= cross_sum) {
      //O(1)
      console.log(right_low, right_high, right_sum);
      return [right_low, right_high, right_sum]; // case 2
    } else {
      //O(1)
      console.log(cross_low, cross_high, cross_sum);
      return [cross_low, cross_high, cross_sum]; // case 3
    }
  }
}

let list = [3, 7, 9, 17, 5, 28, 21, 18, 6, 4];
console.log(MaxSubarray(list, 0, list.length - 1));
