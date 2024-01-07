#!/usr/bin/env ruby
name1 = ARGV[0].scan(/(?<=from:)[a-zA-Z0-9]+/).join
name2 = ARGV[0].scan(/(?<=to:)[+A-Za-z0-9]+/).join
name3 = ARGV[0].scan(/(?<=flags:)[-:0-1]+/).join
puts "#{name1},#{name2},#{name3}"
