document.getElementById("call").onclick = function() {callFunction()};
document.getElementById("chat").onclick = function() {chatFunction()};
document.getElementById("websites").onclick = function() {websitesFunction()};


function callFunction() {
  document.getElementById("call_dropdown").classList.toggle("show");
}
function chatFunction() {
  document.getElementById("chat_dropdown").classList.toggle("show");
}
function websitesFunction() {
  document.getElementById("websites_dropdown").classList.toggle("show");
}