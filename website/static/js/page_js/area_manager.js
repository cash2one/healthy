	var tempname;	//可能会修改的机构名称
	var tempcode;	//机构代码
	var temptype;	//机构类型
	var tempcodeold;	//记录旧的机构代码
	var tempparentcode; //父机构代码
	var state=0;	//["state"]=='0':只是查数据库返回，1修改数据库返回，2添加数据库返回
	
	var org_state=0;	//["org_state"]=='0':只是查数据库返回，1修改数据库返回，2添加数据库返回
	var org_name_new;
	var org_code; //记录旧的机构代码
	var org_areacode;
	var org_type;
	var parentorgcode;
	var levelorder;
	function showA() {
		document.getElementById('rcontent_check_D').style.display="none";
		document.getElementById('rcontent_check_A').style.display="";

	}
	function showD() {
		document.getElementById('rcontent_check_A').style.display="none";
		document.getElementById('rcontent_check_D').style.display="";
	}
	function onClickD(e){
		document.getElementById('code_E').innerHTML=e.getAttribute("orgcode");//医疗机构编码
		document.getElementById('type_E').innerHTML=e.getAttribute("orgtype");
		document.getElementById('pcode_E').innerHTML=e.getAttribute("orgpcode");
		document.getElementById('orgarea_E').innerHTML=e.getAttribute("areacode");
		document.getElementById('orglevel_E').innerHTML=e.getAttribute("orglevelorder");
		document.getElementById('name_E').value=e.getAttribute("orgname");
	  	//  	document.getElementById('parentcode_C').innerHTML=a_areaCode; //修改面板 C （添加区域）
	  	
	}
	function update_area() //根据 state来确定查看/修改/添加 
	{
		$.ajax({
            type:"POST",
            data: {state:state,codeold:tempcodeold,name:tempname,code:tempcode,type:temptype,codeparent:tempparentcode},// 是否修改机构，以及修改的参数
            url: "/update_area/",//"{% url 'update_area' %}", //后台处理函数的url 这里用的是static url 需要与urls.py中的name一致
            cache: false,
            dataType: "json",
            success: function(result, statues, xml){
            	$('#left_tree').html(result['html']);                                        //成功时弹出view传回来的结果
            },
            error: function(){
                alert("error when update area!");
            }
        });
		return false; //此处需要return
	}
	function fuc_update_org() //根据org_state来确定查看/修改/添加 
	{
		$.ajax({
            type:"POST",
            data: {state:org_state,areacode:org_areacode,name:org_name_new,
            	code:org_code, type:org_type, codeparent:parentorgcode,levelorder:levelorder },// 是否修改机构，以及修改的参数
            url: "/update_org/",//"{% url 'update_org' %}", //后台处理函数的url 这里用的是static url 需要与urls.py中的name一致
            cache: false,
            dataType: "json",
            success: function(result, statues, xml){
            	$('#info_check_D').html(result['html']);                                        //成功时弹出view传回来的结果
            	
            },
            error: function(){
                alert("error when update org!");
            }
        });
		return false; //此处需要return
	}
	function onClick(e){
		//先修改AB面板的区域信息，再修改DE面板的机构信息
      	var a_areaCode=e.getAttribute("a_areaCode");//从树结构中获取区域信息
      	var a_areaName=e.getAttribute("a_areaName");
      	var a_areaType=e.getAttribute("a_areaType");
      	document.getElementById('name_A').innerHTML=a_areaName;	//修改面板A（查看面板）
      	document.getElementById('code_A').innerHTML=a_areaCode;
      	document.getElementById('type_A').innerHTML=a_areaType;
      	document.getElementById('name_B').value =a_areaName;	//修改面板B （修改面板）
      	document.getElementById('code_B').value =a_areaCode;
      	document.getElementById('type_B').value =a_areaType;
      	document.getElementById('code_B').setAttribute("old_codeB", a_areaCode);
      	document.getElementById('orgarea_D').innerHTML=a_areaCode;//修改添加医疗机构面板D （修改面板）
      	
      	org_state=0;	//查看机构信息，更新面板DE
      	org_areacode=a_areaCode;
      	fuc_update_org();
      }
	function onClickC(e){
	  	var a_areaCode=e.getAttribute("a_parentcode");
	  	document.getElementById('parentcode_C').innerHTML=a_areaCode; //修改面板 C （添加区域）
	}
	$(document).ready(function(){
     
        state=0;
        update_area();
        $('#area_area_modify').submit(
            	function(){
            		state=1;
            		tempname=$('#name_B').val();
            		tempcode=$('#code_B').val();
            		temptype=$('#type_B').val();
            		tempcodeold=document.getElementById('code_B').getAttribute("old_codeB");
            		$("#modal-container-B").modal('hide');
            		document.getElementById('name_A').innerHTML=tempname;	//修改面板A（查看面板）
                  	document.getElementById('code_A').innerHTML=tempcode;
                  	document.getElementById('type_A').innerHTML=temptype;
            		return update_area();
                }        
                );
        $('#area_area_add').submit(
            	function(){
            		state=2;
            		tempname=$('#name_C').val();
            		tempcode=$('#code_C').val();
            		temptype=$('#type_C').val();
            		tempparentcode=$('#parentcode_C').html();
            		$("#modal-container-C").modal('hide');
            		return update_area();
                }        
                );
        $('#area_org_modify').submit(
            	function(){
            		org_state = 1;
            		org_code = $('#code_E').html();
            		org_name_new=$('#name_E').val();
            		org_areacode = $('#orgarea_E').html();
            		org_type = $('#type_E').html();
            		parentorgcode = $('#pcode_E').html();
            		levelorder = $('#orglevel_E').html();
            		$("#modal-container-E").modal('hide');
            		return fuc_update_org();
                }        
                );
          $('#area_org_add').submit(
                    	function(){
                    		org_state = 2;
                    		org_code = $('#code_D').val();
                    		org_name_new=$('#name_D').val();
                    		org_areacode = $('#orgarea_D').html();
                    		org_type = $('#type_D').val();
                    		parentorgcode = $('#pcode_D').val();
                    		levelorder = $('#select_D').val();
                    		//if(org_code==''){
                    			//document.getElementById('error_D').innerHTML="医疗机构编码不能为空！";
                    			//$('#error_D').style.display="";
                    			//document.getElementById('error_D').style.display="";
                    		//return false;
                    		//}
                    		document.getElementById('error_D').style.display="none";//格式正确时隐藏报错
                    		$('#code_D').val("");	//html内容清空
                    		$('#name_D').val("");  
                    		return fuc_update_org();
                        }        
                        );
                
        
	 });
