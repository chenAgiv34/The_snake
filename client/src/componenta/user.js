export function User(mail, password) {
  this.mail = mail;
  this.password = password;
}
export function saveUser(user) {
  localStorage.setItem("currentUser", JSON.stringify(user));
}

export function getUser() {
  let user = localStorage.getItem("currentUser");
  return JSON.parse(user);
}
// export function removeUser() {
//   localStorage.removeItem("currentUser");
// }
// export function saveAllUser(arrUser) {
//   localStorage.setItem("arrAllUser", JSON.stringify(arrUser));
// }

// export function getAllUser() {
//   let arrUser = localStorage.getItem("arrAllUser");
//   return JSON.parse(arrUser);
// }
// export function removeAllUser() {
//   localStorage.removeItem("arrAllUser");
// }
