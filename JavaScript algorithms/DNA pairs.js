//DNA pairs (CGC should returb (CG,GC,CG)
function pairElement(str) {
  var split = str.split("");
  var newArr = [];
  for (let i = 0; i < split.length; i++) {
    if (split[i] == "G") {
      newArr.push(["G", "C"]);
    }
    if (split[i] == "C") {
      newArr.push(["C", "G"]);
    }
    if (split[i] == "A") {
      newArr.push(["A", "T"]);
    }
    if (split[i] == "T") {
      newArr.push(["T", "A"]);
    }
  }
  return newArr;
}

pairElement("GCG");