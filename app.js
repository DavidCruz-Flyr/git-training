import { readFileSync, writeFileSync } from "fs";

const data = readFileSync("./data.txt", "utf8").split("\n");

let suma= 0;
let promedio=0;

for (let num of data) {
    console.log(num);
    suma = suma + parseInt(num);
}

promedio = suma / data.length; 

console.log("La suma es " + suma);
console.log("Promedio " + Math.round(promedio));

if(data.length <= 1000)
{
    data.push(Math.round(promedio));
}
else{
    data[data.length-1] = Math.round(promedio);
}


writeFileSync("./data.txt",  data.join("\n"), "utf-8");
