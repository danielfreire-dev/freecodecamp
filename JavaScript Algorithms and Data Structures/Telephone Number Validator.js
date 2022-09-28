const RE = /^1?\s?\d{3}-\d{3}-\d{4}$/
const RE2 = /^1?\s?\(\d{3}\)\d{3}-\d{4}$/
const RE3 = /^1?\s?\(\d{3}\)\s\d{3}-\d{4}$/
const RE4 = /^1?\s?\d{3}\s\d{3}\s\d{4}$/
const RE5 = /^1?\s?\d{10}$/

function telephoneCheck(str) {
  return RE.test(str) || RE2.test(str) || RE3.test(str) || RE4.test(str) || RE5.test(str);
}
/**
console.log(telephoneCheck("555-555-5555"));
console.log(telephoneCheck("(555)555-5555"));
console.log(telephoneCheck("(555) 555-5555"));
console.log(telephoneCheck("555 555 5555"));console.log(telephoneCheck("5555555555"));console.log(telephoneCheck("1 555 555 5555"));
console.log(telephoneCheck("2 (757) 622-7382"));
*/