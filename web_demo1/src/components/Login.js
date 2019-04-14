import React, { Component } from 'react';
import { Card,Layout, Menu, Icon ,Button,Form,Input,Checkbox} from 'antd';
import {Redirect }from "react-router-dom"
import logo from '../image/logo.png';
import {connect} from "react-redux"
import {regaction, close_regaction, login_action} from "../redux/actions/reg_action";
import "../css/background.css"

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


    loginSubmit = (e) => {
        e.preventDefault();
        this.props.form.validateFields((err, values) => {
            if (!err) {
                console.log('Received values of form: ', values);
                this.setState({loginflag:true})

            }
        });
    }

    registerSubmit = (e) => {
        e.preventDefault();
        this.props.form.validateFields((err, values) => {
            if (!err) {
                console.log('Received values of form: ', values);

            }
        });
    }

    closeregister=()=>{
        this.setState({
            registerFlag:false
        })
    }

componentDidMount() {
        console.log(this.props.registerFlag)
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
                        this.props.registerFlag?

                            <div className={"register-form"}>{/*注册框*/}

                                <Icon type="close" className={"close"} onClick={this.props.closeregister}  />
                                <Form {...formItemLayout}  onSubmit={this.registerSubmit}>
                                    <h2>注册</h2>
                                    <Form.Item label={"用户名"} >
                                        {getFieldDecorator('registerUsername', {
                                            rules: [{
                                                 message: '请输入用户名!',
                                            }, {
                                                required: true, message: 'Please input your username!',
                                            }],
                                        })(
                                            <Input />
                                        )}
                                    </Form.Item>
                                    <Form.Item
                                        label="密码"
                                    >
                                        {getFieldDecorator('password', {
                                            rules: [{
                                                required: true, message: 'Please input your password!',
                                            }, {
                                                validator: this.validateToNextPassword,
                                            }],
                                        })(
                                            <Input type="password" />
                                        )}
                                    </Form.Item>

                                <Form.Item
                                    label="确认密码"
                                >
                                    {getFieldDecorator('confirm', {
                                        rules: [{
                                            required: true, message: 'Please confirm your password!',
                                        }, {
                                            validator: this.compareToFirstPassword,
                                        }],
                                    })(
                                        <Input type="password" onBlur={this.handleConfirmBlur} />
                                    )}
                                </Form.Item>
                                    <Form.Item
                                        label="手机号"
                                    >
                                        {getFieldDecorator('phone', {
                                            rules: [{ required: true, message: 'Please input your phone number!' }],
                                        })(
                                            <Input  style={{ width: '100%' }} />
                                        )}
                                    </Form.Item>
                                    <Form.Item {...tailFormItemLayout}>
                                        {getFieldDecorator('agreement', {
                                            valuePropName: 'checked',
                                        })(
                                            <Checkbox>I have read the <a href="">agreement</a></Checkbox>
                                        )}
                                    </Form.Item>
                                    <Form.Item {...tailFormItemLayout}>
                                        <Button type="primary" htmlType="submit">Register</Button>
                                    </Form.Item>
                            </Form>





                            </div>

                        :
                            <div></div>
                    }
                </div>


                {/*登录部分*/}
            <div className={"login"}>
                <h2 >登录部分</h2>
                <br/>
                <Form onSubmit={loginsubmit}style={{margin:"auto",marginTop:"60%",marginBottom:"100%"}}>


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
        loginsubmit:(e)=>{
            e.preventDefault();
        dispatch(login_action);
        }
    }
}

Login=connect(mapStateToProps,mapDispatchToProps)(Login)
export default Form.create() (Login);