$(document).ready(function(){
  $('#solution')[0].innerHTML = "<p># Your Code Appears Here<br>print('Hello, World!')</p>";
  $('#pc').keypress(function(event){
    var keycode = (event.keyCode ? event.keyCode : event.which);
    if(keycode == '13'){
        loadSolution();
    }
});
});

function loadSolution() {
  var problemcode = $('#pc')[0].value;
  problemcode = problemcode.toUpperCase();
  $.getJSON('https://api.allorigins.ml/get?url=' + encodeURIComponent('https://github.com/Ritvik19/CodeChef_Practice/blob/master/'+problemcode+'.py') + '&callback=?', function(data, status)
  {
    console.log(status);
    console.log(data.contents.length);
    fetched_data = data.contents;
    var beg = fetched_data.search(/<table/);
    var end = fetched_data.search(/<\/table/);
    fetched_table = fetched_data.substring(beg, end+8);
    if (fetched_table.length > 7)
    {
      $('#solution')[0].innerHTML = fetched_table;
    }
    else
    {
        $('#solution')[0].innerHTML = '<p>Solution Could Not Be Found!!!<p>';
    }
  });
}

var clipboard = new ClipboardJS('.copy-button');

function snackbarDisplay() {
  // Get the snackbar DIV
  var x = document.getElementById("snackbar");

  // Add the "show" class to DIV
  x.className = "show";

  // After 3 seconds, remove the show class from DIV
  setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}
