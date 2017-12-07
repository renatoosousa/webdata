var ed = require('edit-distance');
var fs = require('fs');
var path = require('path');

function getED(A,B){
    var insert, remove, update;
    insert = remove = function(node) { return 1; };
    update = function(stringA, stringB) { return stringA !== stringB ? 1 : 0; };
    var lev = ed.levenshtein(A.toLowerCase(), B.toLowerCase(), insert, remove, update);
    return lev.distance;
}

filePath1 = path.join(__dirname, 'dic_city.txt');
filePath2 = path.join(__dirname, 'stop_words.txt');
filePath3 = path.join(__dirname, 'comum_word.txt');

fs.readFile(filePath1, {encoding: 'utf-8'}, function(err,dic_city){
fs.readFile(filePath2, {encoding: 'utf-8'}, function(err,stop_words){
fs.readFile(filePath3, {encoding: 'utf-8'}, function(err,comum_word){
	dic_city = dic_city.split("\n");
	stop_words = stop_words.split("\n");
	comum_word = comum_word.split("\n");
    
    frase = ["Aprtameto", "em", "Recifi","quart"];
    var calc = 100000;

    var wordCor = new Array(frase.length);
	for (var i = 0; i < frase.length; i++) {
  		wordCor[i] = [];
	}
    for(var i = 0; i<frase.length; i++){
   		var temp = 1000000;

   		for(var j = 0; j<dic_city.length; j++){
    		res = getED(frase[i],dic_city[j]);
    		if(res<temp){
    			temp = res;
    			if(wordCor[i].length>0)wordCor[i].splice(0,1);
    			wordCor[i].push(dic_city[j].toLowerCase());
    		}
    	}
    	for(var j = 0; j<stop_words.length; j++){
    		res = getED(frase[i],stop_words[j]);
    		if(res<temp){
    			temp = res;
    			wordCor[i].splice(0,1);
    			wordCor[i].push(stop_words[j].toLowerCase());
    		}
    	}
    	for(var j = 0; j<comum_word.length; j++){
    		res = getED(frase[i],comum_word[j]);
    		if(res<temp){
    			temp = res;
    			wordCor[i].splice(0,1);
    			wordCor[i].push(comum_word[j].toLowerCase());
    		}
    	}
    }

    var recomen = [];
    for (var i = 0; i <frase.length ; i++) {
    	recomen.push(wordCor[i]);
    }
    recomen = recomen.join(' ');
    console.log(recomen)
});
});
});
