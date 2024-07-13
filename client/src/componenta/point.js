export function savePoint(arr) {
  localStorage.setItem("arrPoint",[]);

  localStorage.setItem("arrPoint", JSON.stringify(arr));
}
export function getPoint() {
  let arr = localStorage.getItem("arrPoint");
  return JSON.parse(arr);
}
export function saveAllPoint(arr) {
  let existingData;
  try {
    existingData = JSON.parse(localStorage.getItem("arrPointHistory"));
  } catch (error) {
    console.error("Error parsing existing data:", error);
    existingData = []; 
  }
  const updatedData = existingData.concat(arr);
  // const updatedData = [existingData, arr] ;

  localStorage.setItem("arrPointHistory", JSON.stringify(updatedData));
}

export function getAllPoint() {
  let arrPoint = localStorage.getItem("arrPointHistory");
  return JSON.parse(arrPoint);
}
