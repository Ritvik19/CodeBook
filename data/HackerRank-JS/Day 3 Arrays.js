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

/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
    // Complete the function
    let biggest = 0, next_biggest = 0;

    for (var i = 0, n = nums.length; i < n; ++i) {
        var nr = +nums[i]; // convert to number first

        if (nr > biggest) {
            next_biggest = biggest; // save previous biggest value
            biggest = nr;
        } else if (nr < biggest && nr > next_biggest) {
            next_biggest = nr; // new second biggest value
        }
    }
    return (next_biggest)
}


function main() {
    const n = +(readLine());
    const nums = readLine().split(' ').map(Number);

    console.log(getSecondLargest(nums));
}
