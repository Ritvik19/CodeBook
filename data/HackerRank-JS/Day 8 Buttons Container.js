// js
var l = "4";
var a = ["1", "2", "3", "6", "9", "8", "7", "4"];
var b = ["1", "2", "3", "6", "9", "8", "7", "4"];

var rotate = function() {
    for (var i = 7; i > 0; i--) {
        a[i] = a[i - 1];
    }

    a[0] = l;
    l = a[7];

    for (var i = 0; i < 8; i++) {
        document.getElementById("btn" + b[i]).innerText = a[i];
    }
}
//CSS
.btnContainer {
  width: 75%;
}

.btnContainer > .btnStyle {
  width: 30%;
  height: 48px;
  font-size: 24px;
}
//HTML
<!-- Enter your HTML code here -->
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Buttons Grid</title>
    </head>
    <body>
    <script src="js/buttonsGrid.js" type="text/javascript"></script>
    <link rel="stylesheet" href="css/buttonsGrid.css" type="text/css">

    <div id="btns" class="btnContainer">
        <button id="btn1" class="btnStyle">1</button>
        <button id="btn2" class="btnStyle">2</button>
        <button id="btn3" class="btnStyle">3</button>
        <button id="btn4" class="btnStyle">4</button>
        <button id="btn5" class="btnStyle" onClick="rotate()">5</button>
        <button id="btn6" class="btnStyle">6</button>
        <button id="btn7" class="btnStyle">7</button>
        <button id="btn8" class="btnStyle">8</button>
        <button id="btn9" class="btnStyle">9</button>
    </div>
    </body>
</html>
