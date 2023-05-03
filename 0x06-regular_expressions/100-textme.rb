#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:([A-z,a-z,0-9,+]*)\] \[to:([A-Z,a-z,0-9,+]*)\] \[flags:([-,0-1,:]*)\]/).join(',')
