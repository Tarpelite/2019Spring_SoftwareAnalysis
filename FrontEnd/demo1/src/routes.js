import Home from "./components/Home";
import PersonalInformation from "./components/PersonalInformation";
import MyAccount from "./components/MyAccount";
import MyResources from "./components/MyResources";
import Login from "./components/Login";
import SystemPage from "./components/SystemPage";
import MyStar from "./components/MyStar";
import ShopCar from "./components/ShopCar";

export const routes=[

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



export const routes2=[
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
    },
    {
        path:"/system/star",
        component:MyStar
    },
    {
    path:"/system/shopcar",
        component:ShopCar
    }
]
