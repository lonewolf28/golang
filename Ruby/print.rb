#!/home/raj/.rvm/rubies/ruby-2.4.1/bin/ruby

pdf = Dir["/home/raj/srv/www/shop.medreleaf.com/current/web/app/uploads/consent-forms/*"]

pdf.each do |p|
	 system("/usr/bin/lpr #{p} ")
end
