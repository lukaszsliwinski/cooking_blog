jQuery(".menu__wrapper .menu__title").click(function(){ 
	if ( jQuery(this).parent().hasClass("active") ) 
	{
		jQuery(".menu__wrapper").removeClass("active");
	}
	else 
	{
        jQuery(".menu__wrapper").removeClass("active");
        jQuery(this).parent().addClass("active");
	}
});