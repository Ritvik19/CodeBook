// js
var opr = "";

var screen = document.getElementById("res");
screen.innerHTML = "";

buttonClicked = function() {
    var e = window.event;
    var btn = e.target || e.srcElement;

    if (btn.id != "btnClr" && btn.id != "btnEql") {
        screen.innerHTML += btn.innerHTML;

        if (btn.id != "btn0" && btn.id != "btn1") {
            opr = btn.innerHTML;
        }
    } else if (btn.id == "btnEql") {
        var str = screen.innerHTML.split(opr);
        var op1 = str[0];
        var op2 = str[1];

        /* The double bitwise NOT ('~~') is a shortcut for Math.floor() */
        screen.innerHTML = (~~eval(parseInt(op1, 2) + opr + parseInt(op2, 2))).toString(2);

        opr = "";
    } else if (btn.id == "btnClr") {
        screen.innerHTML = "";
        opr = "";
    }
}
//CSS
#res {
    width: 81%;
    height: 48px;
    font-size: 20px;
    background: #d3d3d3;
    border: solid;
}

.btnContainer {
    width: 90%;
}

.btnContainer > .btnStyle1, .btnStyle2, .btnStyle3 {
    width: 22%;
    height: 36px;
    font-size: 18px;
}

.btnContainer > .btnStyle1 {
    background: lightgreen;
    color: brown;
}

.btnContainer > .btnStyle2 {
    background: darkgreen;
    color: white;
}

.btnContainer > .btnStyle3 {
    background: black;
    color: red;
}
//HTML
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="css/binaryCalculator.css" type="text/css">
    </head>

    <body>
        <div id="res"></div>
        <div id="btns" class="btnContainer">
            <button id="btn0" class="btnStyle1" onclick="buttonClicked(event)">0</button>
            <button id="btn1" class="btnStyle1" onclick="buttonClicked(event)">1</button>
            <button id="btnClr" class="btnStyle2" onclick="buttonClicked(event)">C</button>
            <button id="btnEql" class="btnStyle2" onclick="buttonClicked(event)">=</button>
            <button id="btnSum" class="btnStyle3" onclick="buttonClicked(event)">+</button>
            <button id="btnSub" class="btnStyle3" onclick="buttonClicked(event)">-</button>
            <button id="btnMul" class="btnStyle3" onclick="buttonClicked(event)">*</button>
            <button id="btnDiv" class="btnStyle3" onclick="buttonClicked(event)">/</button>
        </div>

        <script src="js/binaryCalculator.js" type="text/javascript"></script>
    </body>
</html>
