jQuery(".panel .title").click(function(){ 
	if ( jQuery(this).parent().hasClass("active") ) 
	{
		jQuery(".panel").removeClass("active");
	}
	else 
	{
		jQuery(".panel").removeClass("active");
		jQuery(this).parent().addClass("active");
	}
});