const mongoose = require( 'mongoose' );
const User=require('./User')
const requestSchema=mongoose.Schema({
    question:{
        type:String,
        required:true
    },
    answer:{
        type:String,
        required:true
    },
    user:{
        type:mongoose.Schema.Types.ObjectId,
        ref:"User",
        required:true
    }
}
)

module.exports=mongoose.model("Request",requestSchema)