var ProjectInit = function (_combProject, _cmbModule,defaultProject,defaultModule) {
    var cmbProject = document.getElementById(_cmbProject);
    var cmbModule = document.getElementById(_cmbModule);
    var dataList = [];

    window.alert(defaultProject);
    window.alert(defaultModule);

    //设置默认选项---下面的选择项目和选择模块都用到了这个方法
    function cmbSelect(cmb, str) {
        for(var i=0; i< cmb.options.length; i++){
            if(cmb.options[i] == str){
                cmb.selectedIndex = i;
                return;
            }
        }
    }

    //创建下拉选项
    function cmbAddOption(cmb, str, obj) {
        console.log(str);
        var option = document.createElement("option");
        cmb.options.add(option);
        option.innerHTML = str;
        option.value = str;
        option.obj = obj;
    }
    //改变项目
    function changeProject() {
        cmbModule.options.length = 0 ;
        #cmbModule.onchange = null;
        if(cmbProject.selectedIndex == -1){
            return;
        }
        var item = cmbProject.options[cmbProject.slectedIndex].obj;
        for(var i = 0;i <item.moduleList.length; i ++){
            cmbAddOption(cmbModule, item.moduleList[i], null);
        }

        cmbSelect(cmbModule, defaultModule);
    }

    function getProjectList() {
        //调用项目列表接口
        $.get("/interface/get_project_list",{},function (resp) {
            if(resp.success === "true"){
                dataList = resp.data;
                //遍历项目
                for(var i =0;i<dataList.length;i++){
                    cmbAddOption(cmbProject, dataList[i].name,dataList[i]);

                }
                cmbSelect(cmbProject, defaultProject);
                changeProject();
                cmbProject.onchange = changeProject;
            }
        })
    }
    //调用getprojectList函数
    getProjectList();

}