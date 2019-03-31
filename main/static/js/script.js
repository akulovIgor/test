var kinput = document.getElementById('kinput');
var area = document.getElementById('area');
var last_text;
kinput.onkeypress = handle;

function handle(e) {

  var text = String.fromCharCode(e.charCode);

  if(e.keyCode == 8 || e.keyCode == 46){
  area.value -= last_text;
  }
  area.value += text;
  last_text = text;
  area.scrollTop = area.scrollHeight;
  /*  if (form.elements[e.type + 'Stop'].checked) {
    e.preventDefault();
  }*/

}