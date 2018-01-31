#!/usr/bin/ruby
require 'net/http'
require 'uri'




def web_site_alive
    web_addr = '104.156.64.188'
    port_url = { '8080': 'dcf', '8081': 'prc', '8082': 'topi' }
    port_url.each do | port, sub_url |
        url = 'http://' + web_addr + ':' + port.to_s + '/' + sub_url
        begin
            esp_addr = URI.escape(url)
            uri = URI.parse(esp_addr)
            res = Net::HTTP.get_response(URI(uri))
            #puts res.body if res.is_a?(Net::HTTPSuccess)
        rescue Exception => e
            puts e.message
        else
            puts "URL: #{url}: #{res}"
        end
    end
end


web_site_alive


