import { readFileSync, writeFileSync } from "fs";

const data = readFileSync("./data.txt", "utf8").split("\n");

for (let num of data) {
    console.log(num);
}

writeFileSync("./data.txt", data.join("\n"), "utf-8");
