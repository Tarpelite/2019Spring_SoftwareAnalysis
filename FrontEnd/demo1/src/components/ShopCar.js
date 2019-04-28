import React, { Component } from 'react';
import {Table, Button, Tag, Popconfirm} from 'antd';
import {connect} from "react-redux";
import axios from "axios"



class ShopCar extends Component{
    constructor(props) {
        super(props);
this.get_shopcar_data(this.props.user_id)
        /*this.props.init_stardata();*/
    }

    columns = [{
        title: '资源名称',
        dataIndex: 'name',
        key:"name",
        render: (text,record, index) => <a href={record.url} target="_Blank" >{text}</a>
    }, {
        title: '作者',
        dataIndex: 'author',
        render: (text,record, index) => <a href={record.author_url} target="_Blank" >{text}</a>
    }, {
        title: '资源类型',
        dataIndex: 'type',
        render: type => (
            <span>
      <Tag color={'geekblue'} >{type}</Tag>
    </span>
        ),
    },{
        title:"操作",
        dataIndex:"operation",
        render: (text, record) => (
            this.props.data.length >= 1
                ? (
                    <Popconfirm title="确认删除?" onConfirm={() => this.handleDelete(record.key)}>
                        <a href="javascript:;">Delete</a>
                    </Popconfirm>
                ) : null
        ),
    }
    ];

    get_shopcar_data=(user_id)=>{
        axios.get(`Http://127.0.0.1:8000/item_cart/${user_id}`, {
            params: {

            }})
            .then( (response) =>{
                console.log(response);
                //设置购物车数据
                this.props.get_shopcar_data(response.data.item_list,response.data.num)
            })
            .catch(function (error) {
                console.log(error);
            })
            .then(function () {
                // always executed
            });
    }

    onSelectChange = (selectedRowKeys) => {
        console.log('selectedRowKeys changed: ', selectedRowKeys);
        //这里应该就是将state的选中数组绑定到表格的操作了
        this.props.set_selectedRowKeys(selectedRowKeys);
        console.log("选择项改变后的state长度为"+this.props.data.length)
    }

    handleDelete = (key) => {
        console.log("你想删除"+key);
        console.log("类里面的state：");
        console.log(this.state)
        /*this.props.delete_stardata(key);
        console.log("删除后的state");
        console.log(this.props.data)*/
    }
    multiDelete=(selectedRowKeys) => {

        console.log("你想删除");
        console.log(selectedRowKeys)
        console.log("类里面的state：");
        console.log(this.state)
        let newdata=[];
        //在选中数组里面找不到item.key，其实就是批量删除的筛选器了
        this.setState({data:this.state.data.filter(item => selectedRowKeys.indexOf(item.key)=== -1)})
        //完成删除动作之后需要把选中数组也一起清空
        this.state.selectedRowKeys=[];

    }
get_shopcar_data_test=()=>{

}


    render()  {

        const rowSelection = {
            selectedRowKeys:this.props.selectedRowKeys,
            onChange: this.onSelectChange,
        };
        const hasSelected = this.props.selectedRowKeys.length > 0;

        return (
            <div style={{}}>
                <div style={{ marginBottom: 6 ,marginRight:8, float:"left"}}>
                    <span style={{ marginRight: 8 }}>
                        {hasSelected ? ` ${this.props.selectedRowKeys.length} 条资源已选中` : ''}
                    </span>
                </div>

                <br/>

                <Table  rowSelection={rowSelection} columns={this.columns} dataSource={this.props.data} pagination={{pageSize:7}} />
                <Button
                    type="primary"
                    onClick={()=>{/*this.props.multidelete_stardata()*/}}
                    disabled={!hasSelected}
                    /*loading={loading}*/
                    style={{margin:"auto"}}
                >
                    批量结算
                </Button>

                <button onClick={()=>{console.log(this.props.data)}}>输出state</button>
                <button onClick={()=>this.get_shopcar_data_test()}>初始化data</button>

            </div>
        );

}}

    function mapStateToProps(state)
{
    return{
        data:state.shopcar.data,
        selectedRowKeys:state.shopcar.selectedRowKeys,
        user_id:state.login.user_id
    }
}

    function mapDispatchToProps(dispatch){
    return{

        set_selectedRowKeys:(selectedRowKeys)=>{dispatch({type: "set_shopcar_selectedRowKeys",selectedRowKeys:selectedRowKeys})},
        get_shopcar_data:(data,num)=>{dispatch({type:"get_shopcar",data:data,num:num})}
    }
}
    ShopCar=connect(mapStateToProps,mapDispatchToProps)(ShopCar)
export default  ShopCar;