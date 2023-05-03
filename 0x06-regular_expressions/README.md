# Project - 0x06. Regular expression

#### Concepts
*For this project, we'll consider this concept:*
- Regular Expression

## Background Context
For this project, I have to build my regular expression using Oniguruma,
a regular expression library that which is used by Ruby by default.
Other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex),
here is the Ruby code that will be used, just replace the regexp part, meaning the code in between the //:

	sylvain@ubuntu$ cat example.rb
	#!/usr/bin/env ruby
	puts ARGV[0].scan(/127.0.0.[0-9]/).join
	sylvain@ubuntu$
	sylvain@ubuntu$ ./example.rb 127.0.0.2
	127.0.0.2
	sylvain@ubuntu$ ./example.rb 127.0.0.1
	127.0.0.1
	sylvain@ubuntu$ ./example.rb 127.0.0.a
