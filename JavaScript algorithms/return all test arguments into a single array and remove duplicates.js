//return all test arguments into a single array and remove duplicates
function uniteUnique(...ar) {
  ar.flat();
  var newArr = [].concat(...ar);
  var uniq = [...new Set(newArr)];
  return uniq;
}

uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1]);