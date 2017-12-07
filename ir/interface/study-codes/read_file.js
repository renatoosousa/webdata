var ed = require('edit-distance');
var fs = require('fs');
var path = require('path');
filePath = path.join(__dirname, 'dic_city.txt');

// var data = []

// st = "Recifes"
// fs.readFile(filePath, {encoding: 'utf-8'}, function(err,data){
//     if (!err) {
//         data = data.split("\n");
//         for(var i = 0; i<data.length;i++){
//             if(st.toLowerCase()==data[i].toLowerCase()){
//                 console.log("Yes");
//             }
//         }
//     }else{
//         console.log(err);
//     }
// });

// function (A,B){
//     var insert, remove, update;
//     insert = remove = function(node) { return 1; };
//     update = function(stringA, stringB) { return stringA !== stringB ? 1 : 0; };
//     var lev = ed.levenshtein(A.toLowerCase(), B.toLowerCase(), insert, remove, update);
//     return lev.distance;
// }


fs.readFile(filePath, {encoding: 'utf-8'}, function(err,data){
    if (!err) {
        data = data.split("\n");
        console.log('received data: ' + data[1]);

        var insert, remove, update;
        insert = remove = function(node) { return 1; };
        update = function(stringA, stringB) { return stringA !== stringB ? 1 : 0; };
         
        // Define two strings. 
        var stringA = "Recife";
        var stringB = "Recifes";
        // var stringB = "Recifs";
         
        // Compute edit distance, mapping, and alignment. 
        // var lev = ed.levenshtein(stringA, stringB, insert, remove, update);
        // console.log('Levenshtein', lev.distance, lev.pairs(), lev.alignment());

        var three_word = []
        for(var i = 0; i<data.length;i++){
            var lev = ed.levenshtein(stringB.toLowerCase(), data[i].toLowerCase(), insert, remove, update);
            if(three_word.length<3){
                three_word.push(data[i]);
            }
            else{
                for(var j = 0; j<three_word.length;j++){
                    var lev2 = ed.levenshtein(stringB.toLowerCase(), three_word[j].toLowerCase(), insert, remove, update);
                    if(lev.distance<lev2.distance){
                        if(data[i]!=three_word[0] && data[i]!=three_word[1] && data[i]!=three_word[2]){
                            three_word.splice(j,1);
                            three_word.push(data[i]);
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

    } else {
        console.log(err);
    }
});

// console.log(data[3]);
// var insert, remove, update;
// insert = remove = function(node) { return 1; };
// update = function(stringA, stringB) { return stringA !== stringB ? 1 : 0; };
 
// // Define two strings. 
// var stringA = "Recife";
// var stringB = "Reicie";
// // var stringB = "Recifs";
 
// // Compute edit distance, mapping, and alignment. 
// var lev = ed.levenshtein(stringA, stringB, insert, remove, update);
// console.log('Levenshtein', lev.distance, lev.pairs(), lev.alignment());