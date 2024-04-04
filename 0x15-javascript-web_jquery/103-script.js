$(document).ready(function () {
	function fetchHello() {
		const langCode = $('INPUT#language_code').val();
		$.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: langCode }, function(data) {
			$('DIV#hello').text(data.hello);
		});
	}
	$('INPUT#btn_translate').click(fetchHello);
	$('INPUT#language_code').keypress(function(event) {
		if (event.which === 13) {
			fetchHello();
		}
	});
});
