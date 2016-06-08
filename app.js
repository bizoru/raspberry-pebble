/**
 * Welcome to Pebble.js!
 *
 * This is where you write your app.
 */

var UI = require('ui');
var ajax = require('ajax');


var main = new UI.Card({
  title: 'Pebble LED',
  icon: 'images/menu_icon.png',
  subtitle: 'Led App',
  body: 'Prende Led con Boton Arriba, Apaga Led Boton Abajo',
  subtitleColor: 'indigo', // Named colors
  bodyColor: '#9a0036' // Hex colors
});

main.show();

main.on('click', 'down', function(e) {
  var card = new UI.Card();
  card.title('Led Apagado!');
  card.show();
  ajax({ url: 'http://trolear.me:3412/turn/off', type: 'json' },
  function(data) {
     console.log(data);
  }
);
});

main.on('click', 'up', function(e) {
  var card = new UI.Card();
  card.title('Led Prendido!');
  card.show();
  ajax({ url: 'http://trolear.me:3412/turn/on', type: 'json' },
  function(data) {
    console.log(data);
  }
);
});
