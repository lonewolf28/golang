#!/home/raj/.rvm/rubies/ruby-2.4.1/bin/ruby

require 'nokogiri'
require 'open-uri'
require 'csv'

doc = File.open('./tweed.html'){ |f| Nokogiri::HTML(f) }
names = []
thcs = []

doc.xpath('//h4/span').each do |e|
    if e.text.empty? || e.text.nil?
        next
    else
        cost, name = e.text.split("\n")
        if ! name.nil?
            name.strip!
            name = name
            names << name
        end
    end
end

doc.xpath('//p').each do |t|
    if t.text.empty? || t.text.nil?
        next
    else
        thc, * = t.text.split("\n")
        thcs << thc
    end
end

thcs.reject! { |r| r.empty? }
thcx = thcs.each_slice(2).to_a
csv_w = CSV.open("tweed.csv", "w")

names.zip(thcx) do |elms|
    csv_w << elms.flatten
end
