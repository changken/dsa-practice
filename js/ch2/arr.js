let arr = ['harry', 'ron', 'snap'];

// for loop
for (let i = 0; i < arr.length; i++) {
  console.log(i, arr[i]);
}

// foreach
arr.forEach((person, index) => {
  console.log(index, person);
});
