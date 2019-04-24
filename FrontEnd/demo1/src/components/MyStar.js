import React, { Component } from 'react';
import { Table, Button,Tag ,Popconfirm} from 'antd';
import {quit_action} from "../redux/actions/reg_action";
import {connect} from "react-redux";


class MyStar extends Component{
    constructor(props) {
        super(props);
        /*this.init();*/
        this.props.init_stardata();
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

    /*state = {
        selectedRowKeys: [], // Check here to configure the default column
        loading: false,
        data : []
    };*/
    start = () => {
        this.setState({ loading: true });
        // ajax request after empty completing
        setTimeout(() => {
            this.setState({
                selectedRowKeys: [],
                loading: false,
            });
        }, 1000);
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
        /*this.setState({selectedRowKeys:[]})
        let newdata=this.state.data.filter(item => item.key !== key);
        this.setState({data:newdata});*/

        this.props.delete_stardata(key);


        console.log("删除后的state");
         console.log(this.props.data)
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

        /*console.log("删除后的state");
        console.log(this.state.data)*/
    }

/*    init=()=>{
        for (let i = 0; i < 20; i++) {
            this.state.data.push({
                key: i,
                name: `state资源 ${i}`,
                type:"state论文",
                author: `state作者. ${i}`,
                url:"https://www.jianshu.com/p/9cc2f7696300?from=timeline&isappinstalled=0",
                author_url:"http://space.bilibili.com/123938419/"
            });
        }
    }*/

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
                    onClick={()=>{this.props.multidelete_stardata()}}
                    disabled={!hasSelected}
                    /*loading={loading}*/
                    style={{margin:"auto"}}
                >
                    批量删除
                </Button>

                <button onClick={()=>{console.log(this.props.data)}}>输出state</button>


            </div>
        );
    }



}

function mapStateToProps(state)
{
    return{
        data:state.star.star_data,
        selectedRowKeys:state.star.selectedRowKeys
    }
}

function mapDispatchToProps(dispatch){
    return{

        set_selectedRowKeys:(selectedRowKeys)=>{dispatch({type: "set_selectedRowKeys",selectedRowKeys:selectedRowKeys})},
        delete_stardata:(itemkey)=>{dispatch({type:"delete_stardata",itemkey:itemkey})},
        multidelete_stardata:()=>{dispatch({type:"multidelete_stardata"})},
        init_stardata:()=>{dispatch({type:"init_stardata"})}
    }
}
MyStar=connect(mapStateToProps,mapDispatchToProps)(MyStar)
export default  MyStar;