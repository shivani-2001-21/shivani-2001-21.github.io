import homepage from "./components/homepage.js"
const routes=[

    {   
        path:"/user_home",
        component:homepage,
    }
   
]
const router= new VueRouter({
    routes
})

export default router;
