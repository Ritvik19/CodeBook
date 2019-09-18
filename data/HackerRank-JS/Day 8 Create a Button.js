// js
function increment()
{
    document.getElementById('btn').innerHTML = Number(document.getElementById('btn').innerHTML) + 1;
}
//CSS
#btn{
    width: 96px;
    height: 48px;
    font-size: 24px;
}
//HTML
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Button</title>
        <link rel="stylesheet" href="css/button.css" type="text/css">
    </head>
    <body>
        <button type="button" id="btn" onclick="increment()">0</button>
       <script src="js/button.js" type="text/javascript"></script>
    </body>
</html>
