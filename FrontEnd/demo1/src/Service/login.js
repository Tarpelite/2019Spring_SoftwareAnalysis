import axios from "axios"
import {close_regaction, regaction} from "../redux/actions/reg_action";
import {connect} from "react-redux";

function loginsubmit(loginUserName,loginPassword) {

    console.log("函数成功调用，参数为")
    console.log(loginUserName)
    console.log(loginPassword)
    axios.get('Http://127.0.0.1:8000/login', {
        params: {
            username:loginUserName,
            passwd:loginPassword
        }
    })
        .then( (response) =>{
            console.log(response);
            if (response.data.status)
            {
                console.log("密码正确，开始登录");
                this.props.loginsubmit(loginUserName,response.data.is_expert);
            }
            else {alert("登录失败")}
        })
        .catch(function (error) {
            console.log(error);
        })
        .then(function () {
            // always executed
        });


}
function mapStateToProps(state)
{
    return{
        registerFlag:state.reg.regflag,
        loginflag:state.login.loginflag
    }
}

function mapDispatchToProps(dispatch){
    return{
        register:()=>{dispatch(regaction)},
        closeregister:()=>{dispatch(close_regaction)},
        loginsubmit:(username,is_expert)=>{
            dispatch({type:"login",username:username,is_expert:is_expert});
        }
    }
}

loginsubmit=connect(mapStateToProps,mapDispatchToProps)(loginsubmit);
export default loginsubmit()