import React, { Component } from 'react';
import {Button, Checkbox, Icon, Input,Form} from "antd";

import "../App.css"
import {close_regaction, login_action, regaction} from "../redux/actions/reg_action";
import {connect} from "react-redux";
import axios from "axios"
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


class Register extends Component{

    state = {
        confirmDirty: false,
        autoCompleteResult: [],
    };

    //密码框对应的方法
    validateToNextPassword = (rule, value, callback) => {
        const form = this.props.form;
        if (value && this.state.confirmDirty) {
            form.validateFields(['confirm'], { force: true });
        }
        callback();
    }

    //确认密码框的方法
    compareToFirstPassword = (rule, value, callback) => {
        const form = this.props.form;
        if (value && value !== form.getFieldValue('password')) {
            callback('Two passwords that you enter is inconsistent!');
        } else {
            callback();
        }
    }

    //确认密码框不聚焦时触发的方法
    //只要有输入就把confirmDirty设为真
    handleConfirmBlur = (e) => {
        const value = e.target.value;
        this.setState({ confirmDirty: this.state.confirmDirty || !!value });
    }

//注册提交的方法
    registerSubmit = (e) => {
        e.preventDefault();
        this.props.form.validateFields((err, values) => {
            if (!err) {
                console.log('Received values of form: ', values);

            }
        });
    }

    //注册提交到后端的测试方法
    registerSubmit_test=(e)=>{
        e.preventDefault();
        axios.get('Http://127.0.0.1:8000/register', {
            params: {
                username: this.props.form.getFieldValue("registerUsername"),
                passwd:this.props.form.getFieldValue("password"),
                telephone:this.props.form.getFieldValue("phone")
            }
        })
            .then(function (response) {
                console.log(response);
                if(response.data.status){
                    alert("注册成功，快去登录吧！")
                }
                else {
                    alert("注册失败，似乎除了点问题")
                }
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
        return(
            <div className={"register-form"}>{/*注册框*/}

                <Icon type="close" className={"close"} onClick={this.props.closeregister}  />
                <Form {...formItemLayout}  onSubmit={this.registerSubmit_test}>
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
                            <Input  style={{ }} />
                        )}
                    </Form.Item>
                    <Form.Item {...tailFormItemLayout}>
                        {getFieldDecorator('agreement', {
                            valuePropName: 'checked',//输入框什么的默认是value，但是checkbox必须把值的名字改成checked
                        })(
                            <Checkbox>I have read the <a href="">agreement</a></Checkbox>
                        )}
                    </Form.Item>
                    <Form.Item {...tailFormItemLayout}>
                        <Button type="primary" htmlType="submit">注册</Button>
                    </Form.Item>
                </Form>





            </div>
        )
    }

}
function mapStateToProps(state)
{
    return{
        registerFlag:state.reg.regflag,

    }
}

function mapDispatchToProps(dispatch){
    return{

        closeregister:()=>{dispatch(close_regaction)},

    }
}
Register=connect(mapStateToProps,mapDispatchToProps)(Register)
export default Form.create()(Register);