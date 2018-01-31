#!/home/raj/.rvm/rubies/ruby-2.4.1/bin/ruby

require 'csv'

wh = CSV.open("output.csv", "wb")
id_val = ""

CSV.foreach('/home/raj/Downloads/ConditionSalesCSV.csv') do |row|
	id = []
	row.each do |cell|
		if cell.is_a?(String)
			if cell.size == 10
				id_val = cell
				id << cell
			else
				id << id_val
			end
		else
			id << ""
		end
		
	end
	wh <<  [ id.join(",") ]
end

