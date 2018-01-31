#!/home/raj/.rvm/rubies/ruby-2.4.1/bin/ruby

require 'open3'

server_ips = [
    "169.55.137.249",
    "169.55.137.248",
    "169.55.137.247",
    "158.85.100.135",
    "158.85.100.139",
    "158.85.100.140",
    "169.55.176.85",
    "169.55.176.94",
    "158.85.100.141",
    "158.85.100.134",
    "158.85.100.138",
    "158.85.100.136",
    "169.55.176.83",
    "158.85.100.132",
    "169.55.176.89",
    "169.55.137.233",
    "169.55.137.250"
]

#"ssh-copy-id -i /home/raj/.ssh/admin/rsa_key_file.pub root@#{ips}"

server_ips.each do |ips|
    Open3.popen3("ssh-copy-id -i /home/raj/.ssh/admin/rsa_key_file.pub root@#{ips}") do |stdin,stdout,stderr,wait_thr|
        puts "stdout #{stdout.read} => stderr #{stderr.read}, stdin #{stdin.read}"
    end
end
