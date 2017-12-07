var ed = require('edit-distance');
var fs = require('fs');
var path = require('path');
filePath = path.join(__dirname, 'dic_city.txt');

/*Importar configuracoes do servidor*/
var app = require('./config/server');

var server = app.listen(3000, function() {
	// body...
	console.log("Server running");
});

function uintToString(uintArray) {
    var encodedString = String.fromCharCode.apply(null, uintArray),
        decodedString = decodeURIComponent(escape(encodedString));
    return decodedString;
}

var io = require('socket.io').listen(server);

var net = require('net');
var client = new net.Socket();

/* Criar a conexão por websocket */
io.on('connection', function(socket){
	console.log('User connected');
	client.connect(8484, '127.0.0.1', function() {
		console.log('Connected with python server');
		socket.on('disconnect',function(){
			console.log('User disconnected');
		});

		socket.on('msgParaServidor', function(data){
			

		    client.write('{"cidade": "'+data.mensagem+'"}');
		    client.on('data', function(rec) {
		    	console.log('Received: ' + rec);
		    	socket.emit(
					'msgParaCliente', 
					{mensagem : uintToString(rec).split("criscriscris")}
				);
			});

			// socket.emit(
			// 	'msgParaCliente', 
			// 	{mensagem : data.mensagem}
			// );
		});

		socket.on('buscaUnica', function(data){
	    	socket.emit(
				'erroBuscaUnica', 
				{mensagem : ["primeiro","segundo","terceiro"]}
			);
		});

		socket.on('buscaByCity', function(data){

			fs.readFile(filePath, {encoding: 'utf-8'}, function(err,buscaCity_data){
			    buscaCity_data = buscaCity_data.split("\n");
			    // console.log('received buscaCity_data: ' + buscaCity_data[1]);
			    var checking = true;
			    for(var i = 0; i<buscaCity_data.length;i++){
		            if(data.cidade.toLowerCase()==buscaCity_data[i].toLowerCase()){
		                checking = false;
		            }
		        }

		        if(checking){
				    var insert, remove, update;
				    insert = remove = function(node) { return 1; };
				    update = function(stringA, stringB) { return stringA !== stringB ? 1 : 0; };
				     
				    // Define two strings. 
				    // var stringA = "Recife";
				    var stringB = data.cidade;
				    // var stringB = "Recifs";
				     
				    // Compute edit distance, mapping, and alignment. 
				    // var lev = ed.levenshtein(stringA, stringB, insert, remove, update);
				    // console.log('Levenshtein', lev.distance, lev.pairs(), lev.alignment());

				    var three_word = []
				    for(var i = 0; i<buscaCity_data.length;i++){
				        var lev = ed.levenshtein(stringB.toLowerCase(), buscaCity_data[i].toLowerCase(), insert, remove, update);
				        if(three_word.length<3){
				            three_word.push(buscaCity_data[i]);
				        }
				        else{
				            for(var j = 0; j<three_word.length;j++){
				                var lev2 = ed.levenshtein(stringB.toLowerCase(), three_word[j].toLowerCase(), insert, remove, update);
				                if(lev.distance<lev2.distance){
				                    if(buscaCity_data[i]!=three_word[0] && buscaCity_data[i]!=three_word[1] && buscaCity_data[i]!=three_word[2]){
				                        three_word.splice(j,1);
				                        three_word.push(buscaCity_data[i]);
				                    }
				                }
				            }
				        }
				    }
				    three_word.sort(function (A,B){
				        var insert, remove, update;
				        insert = remove = function(node) { return 1; };
				        update = function(stringA, stringB) { return stringA !== stringB ? 1 : 0; };
				        var lev = ed.levenshtein(A.toLowerCase(), B.toLowerCase(), insert, remove, update);
				        return lev.distance;
				    });
				    console.log(three_word);
			    	socket.emit(
						'erroBuscaByCity', 
						{mensagem : three_word}
					);
				    

			    }else{
			    	client.write('{"cidade": "'+ data.cidade +'", "quartos": '+ data.quartos+', "banheiros":'+ data.banheiros+', "valor": '+ data.valor+', "vaga": '+data.vaga+'}');
				    client.on('data', function(rec) {
				    	console.log('Received: ' + rec);
				    	socket.emit(
							'msgParaCliente', 
							{mensagem : uintToString(rec).split("criscriscris")}
						);
					});
			    }
			});	  



		});

		socket.on('buscaByCityRight', function(data){
			client.write('{"cidade": "'+ data.cidade +'", "quartos": '+ data.quartos+', "banheiros":'+ data.banheiros+', "valor": '+ data.valor+', "vaga": '+data.vaga+'}');
		    client.on('data', function(rec) {
		    	console.log('Received: ' + rec);
		    	socket.emit(
					'msgParaCliente', 
					{mensagem : uintToString(rec).split("criscriscris")}
				);
			});
		});

	});
});