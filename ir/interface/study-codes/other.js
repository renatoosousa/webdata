var ed = require('edit-distance');
var fs = require('fs');
var path = require('path');

function getED(A,B){
    var insert, remove, update;
    insert = remove = function(node) { return 1; };
    update = function(stringA, stringB) { return stringA !== stringB ? 1 : 0; };
    var lev = ed.levenshtein(A, B, insert, remove, update);
    return lev.distance;
}

filePath1 = path.join(__dirname, 'dic_city.txt');
filePath2 = path.join(__dirname, 'stop_words.txt');
filePath3 = path.join(__dirname, 'comum_word.txt');


fs.readFile(filePath3, {encoding: 'utf-8'}, function(err,comum_word){
	comum_word = comum_word.split("\n");
    var frase = ["Apto", "ems", "Recifi","qts"];
    var calc = 100000;

    var wordCor = [];
    for(var i = 0; i<frase.length; i++){
   		var temp = 1000000;
    	for(var j = 0; j<comum_word.length; j++){
    		var res = getED(frase[i],comum_word[j]);
    		if(res<temp){
    			temp = res;
                if(wordCor.length>0) wordCor.splice(i,1);
    			wordCor.push(comum_word[j].toLowerCase());
    		}
    	}
    }

    var recomen = [];
    for (var i = frase.length - 1; i >= 0; i--) {
    	recomen.push(wordCor[i]);
    }
    recomen = recomen.join(' ');
    console.log(recomen);
});

