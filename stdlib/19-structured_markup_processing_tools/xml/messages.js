var util = require('util');
var BigNumber = require('bignumber.js');
var fn = require('./functions.js');
var sprintf = require('sprintf-js').sprintf;
var indent='    ';
function getRecordFmt(n) {
  var pad='';
  for (var i = 0; i < n; i++) {
    pad += indent;
  };
  return pad + '%1$-50s = %2$s';
}
