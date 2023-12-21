	let endpoint='ws://127.0.0.1:8000/';
	var socket=new WebSocket(endpoint)
	socket.onopen = function (e) {
		console.log("The connection was setup successfully !");
		console.log(e);


	};
	
	
	socket.onmessage=function(e){
		console.log("yes")
		const data=JSON.parse(e.data);
		console.log(data.message); 
		const outer=document.createElement("div");
			const node = document.createElement("button");
			node.className="btn btn-primary";
           const textnode = document.createTextNode(data.message);
            node.appendChild(textnode);
			outer.appendChild(node);
			outer.style.width="5%";
			outer.style.marginTop="4%";
			outer.style.marginRight="0%";
			document.getElementById("in-chat-Vlogging").appendChild(outer);
	};
	  socket.onclose=function(e){
		console.error("the connection closed unexpected",e);
	};
function setReceiver(parameter) {
	if(parameter=='Gaming'){
	  document.getElementById('chat_head').innerText="Gaming";
	  document.getElementById('chatbox-Gaming').style.display="block";
	  document.getElementById('chatbox-Vlogging').style.display="None";
	  document.getElementById('chatbox-Cooking').style.display="None";
	  document.getElementById('chatbox-Challenges').style.display="None";
	} 
	else if(parameter=='Vlogging'){
		document.getElementById('chat_head').innerText="Vlogging";
		document.getElementById('chatbox-Gaming').style.display="None";
	  document.getElementById('chatbox-Vlogging').style.display="block";
	  document.getElementById('chatbox-Cooking').style.display="None";
	  document.getElementById('chatbox-Challenges').style.display="None";
	}
	else if(parameter=='Cooking'){
		document.getElementById('chat_head').innerText="Cooking";
		document.getElementById('chatbox-Gaming').style.display="None";
	  document.getElementById('chatbox-Vlogging').style.display="None";
	  document.getElementById('chatbox-Cooking').style.display="block";
	  document.getElementById('chatbox-Challenges').style.display="None";
	}
	else{
		document.getElementById('chat_head').innerText="Challenges";
		document.getElementById('chatbox-Gaming').style.display="None";
	  document.getElementById('chatbox-Vlogging').style.display="None";
	  document.getElementById('chatbox-Cooking').style.display="None";
	  document.getElementById('chatbox-Challenges').style.display="block";
	}

	}
	document.getElementById('game-send').onclick=
	function (event){
		const messageInputDom =document.getElementById
		('game-text-input')
		const username=document.getElementById
		('user_check').value
		print(username);
		const message=messageInputDom.value
		socket.send(JSON.stringify({
     'msg':message,
	 //'user':username,
		}))
		messageInputDom.value="";
	}