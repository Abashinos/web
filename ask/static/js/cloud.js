<script type="text/javascript" src="swfobject.js"></script>
function  myTags(mytags){
		mytags=mytags.replace(/<A/g, '<a')
			.replace(/\/A>/g, "/a>")
			.replace(/(\starget=_)(\w*)/g, ' target="_$2"')
			.replace(/(\sclass=)(?!")(\w*)/g, ' class="$2"')
			.replace(/(\sname=)(?!")(\w*)/g, ' name="$2"')
			.replace(/(\sid=)(?!")(\w*)/g, ' id="$2"')
			.replace(/(\srel=)(?!")(\w*)/g, ' rel="$2"');
		mytags=encodeURIComponent(mytags).replace(/!/g, '%21')
			.replace(/'/g, '%27').replace(/\(/g, '%28')
			.replace(/\)/g, '%29').replace(/\*/g, '%2A');
		var rnumber = Math.floor(Math.random()*9999999);
		var flashvars = {
			tcolor:"0x2A62C8",
			tcolor2:"0x000000",
			hicolor:"0xB12AC8",
			tspeed:"110",
			distr:"true",
			mode:"tags",
			tagcloud:mytags
		};
		var params = {
			allowScriptAccess:"always",
			wmode:'transparent'
		};
		var attributes = {
			id:"flash_cloud"
		};
		swfobject.embedSWF("tagcloud.swf?r="+rnumber,
						   "tags", "600", "420", "9.0.0",
						   "expressInstall.swf", flashvars,
						   params, attributes);
	}
 
	window.onload=function(){ 
		var mytags="<tags>"
		+document.getElementById('tags').innerHTML
		+"</tags>";
		myTags(mytags);
	};