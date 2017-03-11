//类似XX_list.js文件，phy_list.js的注释是最全面的。
	var page_number = 1; 	//当前页码
	var total_page = 1;		//页面总数
	var nperpage=8;		//每一页显示的记录条数
	!function() {	//日历格式
		laydate.skin('molv');
		laydate({
			elem : '#Calendar1'
		});
		laydate({
			elem : '#Calendar2'
		});
	}();
	 function doquery(isadd) //查询函数
        {
        		var liveaddr=$('#select1').val();	//页面第一行变量
        		var street=$('#select2').val();
        		var community=$('#select3').val();
        		var institution=$('#select4').val(); 
			    var name = $('#name').val();                //获得form中用户输入的name 注意这里的id_name 与你html中的id一致
			     
			    var date1 = $('#Calendar1').val();	//第二行变量
			    var date2 = $('#Calendar2').val(); 
			    var input1 = $('#input1').val();	//第三行变量
			    var input2 = $('#input2').val(); 
                var gender=$('#sex').val();
                
                var radio = document.getElementsByName("sex");	//获取互斥项的值
                var radioLength = radio.length;
                for(var i = 0;i < radioLength;i++)
				   {
				    if(radio[i].checked)
				    {
				     gender = radio[i].value;
				    
				    }
				   }
				//使用ajax函数异步请求，向后台查询，并局部刷新页面
                $.ajax({
                    type:"POST",
                    data: {	//POST请求的数据（这里是查询参数）
                  		 householdRegisterCode:liveaddr, //#户籍地代码
                  		 street:street,
                  		 community:community,
                  		 registerOrgCode:institution, //建档单位编号
            			 name:name, genderCode:gender, //#姓名#性别代码 
             			 star:date1, end:date2,//#建档时间起止范围
             			 personId:input1, healthFileNumber:input2,  //#居民身份证号#健康档案编号
              			 page_n:page_number+isadd, nperpage:nperpage, // 页码，每页的记录个数
              			 },
                    url: "/phy_list_q/",	//"{% url "phy_list_q" %}", //后台处理函数的url 如果使用django语法，这里用的是static url 需要与urls.py中的name一致
                    cache: false,
                    dataType: "json",		//设置返回值类型
                    success: function(result, statues, xml){ //请求成功返回时，调用的函数
                    	page_number = page_number+isadd;	//页码
                    	total_records = result['number'];	//总的记录条数，从返回值中获取
                    	total_page = Math.ceil(result['number']/nperpage); //页面显示的参数
                    	var pg=page_number.toString()+'/'+total_page.toString(); 
                    	document.getElementById("pageinput").value=pg;
                    	
                    	$('#records_num').html("\t"+total_records+"\t");
                        $('#data').html(result['html'])   //重新填入页面#data中
                    },
                    error: function(){ //请求失败时调用的函数
                        alert("false");
                    }
                });
                return false;
        }
	
	$(document).ready(function(){
		//                $.ajax({
         //         traditional: true//这个设置为true阻止深度序列化，data:{"steps":["qwe","asd","zxc"]}会转换成steps=qwe&steps=asd&...//默认的话，traditional为false，即jquery会深度序列化参数对象，
          //        }); //加上这句刷新一次，会请求两次phy_list,原因是这个函数$.ajax()会请求服务器，默认的url是当前页地址，也就是phy_list //参考http://www.php100.com/html/program/jquery/2013/0905/6004.html
            $.ajaxSetup({  //设置全局 AJAX 默认选项
                 data: {csrfmiddlewaretoken: $('#csrf_token').html() }, //django使用csrf_token进行跨站请求伪造保护，POST请求数据中需要设置该字段
            });
            var today = new Date();
		    document.getElementById("Calendar2").value = today.getFullYear()+"-"+(today.getMonth()+1)+"-"+(today.getDate()+1);
            doquery(0);
        	$('#form_ehr_query').submit(  //将函数绑定到 submit 事件
	        	function(){
	        		page_number = 1;
	                return doquery(0);
	            }        
            );
             
              $('#firstpage').click( //将函数绑定到 click 事件
	        	function(){
	        		page_number=1
	                return doquery(0);
	            }        
            );
             $('#prepage').click(
	        	function(){
	        		if(page_number>1)
	                	return doquery(-1);
	            }        
            );
             $('#nextpage').click(
	        	function(){
	        		if(page_number<total_page)
	                	return doquery (1);
	            }        
            );
            $('#lastpage').click(
        	function(){
        		page_number=total_page
                return doquery(0);
            }        
            );
            
        });
            

