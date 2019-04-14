import React, { Component } from 'react';
import {Card, Layout, Menu, Icon, Button, Form, Input, Checkbox, Avatar} from 'antd';
import {Redirect }from "react-router-dom"
import logo from '../image/logo.png';
import {connect} from "react-redux"
import {regaction, close_regaction, login_action} from "../redux/actions/reg_action";
import "../css/background.css"
import Register from "./Register";

const {
    Header, Content, Footer, Sider,
} = Layout;
const Formitem=Form.item;

const registerFlag=false;
const loginflag=false;
class Login extends Component{
    constructor(props) {
        super(props);
    this.state={
    /*registerFlag:false,*/
        /*loginflag:false*/
    }
    }

    /*register=()=>{
        this.setState({
            registerFlag:true
        })
    }*/


    /*loginSubmit = (e) => {
        e.preventDefault();
        this.props.form.validateFields((err, values) => {
            if (!err) {
                console.log('Received values of form: ', values);
                this.setState({loginflag:true})

            }
        });
    }*/

    /*registerSubmit = (e) => {
        e.preventDefault();
        this.props.form.validateFields((err, values) => {
            if (!err) {
                console.log('Received values of form: ', values);

            }
        });
    }*/

   /* closeregister=()=>{
        this.setState({
            registerFlag:false
        })
    }*/

componentDidMount() {
        console.log(this.props.registerFlag)
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

    render() {
        const { getFieldDecorator } = this.props.form;
        const {register,loginsubmit}=this.props

        const formItemLayout = {
            labelCol: {
                xs: { span: 24 },
                sm: { span: 8 },
            },
            wrapperCol: {
                xs: {span: 24},
                sm: {span: 10},
            }
        };
        const tailFormItemLayout = {
            wrapperCol: {
                xs: {
                    span: 24,
                    offset: 0,
                },
                sm: {
                    span: 16,
                    offset: 4,
                },
            },
        };
        if (this.props.loginflag)
        {
            return<Redirect to={"/system"}/>
        }
        return(

            <div className="Login">

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
                <Form onSubmit={this.LoginSubmit}style={{margin:"auto",marginTop:"10%",marginBottom:"100%"}}>

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
        loginsubmit:(value)=>{
        dispatch(login_action);
        }
    }
}

Login=connect(mapStateToProps,mapDispatchToProps)(Login)
export default Form.create() (Login);