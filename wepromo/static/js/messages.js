let loc=window.location
let wsStart='ws://'
if(loc.protocol==='https'){
    wsStart='wss://'
}
print("right");
print(window.location.host);
let endpoint='ws://127.0.0.1:8000/';
console.log(endpoint)
var socket=new WebSocket(endpoint)
socket.onopen = function (e) {
    console.log("The connection was setup successfully !");
    socket.send("hello we are here");
  };

  socket.onmessage=function(e){
    console.log("message received from client",e);
  }
  socket.onclose=function(e){
    console.error("the connection closed unexpected");
  }
  document.querySelector("#id_message_send_input").focus();
  document.querySelector("#id_message_send_input").onkeyup = function (e) {
    if (e.keyCode == 13) {
      document.querySelector("#id_message_send_button").click();
    }
  };
  document.querySelector("#id_message_send_button").onclick = function (e) {
    var messageInput = document.querySelector(
      "#id_message_send_input"
    ).value;
    chatSocket.send(JSON.stringify({ message: messageInput, username : "{{request.user.username}}"}));
  };
 
