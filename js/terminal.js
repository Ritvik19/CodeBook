function copyToClipboard(containerid) {
    var el = document.getElementById(containerid);
    var range = document.createRange();
    range.selectNodeContents(el);
    var sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(range);
    document.execCommand('copy');
    return false;
}

function copyStringToClipboard(str) {
    var el = document.createElement('textarea');
    el.value = str;
    el.setAttribute('readonly', '');
    el.style = { position: 'absolute', left: '-9999px' };
    document.body.appendChild(el);
    el.select();
    document.execCommand('copy');
    document.body.removeChild(el);
}

$('#command').keyup(function(e) {
    if (e.keyCode === 13) {
        command = this.value.toLowerCase();
        $('#terminal')[0].innerHTML += '<br>$ ' + command
        if (command == 'copy') {
            copyToClipboard('code')
            $('#terminal')[0].innerHTML += '<br>code copied'
        } else if (command == 'download') {
            window.open('../data/' + P + '/' + Q + '.' + E)
            $('#terminal')[0].innerHTML += '<br>downloaded'
        } else if (command == 'exit') {
            window.open('/', '_self')
        } else if (command == 'share') {
            copyStringToClipboard(window.location.href);
            $('#terminal')[0].innerHTML += '<br>URL copied to clipboard'
        } else {
            $('#terminal')[0].innerHTML += '<br>command not found'
        }
        this.value = ''
    }
});

function loadCode(p, q, e) {
    document.getElementById('title').innerHTML = p + " - " + q + "." + e;
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
var P = decodeURIComponent(params.get('p'))
var Q = decodeURIComponent(params.get('q'))
var E = decodeURIComponent(params.get('e'))
if (P != null && Q != null && E != null) {
    loadCode(P, Q, E);
}