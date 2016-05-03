import sys


def parse(ll):
	parencounter = ""
	tablevel = 0
	end = []
	for l in ll:
		if l[0] == "\t":
			if l[tablevel]:
				if l[tablevel] == "\t":
					end.append(l[0] + "(" + l[1:])
					parencounter = parencounter + ")"
					tablevel += 1
				else: 
					end.append("(" + l + ")")
			# this is all a dirty hack based on 0-based indexing.
		elif l[0] == "":
			end.append(parencounter + l)
			tablevel = 0
		elif tablevel == 0:
			end.append(l)
		else:
			end.append("(" + l + ")")
	end.append(parencounter)
	print end
	print
	return "".join(end)
			# it would be nice to just append the close parens to the end of previous line, but maybe that's an after-the-fact task
			# consequence of this is it won't allow implicit line continuations...

# this isn't working, is putting close parens in front of lines that shouldn't have close parens. 

if __name__ == "__main__":
	with open(sys.argv[1]) as f:
		lines = f.readlines()
		print lines
		print
		print parse(lines)


