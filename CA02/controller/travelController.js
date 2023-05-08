const api_key="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"
const { Configuration, OpenAIApi } = require("openai");
const Request=require("../models/request")

module.exports={
    show:(req,res,next)=>{
      res.render("travel/index")

    }
    ,
    getQuestion: async (req,res,next)=>{
      const configuration = new Configuration({
        apiKey: api_key,
      });
      const openai = new OpenAIApi(configuration);
      const message="Help me find the top10 famous scenic spots in the following places, and express them in lists:"+req.body.question
      
      const completion = await openai.createCompletion({
        model: "text-davinci-003",
        prompt: message,
        max_tokens: 75,
        n: 1,
        stop: null,
        temperature: 1,
      });
        
    res.locals.question=req.body.question
    res.locals.answer = completion.data.choices[0].text.replace(/\n/g, '<br>').replace(',', '', 1);


    res.locals.user=req.user
    Request.create({
      question:res.locals.question,
      answer:res.locals.answer,
      user:res.locals.user
    }).catch((e)=>{
      console.log(e.body)
    })
    res.render("travel/results")
},
showRequest: (req, res, next) => {
  Request.find({})
    .populate("user")
    .then((requests) => {
      res.locals.requests = requests;
      next();
    })
    .catch((error) => {
      console.log(`Error fetching requests: ${error.message}`);
      next(error);
    });
  
},
requestView: (req, res) => {
  res.render("requests");
},

}