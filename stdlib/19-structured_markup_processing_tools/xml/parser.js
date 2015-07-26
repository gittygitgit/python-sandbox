var sprintf = require('sprintf-js').sprintf
var winston = require('winston')
function parse(b, l) {
  var messageGroup = b.readInt16LE(0);
  var messageId= b.readInt16LE(2);
  var msgKey=(messageId << 16) | messageGroup;
  switch(msgKey) {
    case 65546:
      winston.debug('OrderBook');
      l.onOrderBook(b);
      break;
    case 131082:
      winston.debug('Participant');
      l.onParticipant(b);
      break;
    case 196618:
      winston.debug('User');
      l.onUser(b);
      break;
    case 262154:
      winston.debug('SessionChange');
      l.onSessionChange(b);
      break;
    case 327690:
      winston.debug('Order');
      l.onOrder(b);
      break;
    case 393226:
      winston.debug('BinaryDeal');
      l.onBinaryDeal(b);
      break;
    case 458762:
      winston.debug('Trade');
      l.onTrade(b);
      break;
    case 524298:
      winston.debug('EquilibriumPrice');
      l.onEquilibriumPrice(b);
      break;
    case 589834:
      winston.debug('StartOfTransaction');
      l.onStartOfTransaction(b);
      break;
    case 655370:
      winston.debug('Commit');
      l.onCommit(b);
      break;
    case 720906:
      winston.debug('EndOfReferenceData');
      l.onEndOfReferenceData(b);
      break;
    case 786442:
      winston.debug('QuotingResponsibility');
      l.onQuotingResponsibility(b);
      break;
    case 851978:
      winston.debug('PriceLimits');
      l.onPriceLimits(b);
      break;
    case 917514:
      winston.debug('ReferencePrice');
      l.onReferencePrice(b);
      break;
    case 983050:
      winston.debug('OpenBalance');
      l.onOpenBalance(b);
      break;
    case 1048586:
      winston.debug('IndexPrice');
      l.onIndexPrice(b);
      break;
    case 1114122:
      winston.debug('Account');
      l.onAccount(b);
      break;
    default:
      winston.debug(sprintf("unknown message type [messageId=%1$s, messageGroup=%2$s, msgkey=%3$s", messageId, messageGroup, msgKey));
  }
}
module.exports={
  parse:parse
}
