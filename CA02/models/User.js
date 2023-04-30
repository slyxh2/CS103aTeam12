
const mongoose = require( 'mongoose' );
const Schema = mongoose.Schema;

var userSchema = Schema( {
  username:{
    type:String,
    required:true
  },
  password: {
    type:String,
    required:true
  },
  age:Number,
} );

module.exports = mongoose.model( 'User', userSchema );
