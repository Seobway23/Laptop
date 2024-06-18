const readline = require("readline").createInterface({
    input: process.stdin,
    output: process.stdout
});
readline.question('', input => {
    const[coins, mx] = input.split(' ').map(Number);
    
    if (coins * 100 >= mx) {
        console.log("Yes");
    }
    else{
        console.log("No");
        
    readline.close();
    }
})