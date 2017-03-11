	var myMenu;
	window.onload = function() {
		myMenu = new SDMenu("my_menu");		//新建和初始化导航菜单
		myMenu.init();
		if (document.cookie && document.cookie != '') { //如果设置了cookie
			var scroolPosition = $.cookie('scroolPosition_'); //如果有cookie中记录了位置，设置滚动条位置为上次的位置
			if(scroolPosition != null){
				document.getElementById('left').scrollTop = Number(scroolPosition); //设置位置
			}
		}
	};
	//控制导航栏
	$(document).ready(function(e) {
		$(".Switch").click(function() {
			$(".left").toggle();
		});
	});
	//setScroll()使用cookie记录滚动条位置
	function setScroll(){
		var  scroolPosition= String(document.getElementById('left').scrollTop); // cookie是字符串
		$.cookie('scroolPosition_', scroolPosition, {  path: '/' }); // 使用cookie记忆滚动条位置
	}
//	if (document.cookie && document.cookie != '') { //如果设置了cookie
//	var regex2 = new RegExp("scroolPosition_" + "=([0-9]+)");		//恢复滚动条的位置
//	var match2 = regex2.exec(document.cookie); 			//在cookie中匹配滚动条位置关键字
//	if (match2) { 					//如果有cookie中记录了位置，设置滚动条位置为上次的位置
//		var scroolPosition = Number( match2[1]); 		//转换为数字
//		document.getElementById('left').scrollTop = scroolPosition; //设置位置
//	}
//}
	//document.cookie = "scroolPosition_" + "=" + scroolPosition + "; path=/"; ; // 使用cookie记忆滚动条位置