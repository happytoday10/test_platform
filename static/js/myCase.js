//获取指定case_id的用例信息
var CaseInit = function (case_id) {



    function getCaseInfo() {
        //调用某个用例的信息
        $.post("/interface/get_case_info/",{
            "caseId":case_id
        },function (resp) {
            if(resp.success === "true"){
                let result = resp.data;
                console.log("结果：",result)
                //这里是给文本框赋值--直接百度js 设置输入框的值
                document.getElementById("req_name").value = result.name;
                document.getElementById("req_url").value = result.uri;
                document.getElementById("req_header").value = result.header;
                document.getElementById("req_parameter").value = result.parameter;
                //这里处理单选框的，搜索 js给元素添加属性
                if(result.req_method == "post"){
                    document.getElementById("post").setAttribute("checked","")
                }
                //下面这个是针对参数类型的
                if(result.req_type == "JSON"){
                    document.getElementById("req_type").setAttribute("checked","")
                }
                //初始化菜单-调试项目和模块信息的显示是否对。
               ProjectInit('project_name','module_name',result.project_name,result.module_name);



            }
            else{
                window.alert("用例的id不存在");
            }
        });
    }
    //调用getCaseInfo函数
    getCaseInfo();

}