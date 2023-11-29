// Set the current year in the 'date' element

let date=document.getElementById('date')
const d =new Date()
let year =d.getFullYear()
console.log(d.getFullYear());
date.innerHTML=year


