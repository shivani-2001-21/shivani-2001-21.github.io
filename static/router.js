import homepage from "./components/homepage.js"
const routes=[

    {   
        path:"/homepage",
        component:homepage,
    }
   
]
const router= new VueRouter({
    routes
})

export default router;
