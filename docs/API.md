# API

## login 

url: login/  
post:{ username, passwd}  
return:{status, is_expert}

## register

url: register/  
post:{username, passwd, telephone}  
return:{status: {0:用户名重复，1：登录成功}}

## index

url: index/  
post: {username}  
return:{头像url, 学术动态（文章名，文章url, 作者，时间）， 热搜排名（排名，资源名，资源url）

## search

url: search/  
post:{keywords}  
return:{文章题目，作者,作者url，简介，资源url， 排序， 价格}

## 个人信息

url: profile/  
post: {username}  
return:{用户名，手机号，邮箱，is_expert， 介绍，机构，姓名，领域, is_applying}

##  个人信息修改

url: profile_edit/
post:{原用户名，新用户名，手机号，邮箱，is_expert， 介绍，机构，姓名，领域}
return:{status:{0,1}}

## star

url: star/
post:{用户名，资源ID}  
return:{status}

## unstar

url: unstar/
post:{用户名， 资源ID}

## 我的收藏

url: my_collections/
post;{user_name}
return:{资源名，类型，介绍，资源url， 作者，作者url, 价格， buyed}

## 我的账户

url: my_account/
post:{username}
return;{balance}

## 已购资源

url: buyed_resouce/
post:{username}
return:{资源名， 类型， 介绍，资源url, 作者， 作者url, 价格}

## 专家门户

url: expert_home/
post:{username}
return:{姓名，机构，专业，被引次数，成果数， H指数，G指数，文章（排名）』 

## 批量添加到购物车

url: add_item_list/
post: {资源ID_list， username}
return:{status}

## 批量从购物车删除

url: remove_item_list:
post:{资源ID_list, username}
return:{status} 

## 购物车

url: item_cart/
post:{username}
return:{类似已购资源}

## 结算

url: purchase/
post:{username, item_list, total_cost}  
return:{status , balance}


## 申请成为专家

url: apply_for_expert/
post:{username, name, sex, institue, domain}  
return:{status}  

## 获取专家已发布资源

url: has_published/
post:{username}
return:{类似已购资源}


## 发布资源申请列表

url: publish_item_application/
post:{username}
return:{username, 资源申请表}

## 成为专家审核

url: U2E_pass/
post:{username, 申请表ID_list}
return: {status}

## 发布资源审核

url: PUB_pass/
post: {username, 申请表ID_list}
return:{status}







