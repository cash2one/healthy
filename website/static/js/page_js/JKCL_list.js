	var page_number = 1;
	var total_page = 1;
	var nperpage=8;
	function doquery(isadd)
        {
			    var name = $('#name').val(); //姓名
			    var idCard = $('#idCard').val(); //身份证号码
                $.ajax({
                    type:"POST",
                    data: {
                    	idCard:idCard,
                    	name:name,
              			page_n:page_number+isadd, nperpage:nperpage,
              			},// 页码，每页的记录个数
                    url: "/JKCL_list_q/",//"{% url "YTJMeasure_list_q" %}", //后台处理函数的url 这里用的是static url 需要与urls.py中的name一致
                    cache: false,
                    dataType: "json",
                    success: function(result, statues, xml){
                    	page_number = page_number+isadd;
                    	total_records = result['number'];
                    	total_page = Math.ceil(result['number']/nperpage);
                    	var pg=page_number.toString()+'/'+total_page.toString();
                    	document.getElementById("pageinput").value=pg;
                    	
                    	$('#records_num').html("\t"+total_records+"\t");
                        $('#data').html(result['html'])                                        //成功时弹出view传回来的结果
                    },
                    error: function(){
                        alert("false");
                    }
                });
                return false;
        }
	
	$(document).ready(function(){
		
            $.ajaxSetup({
                 data: {csrfmiddlewaretoken: $('#csrf_token').html() },
            });
            var today = new Date();
            
            doquery(0);
        	$('#form_ehr_query').submit(
        	function(){
        		page_number = 1;
                return doquery(0);
            }        
            );
             
              $('#firstpage').click(
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
            