'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function getLetter(s) {
    let letter;
    s = s[0];
    if (['a', 'e', 'i', 'o', 'u'].includes(s)) letter = 'A';
    else if (['b', 'c', 'd', 'f', 'g'].includes(s)) letter = 'B';
    else if (['h', 'j', 'k', 'l', 'm'].includes(s)) letter = 'C';
    else letter = 'D';
    return letter;
}


function main() {
    const s = readLine();

    console.log(getLetter(s));
}
