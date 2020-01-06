function CopyToClipboard(containerid) {
    var el = document.getElementById(containerid);
    var range = document.createRange();
    range.selectNodeContents(el);
    var sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(range);
    document.execCommand('copy');
    return false;
}

$('#command').keyup(function(e) {
    if (e.keyCode === 13) {
        command = this.value
        $('#terminal')[0].innerHTML += '<br>$ ' + command
        if (command == 'copy') {
            CopyToClipboard('code')
            $('#terminal')[0].innerHTML += '<br>copied'
        } else if (command == 'download') {
            window.open('../data/' + P + '/' + Q + '.' + E)
            $('#terminal')[0].innerHTML += '<br>downloaded'
        } else {
            $('#terminal')[0].innerHTML += '<br>command not found'
        }
        this.value = ''
    }
});

function loadCode(p, q, e) {
    document.getElementById('title').innerHTML = q + "." + e + " - " + p;
    var xhttp = new XMLHttpRequest();
    var filepath = '../data/' + p + '/' + q + '.' + e
    console.log(filepath)
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            code = this.responseText;
            code = code.replace(/</g, "&lt;")
            code = code.replace(/>/g, "&gt;")
            document.getElementById("code").innerHTML = code;
        }
    };
    xhttp.open("GET", filepath, true);
    xhttp.send();
}


var params = new URLSearchParams(location.search);
var P = params.get('p')
var Q = params.get('q')
var E = params.get('e')
if (P != null && Q != null && E != null) {
    loadCode(P, Q, E);
}