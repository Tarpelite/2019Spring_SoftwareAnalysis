import Home from "./components/Home";
import PersonalInformation from "./components/PersonalInformation";
import MyAccount from "./components/MyAccount";
import MyResources from "./components/MyResources";
import Login from "./components/Login";
import SystemPage from "./components/SystemPage";

let routes=[

    {
        path:"/",
        component:Login,
        exact:true
    },
    {
        path:"/system/",
        component:SystemPage
    }


]

export  default routes;

let routes2=[
    {
        path:"/system/",
        component:Home,
        exact: true
    },
    {
        path:"/system/personalinformation",
        component:PersonalInformation
    },
    {
        path:"/system/account",
        component:MyAccount
    },
    {
        path:"/system/resources",
        component:MyResources
    }
]
