//Palindrome
function palindrome(str) {
  str = str.replace(/[^A-Za-z0-9]/g, "").toLowerCase();
  let reversed = str.split("").reverse().join("");
  if (str == reversed) {
    return true;
  }
  return false;
}

palindrome("A man, a plan, a canal. Panama");