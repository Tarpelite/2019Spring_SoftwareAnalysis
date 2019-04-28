import React, { Component } from 'react';
import {Card, Layout, Menu, Icon, Button, Form, Input, Checkbox, Avatar} from 'antd';
import {Redirect }from "react-router-dom"
import logo from '../image/logo.png';
import {connect} from "react-redux"
import {regaction, close_regaction, login_action} from "../redux/actions/reg_action";
import "../css/background.css"
import Register from "./Register";
import axios from "axios"


const {
    Header, Content, Footer, Sider,
} = Layout;
const Formitem=Form.item;


class Login extends Component{
    constructor(props) {
        super(props);

    }


componentDidMount() {
        /*console.log(this.props.registerFlag)*/
}

//登录提交的方法
    LoginSubmit = (e) => {
        e.preventDefault();
        this.props.form.validateFields((err, values) => {
            if (!err) {
                console.log('Received values of form: ', values);
                this.props.loginsubmit();
            }
        });
    }

    logintest=(e)=>{
        e.preventDefault();
        this.props.form.validateFields((err, values) => {
            if (!err) {
                console.log('Received values of form: ', values);
            }
        });
        console.log("捕获的用户名为：")
        console.log(this.props.form.getFieldValue("loginUserName"))
        console.log(this.props.form.getFieldValue("loginPassword"))

        axios.get('Http://127.0.0.1:8000/login', {
            params: {
                username: this.props.form.getFieldValue("loginUserName"),
                passwd:this.props.form.getFieldValue("loginPassword")
            }
        })
            .then( (response) =>{
                console.log(response);
                if (response.data.status)
                {
                    console.log("密码正确，开始登录");
                    this.props.loginsubmit(this.props.form.getFieldValue("loginUserName"),response.data.is_expert);
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

    render() {
        const { getFieldDecorator } = this.props.form;
        const {register}=this.props

        // if (this.props.loginflag)
        // {
        //     return<Redirect to={"/system"}/>
        // }
        return(

            <div className="Login">
                {this.props.loginflag?<Redirect to={"/system"}/>:""}
                {/*左边注册部分*/}
                <div style={{width:"75%",float:"left",margin:"0"}}>
                <h2>hello</h2>
                    <img src={logo} className={"logo"}/>

                    {
                        this.props.registerFlag ?
                            <Register/>
                            :
                            <div></div>
                    }

                </div>


                {/*登录部分*/}
            <div className={"login"}>
                <h2 >登录部分</h2>
                <br/>
                <Form onSubmit={this.logintest}style={{margin:"auto",marginTop:"10%",marginBottom:"100%"}}>

                    <Avatar shape="square" size={100} icon="user" style={{display:"inline-block",margin:"50px"}}/>
                    <Form.Item>
                        {getFieldDecorator('loginUserName', {
                            rules: [{ required: true, message: 'Please input your username!' }],
                        })(
                            <Input  prefix={<Icon type="user" style={{ color: 'rgba(0,0,0,0.25)' }} />} placeholder="用户名" style={{margin:"auto",width:"61.8%"}} />
                        )}
                    </Form.Item>
                    <Form.Item>
                        {getFieldDecorator('loginPassword', {
                            rules: [{ required: true, message: 'Please input your Password!' }],
                        })(
                            <Input  prefix={<Icon type="lock" style={{ color: 'rgba(0,0,0,.25)' }} />} type="password" placeholder="密码"  style={{margin:"auto",width:"61.8%"}}/>
                        )}
                    </Form.Item>
                    <Form.Item>
                        <Button type="primary" htmlType="submit" style={{margin:"auto",marginRight:"10px",marginLeft:"10px"}} >登录</Button>
                        <Button onClick={register}>注册</Button>

                    </Form.Item>


                </Form>



            </div>

            </div >
        )
    }

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

Login=connect(mapStateToProps,mapDispatchToProps)(Login)
export default Form.create() (Login);