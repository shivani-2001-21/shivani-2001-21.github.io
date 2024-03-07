console.log("Hello from js")

import router from "./router.js"



const a= new Vue({
    el:"#app", 
    router:router,
    template :`
    <div> 
    
    <center> <h1> <router-link to="/homepage"> Welcome to TixItis </router-link> </h1> 
    <br>
    <br>
    <br>


    <router-view></router-view>
     </div>`

})





            

