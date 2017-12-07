/* Importar modulo do framework express */
var express = require('express');

/* Importar modulo do consign */
var consign = require('consign');

/* Importar modulo do body-parser */
var bodyParser = require('body-parser');

/* Iniciar o objeto express */
var app = express();

/* Setar as variaveis 'view engine' e 'views' do express */
app.set('view engine', 'ejs');
app.set('views', './app/views');

/* Configurar o middleware express.static */
app.use(express.static('./app/public'));

/* Configurar o middleware body-parser */
app.use(bodyParser.urlencoded({extended: true}));

/* Configurar consign autoload routes -- efetua autoload rotas, models controllers */
consign()
	.include('app/routes')
	.then('app/models')
	.then('app/controllers')
	.into(app);

/* Exportar o objeto app */
module.exports = app;