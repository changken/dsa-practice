function hanoi(n, src, dest, spare) {
  // base case
  if (n == 1) {
    console.log(`move disk from ${src} to ${dest}`);
    // recursive case
  } else {
    hanoi(n - 1, src, spare, dest); // n-1 disks from src to spare using dest
    console.log(`move disk from ${src} to ${dest}`);
    hanoi(n - 1, spare, dest, src); // n-1 disks from spare to dest using src
  }
}

hanoi(1, 'A', 'C', 'B');
console.log('\n');
hanoi(2, 'A', 'C', 'B');
console.log('\n');
hanoi(3, 'A', 'C', 'B');
