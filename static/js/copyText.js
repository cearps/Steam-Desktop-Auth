function copyCode(){
  var textToCopy = document.getElementById("authCode");
  textToCopy.select();
  document.execCommand("Copy")
}
