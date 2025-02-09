// alert("I'm external file JS");
// let admin;
// let name = "John";
// admin = name;
// alert(admin);
//
// let planet = "Earth";
// let user = "User Name";
//
//
// const BIRTHDAY = '18.04.1982';
// const AGE = someCode(BIRTHDAY);
//
//
// alert(`hello ${name}`);
// alert(`hello ${"name"}`);
// alert(`hello ${1}`);


// let name1 = prompt("Your name?", "");
// alert(`Hello ${name1}`);


// let a = 1, b = 1;
// let c = ++a;
// let d = b++;
// alert(c);
// alert(d);


// let a = 2;
// let x = 1 + (a*=2); //a = 4, x = 5



// "" + 1 + 0 = "10"
// "" - 1 + 0 = -1
// true + false = 1
// 6 / "3" = 2
// "2" * "3" = 6
// 4 + 5 + "px" = "9px"
// "$" + 4 + 5 = "$45"
// "4" - 2 = 2
// "4px" - 2 = NaN
// "  -9  " + 5 = "  -9  5"
// "  -9  " - 5 = -14
// null + 1 = 1
// undefined + 1 = NaN
// " \t \n" - 2 = 0 -2 = -2


// let a = prompt("First number?", 1);
// let b = prompt("Second number?", 2);
//
// alert(Number(a) + Number(b)); // 12

// alert(2>1);

// 5 > 4 = true
// "apple" > "pineapple" = false
// "2" > "12" = true
// undefined == null = true
// undefined === null = false
// null == "\n0\n" = false
// null === +"\n0\n" = false

// if ("0") {
//     alert( 'Hello' ); alert is shown
// }


// let origName = prompt('What is the "official" name of JS?');
// if (origName === "ECMAScript"){
//     alert('right');
// }
// else{
//     alert('You don’t know? ECMAScript!');
// }



// let input = prompt("Give a number");
// if(input > 0){
//     alert(1);
// }
// else if (input < 0){
//     alert(-1);
// }
// else{
//     alert(0);
// }



// let result;
//
// if (a + b < 4) {
//     result = 'Below';
// } else {
//     result = 'Over';
// }



// let result = (a+b < 4) ? "Below" : "Over";

// let message;
//
// if (login == 'Employee') {
//     message = 'Hello';
// } else if (login == 'Director') {
//     message = 'Greetings';
// } else if (login == '') {
//     message = 'No login';
// } else {
//     message = '';
// }
// can be written like:

// let message = (login == 'Employee') ? 'Hello' :
//     (login = 'Director') ? 'Greetings' :
//         (login = '') ? 'No login' : '';



// alert( null || 2 || undefined );
//returns 2

// alert( alert(1) || 2 || alert(3) );
//shows 1, then returns 2

// alert( 1 && null && 2 );
//returns null

// alert( alert(1) && alert(2) );
//shows 1, then returns undefined

// alert( null || 2 && 3 || 4 );
//returns 3


// let age = prompt("Enter your age");
// if (age >= 14 && age <= 90){
//     alter('ok');
// }
// else{
//     alter('outside of range');
// }


// if (!(age >= 14 && age <= 90));
// if (age < 14 || age > 90);

// if (-1 || 0) alert( 'first' );
// if (-1 && 0) alert( 'second' );
// if (null || -1 && 1) alert( 'third' );  1st and 3rd will run

// let name = prompt('Who\'s there?', '');
// if (name == 'Admin'){
//     let password = prompt('Password?', '')
//         if (password == 'correctPassword'){
//             alert('Welcome');
//         }
//         else if (password == null){
//             alert('Cancelled');
//         }
//         else{
//             alert('Wrong Password');
//         }
// }
// else if (name == null){
//     alert('Cancelled');
// }
// else{
//     alert('I don\'t know you');
// }

// let i = 3;
//
// while (i) {
//     alert( i-- );
// }
//1 is last alerted number


// let i = 0;
// while (++i < 5) alert( i ); 1 2 3 4

// let i = 0;
// while (i++ < 5) alert( i ); 1 2 3 4 5

// for (let i = 0; i < 5; i++) alert( i ); 0 1 2 3 4
//for (let i = 0; i < 5; ++i) alert( i ); 0 1 2 3 4

// for(let i = 2; i <= 10; i += 2){
//     alert(i);
// }

// for (let i = 0; i < 3; i++) {
//     alert( `number ${i}!` );
// }
//
// let i = 0;
// while(i < 3){
//     alert(`number ${i}!`);
//     i++;
// }

// let i = prompt("Input number: ", '');
// while(i <= 100){
//     i = prompt("Try again (greater than 100): ", '');
//     if(i == null) break;
// }

let n = prompt("Enter a number");
let isPrime = true;
for(let i = 1; i < n; i++){
    if(!(n % i)) {
        isPrime = false;
        alert(isPrime);
        break;
    }
}
if(isPrime == true){
    alert(isPrime);
}