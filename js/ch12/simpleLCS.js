function simpleLCS(str1, str2) {
  // base case
  if (str1.length == 0 || str2.length == 0) {
    return 0;
    //recursive case
  } else {
    if (str1[str1.length - 1] == str2[str2.length - 1]) {
      return 1 + simpleLCS(str1.slice(0, -1), str2.slice(0, -1));
    } else {
      return Math.max(
        simpleLCS(str1.slice(0, -1), str2),
        simpleLCS(str1, str2.slice(0, -1))
      );
    }
  }
}

console.log(simpleLCS('AGGTG', 'ATTGC'));
