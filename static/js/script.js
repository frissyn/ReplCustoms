function fadeInWebpage() {
	jQuery('body').css('display','none');
	jQuery(document).ready(function() {
		jQuery('body').fadeIn(2000);
		jQuery('a').on('click',function(event) {
			var thetarget = this.getAttribute('target')
			if (thetarget != "_blank") {
				var thehref = this.getAttribute('href')
				event.preventDefault();
				jQuery('body').fadeOut(function(){
					window.location = thehref
				});
			}});
		});
	setTimeout(function() {
		jQuery('body').fadeIn();
		}, 2000)
};

function transferTo(tag) {
	window.location.href = tag;
};

function sendTo(link) {
	window.open(link, '_blank');
};