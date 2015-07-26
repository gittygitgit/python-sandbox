var Messages = require('./messages.js')
function Listener() {
  this.onOrderBook = function(buf) {
    var x = new Messages.orderBook(buf);
    x.print();
  }
  this.onParticipant = function(buf) {
    var x = new Messages.participant(buf);
    x.print();
  }
  this.onUser = function(buf) {
    var x = new Messages.user(buf);
    x.print();
  }
  this.onSessionChange = function(buf) {
    var x = new Messages.sessionChange(buf);
    x.print();
  }
  this.onOrder = function(buf) {
    var x = new Messages.order(buf);
    x.print();
  }
  this.onBinaryDeal = function(buf) {
    var x = new Messages.binaryDeal(buf);
    x.print();
  }
  this.onTrade = function(buf) {
    var x = new Messages.trade(buf);
    x.print();
  }
  this.onEquilibriumPrice = function(buf) {
    var x = new Messages.equilibriumPrice(buf);
    x.print();
  }
  this.onStartOfTransaction = function(buf) {
    var x = new Messages.startOfTransaction(buf);
    x.print();
  }
  this.onCommit = function(buf) {
    var x = new Messages.commit(buf);
    x.print();
  }
  this.onEndOfReferenceData = function(buf) {
    var x = new Messages.endOfReferenceData(buf);
    x.print();
  }
  this.onQuotingResponsibility = function(buf) {
    var x = new Messages.quotingResponsibility(buf);
    x.print();
  }
  this.onPriceLimits = function(buf) {
    var x = new Messages.priceLimits(buf);
    x.print();
  }
  this.onReferencePrice = function(buf) {
    var x = new Messages.referencePrice(buf);
    x.print();
  }
  this.onOpenBalance = function(buf) {
    var x = new Messages.openBalance(buf);
    x.print();
  }
  this.onIndexPrice = function(buf) {
    var x = new Messages.indexPrice(buf);
    x.print();
  }
  this.onAccount = function(buf) {
    var x = new Messages.account(buf);
    x.print();
  }
}
module.exports={
  Listener: Listener
}
