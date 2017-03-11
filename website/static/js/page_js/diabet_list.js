  var page_number = 1;	//页码
  var total_page = 1;	//总页数，会被查询修改
  var nperpage=3;	//每页记录条数
  
  !function() {
    laydate.skin('molv');
    laydate({
      elem : '#Calendar1'
      });
      laydate.skin('molv');
      laydate({
        elem : '#Calendar2'
        });
        }();
  function doquery(isadd)
        {
          var name = $('#name').val();                //获得form中用户输入的name 注意这里的id_name 与你html中的id一致
          var date1 = $('#Calendar1').val();
          var date2 = $('#Calendar2').val(); //第二行变量
          var input1 = $('#input1').val();
          var input2 = $('#input2').val(); //第三行变量
          var gender=$('#sex').val();

          var radio = document.getElementsByName("sex");
          var radioLength = radio.length;
          for(var i = 0;i < radioLength;i++)
          {
            if(radio[i].checked)
            {
              gender = radio[i].value;

            }
          }

          $.ajax({
            type:"POST",
            data: {
              name:name, genderCode:gender, //#姓名#性别代码
              star:date1, end:date2,//#建档时间起止范围
              personId:input1, healthFileNumber:input2,  //#居民身份证号#健康档案编号
              page_n:page_number+isadd, nperpage:nperpage,// 页码，每页的记录个数
              },
              url: "/diabet_list_q/",//"{% url 'diabet_list_q' %}", //后台处理函数的url 这里用的是static url 需要与urls.py中的name一致
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
      		    	document.getElementById("Calendar2").value = today.getFullYear()+"-"+(today.getMonth()+1)+"-"+(today.getDate()+1);
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

