//return true if arr[0] contains all elements of arr[1]
function mutation(arr) {
  let str2 = arr[1].toLowerCase().split("");

  for (let i = 0; i < str2.length; i++) {
    if (arr[0].includes(str2[i])) {
      return true;
    } else return false;
  }
}

mutation(["hello", "hey"]);