//insert num in sorted array in order
function getIndexToIns(arr, num) {
  let sorted = arr.sort();
  let counter = 0;
  for (let i = 0; i < sorted.length; i++) {
    if (num > sorted[i]) {
      counter++;
    }
  }
  return counter;
}

getIndexToIns([40, 60], 50);