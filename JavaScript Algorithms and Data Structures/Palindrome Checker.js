function stringWithAlphaNumeric(str) {
  return str.replace(/[^a-z0-9]/ig, "");
}

function stringLowerCased(str) {
  return str.toLowerCase();
}

const stringReversed = (str) => {
  let result = "";
  for (let i = str.length-1; i >= 0; i--) {
    result += str[i];
  };
  return result
};

console.log(stringReversed("Hello, world"))

function palindrome(str) {
  const cleanedUpStr = stringWithAlphaNumeric(str);
  const lowerCaseStr = stringLowerCased(cleanedUpStr);
  const reversedStr = stringReversed(lowerCaseStr);
  return lowerCaseStr == reversedStr;
}

palindrome("eye"); 
